import os

from raw_utils import save_to_csv
import preprocessing as util

import pandas as pd
import numpy as np
#%%
# Paths
cwd = os.getcwd()
csv_path = os.path.join(cwd, 'data/csv/')

# Filenames
nazario_csv = 'nazario_recent.csv'
enron_csv = ['enron_text_2000.csv', 'enron_text_20000.csv']

phishing_text_raw = pd.read_csv(os.path.join(csv_path, nazario_csv), index_col=0, dtype={'body': 'object'})
print(phishing_text_raw.info())

phishing_text_raw = phishing_text_raw.dropna()
phishing_text = phishing_text_raw[phishing_text_raw['body'].apply(util.check_empty) == False]
print(phishing_text.shape)

phishing_text = phishing_text[phishing_text['body'].str.contains("This text is part of the internal format of your mail folder, and is not\na real message.") == False]
print(phishing_text.shape)

phishing_text = phishing_text[phishing_text.duplicated(keep='first') == False]
print(phishing_text.shape)

legit_text_small_raw = pd.read_csv(os.path.join(csv_path, enron_csv[0]), index_col=0, dtype={'body': 'object'})
print(legit_text_small_raw.info())

legit_text_big_raw = pd.read_csv(os.path.join(csv_path, enron_csv[1]), index_col=0, dtype={'body': 'object'})
print(legit_text_big_raw.info())

legit_text_small_raw = legit_text_small_raw.dropna()
print(legit_text_small_raw.shape)

legit_text_big_raw = legit_text_big_raw.dropna()
print(legit_text_big_raw.shape)

legit_text_small = legit_text_small_raw[legit_text_small_raw['body'].apply(util.check_empty) == False]
print(legit_text_small.shape)

legit_text_big = legit_text_big_raw[legit_text_big_raw['body'].apply(util.check_empty) == False]
print(legit_text_big.shape)

legit_text_small = legit_text_small[legit_text_small.duplicated(keep='first') == False]
print(legit_text_small.shape)

legit_text_big = legit_text_big[legit_text_big.duplicated(keep='first') == False]
print(legit_text_big.shape)

phishing_text['class'] = 1

legit_text_small = legit_text_small.sample(n=1688, random_state=1746)
legit_text_small['class'] = 0
#%%
balanced = pd.concat([phishing_text, legit_text_small])
balanced = balanced.sample(frac=1, random_state=1746).reset_index(drop=True)
balanced.insert(0, 'id', balanced.index)
#%%
save_to_csv(balanced, csv_path, 'balanced.csv')

legit_text_big = legit_text_big.sample(n=16880, random_state=1746)
legit_text_big['class'] = 0
#%%
imbalanced = pd.concat([phishing_text, legit_text_big])
imbalanced = imbalanced.sample(frac=1, random_state=1746).reset_index(drop=True)
imbalanced.insert(0, 'id', imbalanced.index)
#%%
save_to_csv(imbalanced, csv_path, 'imbalanced.csv')