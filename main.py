# import library for manipulating data
import numpy as np
import pandas as pd

import re # regex
from datetime import datetime
from operator import itemgetter

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

THRESHOLD = .2

# define functions ===================================================#
def removeSpecial(text):
    # Using regular expression to remove special characters and double whitespace
    cleaned_text = re.sub(r'[^\w\s]', '', str(text))  # Remove special characters
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)  # Replace multiple spaces with a single space
    return cleaned_text.strip()  # Remove leading and trailing spaces

def removeSpecialNumbers(text):
    # Using regular expression to remove special characters and double whitespace
    cleaned_text = re.sub(r'\w*\d\w*', ' ', text).strip()
    cleaned_text = re.sub(r'[^\w\s]', '', str(cleaned_text))  # Remove special characters
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)  # Replace multiple spaces with a single space
    return cleaned_text.strip()  # Remove leading and trailing spaces

stop_words = set(stopwords.words('indonesian'))
stop_words.update(['pupuk', 'coklat', 'butiran'])
def tokenize_word(string):
    str_clean = removeSpecial(str(string).lower())
    tokenized = word_tokenize(str_clean)
    return [word for word in set(tokenized) if word not in stop_words]

def tokenize_word_number(string):
    stop_words.update(['gram', 'lt', 'liter', 'litre', 'gr', 'kg', 'ml', 'l', 'ltr'])
    str_clean = removeSpecialNumbers(str(string).lower())
    tokenized = word_tokenize(str_clean)
    return [word for word in set(tokenized) if word not in stop_words]

# Function to calculate Jaccard similarity
def jaccard_similarity(a, b):
    intersection = len(set(a).intersection(b))
    union = len(a) + len(b) - intersection
    return intersection / union

# data all pupuk =====================================================#
df_pupuk = pd.read_pickle('data_pupuk_all_ready.pkl')
descriptions = [scr for scr in df_pupuk.T.to_dict().values()]

# Get similarity Functions ===========================================#
def getSimilarProduct(pos):
    product_name_clean = tokenize_word(pos)
    product_name_nonumber = tokenize_word_number(pos)

    local_match = []
    for desc in descriptions:
        similarity_lv1 = jaccard_similarity(product_name_nonumber, desc['description_nonumber'])
        if similarity_lv1 > 0:
            local_match_temp = {'pos_name': pos,
                                'pos_rawtext_clean': product_name_clean,
                                'pos_rawtext_nonumber': product_name_nonumber,
                                'similarity_lv1': similarity_lv1,
                                'match_id': desc['index'],
                                'match_text': desc['Product SKU'],
                                'match_raw_clean': desc['description_clean'],
                                'match_raw_nonumber': desc['description_nonumber']}
            local_match.append(local_match_temp)
    match_out = {'pos_name': pos,
                'pos_rawtext_clean': product_name_clean,
                'pos_rawtext_nonumber': product_name_nonumber,
                'similarity_lv1': 0,
                'match_id': None,
                'match_text': None,
                'match_raw_clean': None,
                'match_raw_nonumber': None,
                'similarity_lv2': 0}
    if local_match.__len__() != 0:
        max_similarity = 0
        for match in local_match:
            similarity_lv2 = jaccard_similarity(match['pos_rawtext_clean'], match['match_raw_clean'])
            if similarity_lv2 > max_similarity:
                match_out = match
                match_out['similarity_lv2'] = similarity_lv2
                
                max_similarity = similarity_lv2

    classification = 'match' if match_out['similarity_lv2'] > THRESHOLD else 'not match'
    best_match = descriptions[match_out['match_id']] if match_out['match_id'] != None else None
    output = {'time' : datetime.today(),
              'product': pos,
              'classification': classification,
              'best_match': best_match,
              'similarity': match_out['similarity_lv2']}
    return output

def inserttoData(f):
    data = pd.read_csv('data_result_similarities.csv')
    print(f)
    if f['best_match'] != None:
        feedback_insert = {'id': max(data['id'])+1,
                        'product':f['product'],
                        'match_index': f['best_match']['index'],
                        'match_product': f['best_match']['Product SKU'],
                        'match_brand': f['best_match']['Brand'],
                        'match_type': f['best_match']['Type'],
                        'match_category': f['best_match']['Category'],
                        'match_formula': f['best_match']['Formula'],
                        'match_new_sku': f['best_match']['new_sku'],
                        'match_description': f['best_match']['description'],
                        'similarity': f['similarity'],
                        'class': 1 if f['classification'] == 'match' else 0,
                        'class_desc': f['classification'],
                        'time': datetime.now()}
    else:
        feedback_insert = {'id': max(data['id'])+1,
                        'product':f['product'],
                        'match_index': None,
                        'match_product': None,
                        'match_brand': None,
                        'match_type': None,
                        'match_category': None,
                        'match_formula': None,
                        'match_new_sku': None,
                        'match_description': None,
                        'similarity': f['similarity'],
                        'class': 1 if f['classification'] == 'match' else 0,
                        'class_desc': f['classification'],
                        'time': datetime.now()}
    df_toinsert = pd.DataFrame([feedback_insert])
    df_toinsert.to_csv('data_result_similarities.csv', mode='a', index=False, header=False)

# Get similar list ==========================================#
def getListSimilar(pos):
    product_name_clean = tokenize_word(pos)
    product_name_nonumber = tokenize_word_number(pos)

    local_match = []
    for desc in descriptions:
        similarity_lv1 = jaccard_similarity(product_name_nonumber, desc['description_nonumber'])
        if similarity_lv1 > 0:
            local_match_temp = {'pos_name': pos,
                                'pos_rawtext_clean': product_name_clean,
                                'pos_rawtext_nonumber': product_name_nonumber,
                                'similarity_lv1': similarity_lv1,
                                'match_id': desc['index'],
                                'match_text': desc['Product SKU'],
                                'match_raw_clean': desc['description_clean'],
                                'match_raw_nonumber': desc['description_nonumber']}
            local_match.append(local_match_temp)
    
    match_out = []
    for match in local_match:
        similarity_lv2 = jaccard_similarity(match['pos_rawtext_clean'], match['match_raw_clean'])
        if similarity_lv2 > THRESHOLD:
            desc_out = descriptions[match['match_id']]
            desc_out['similarity'] = similarity_lv2
            match_out.append(desc_out)
            del desc_out['description_nonumber']
            del desc_out['description_clean']
    print(len(match_out))
    return sorted(match_out, key=itemgetter('similarity'), reverse=True)

def insertbyIndex(i):
    data = pd.read_csv('data_result_similarities.csv')
    f = descriptions[int(i)]
    print(f)
    feedback_insert = {'id': max(data['id'])+1,
                    'product': f['Product SKU'],
                    'match_index': f['index'],
                    'match_product': f['Product SKU'],
                    'match_brand': f['Brand'],
                    'match_type': f['Type'],
                    'match_category': f['Category'],
                    'match_formula': f['Formula'],
                    'match_new_sku': f['new_sku'],
                    'match_description': f['description'],
                    'similarity': 1,
                    'class': 1,
                    'class_desc': 'match',
                    'time': datetime.now()}
    df_toinsert = pd.DataFrame([feedback_insert])
    df_toinsert.to_csv('data_result_similarities.csv', mode='a', index=False, header=False)