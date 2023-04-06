import raw_utils as util
import os

import pandas as pd
import numpy as np

import random
random.seed(1746)

# ===========================处理所有文件数据集合并成csv

# Paths
cwd = os.getcwd()
nazario_path = os.path.join(cwd, 'dataset/phishing/nazario/')
enron_path = os.path.join(cwd, 'dataset/legitimate/enron/')

csv_path = os.path.join(cwd, 'dataset/csv/')

files_ignored = ['README.txt']
files_ignored_recent = ['README.txt', '20051114.mbox',  'phishing0.mbox',  'phishing1.mbox',  'phishing2.mbox',  'phishing3.mbox', 'private-phishing4.mbox']

phishing = util.read_dataset(nazario_path, files_ignored, text_only=True)

print(phishing.info())

util.save_to_csv(phishing, csv_path, 'nazario_full.csv')

phishing_recent = util.read_dataset(nazario_path, files_ignored_recent, text_only=True)

print(phishing_recent.info())

util.save_to_csv(phishing_recent, csv_path, 'nazario_recent.csv')

filename = util.sample_enron_to_mbox(enron_path, 2000)
enron_2000 = util.mbox_to_df(filename, enron_path+'/mbox', text_only=True)
util.save_to_csv(enron_2000, csv_path, 'enron_text_2000.csv')

filename = util.sample_enron_to_mbox(enron_path, 20000)
enron_20000 = util.mbox_to_df(filename, enron_path+'/mbox', text_only=True)
util.save_to_csv(enron_20000, csv_path, 'enron_text_20000.csv')

