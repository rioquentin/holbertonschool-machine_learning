#!/usr/bin/env python3

import pandas as pd
from tqdm import tqdm
import string
import re
import unidecode
from transformers import BertTokenizer, BertModel
import torch
from sklearn.metrics.pairwise import cosine_similarity


def preprocess_text(text):
    """
    Effectue une série d'étapes de prétraitement sur le texte donné.
    
    Args:
        text (str): Le texte à prétraiter.
        
    Returns:
        str: Le texte après prétraitement.
    """
    text = text.lower()
    text = re.sub(r'[{}]'.format(string.punctuation), ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    if text.endswith(" hf"):
        text = text[:-3].strip()
    text = unidecode.unidecode(text)
    return text


def load_data(file_path):
    """
    Charge les données à partir du fichier Excel donné.
    
    Args:
        file_path (str): Chemin vers le fichier Excel contenant les données.
        
    Returns:
        tuple: Un tuple contenant les DataFrames des données ROME et PNT.
    """
    rome_data = pd.read_excel(file_path, sheet_name="ROME OGR")
    pnt_data = pd.read_excel(file_path, sheet_name="professions Lucie PNT-TK")
    return rome_data, pnt_data


# Initialisation du modèle BERT
tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')
model = BertModel.from_pretrained('bert-base-multilingual-cased')


def get_embedding(text):
    """
    Calcule la représentation sémantique moyenne du texte en utilisant BERT.
    
    Args:
        text (str): Le texte pour lequel la représentation doit être calculée.
        
    Returns:
        torch.Tensor: La représentation sémantique moyenne calculée.
    """
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).numpy()


def bert_similarity(text1, text2):
    """
    Calcule la similarité cosinus entre deux textes en utilisant BERT.
    
    Args:
        text1 (str): Le premier texte.
        text2 (str): Le deuxième texte.
        
    Returns:
        float: La similarité cosinus entre les deux textes.
    """
    emb1 = get_embedding(text1)
    emb2 = get_embedding(text2)
    return cosine_similarity(emb1, emb2)[0][0]


def find_best_match_with_bert(row, pnt_data):
    """
    Trouve la meilleure correspondance en fonction de la similarité BERT pour une ligne de données ROME.
    
    Args:
        row (pd.Series): La ligne de données ROME.
        pnt_data (pd.DataFrame): Les données PNT-TK pour la correspondance.
        
    Returns:
        tuple: Un tuple contenant la meilleure correspondance et le score de similarité.
    """
    best_match = None
    best_score = 0
    for _, pnt_row in pnt_data.iterrows():
        score = bert_similarity(row['experience/masculineName'], pnt_row['description'])
        if score > best_score:
            best_match = pnt_row['description']
            best_score = score
    return best_match, best_score


def assign_code_tk(row, pnt_data):
    """
    Attribution du code TK en fonction du seuil de similarité.
    
    Args:
        row (pd.Series): La ligne de données ROME.
        pnt_data (pd.DataFrame): Les données PNT-TK pour la correspondance.
        
    Returns:
        str: Le code TK attribué ou None si le seuil n'est pas atteint.
    """
    if row['Match Percentage'] > 0.8:  # 80% comme seuil pour la similarité cosinus
        match = pnt_data[pnt_data['description'] == row['Best Match']]
        if not match.empty:
            return match['code tk'].iloc[0]
    return None


def main():
    tqdm.pandas()

    file_path = "tableaufull.xlsx"
    output_file = "correspondence_output_with_percentage.xlsx"

    # Chargement des données
    rome_data, pnt_data = load_data(file_path)
    
    # Prétraitement des données
    rome_data['experience/masculineName'] = rome_data['experience/masculineName'].apply(preprocess_text)
    pnt_data['description'] = pnt_data['description'].apply(preprocess_text)

    # Calcul des correspondances avec BERT
    rome_data['Best Match'], rome_data['Match Percentage'] = zip(*rome_data.progress_apply(find_best_match_with_bert, pnt_data=pnt_data, axis=1))

    # Attribution des codes TK
    rome_data['LUCIE'] = rome_data.apply(assign_code_tk, pnt_data=pnt_data, axis=1)

    # Préparation des données pour le fichier de sortie
    pnt_data['experience/masculineName'] = pnt_data['description']
    pnt_data['Best Match'] = pnt_data['description']
    columns_to_keep = ['experience/masculineName', 'Best Match', 'description']
    table_de_correspondance = pd.merge(rome_data, pnt_data[columns_to_keep], left_on='Best Match', right_on='description', how='left')
    table_de_correspondance = table_de_correspondance.drop(columns=['description'])
    table_de_correspondance = table_de_correspondance.rename(columns={'experience/masculineName_x': 'Intitulé_Rome_Pole_Emploi', 'Best Match_x': 'Intitulé_PNT_TextKernel'})
    table_de_correspondance = table_de_correspondance.sort_values(by='Match Percentage', ascending=False)

    # Écriture des résultats dans un fichier Excel
    with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
        table_de_correspondance.to_excel(writer, index=False, sheet_name='Correspondences')

    print(f"Les correspondances ont été écrites dans '{output_file}'.")

if __name__ == "__main__":
    main()