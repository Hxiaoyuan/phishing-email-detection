# phishing-email-detection
钓鱼网站侦查

数据集下载
cd ~/projects/phishing/data/phishing/nazario/
wget -r --no-parent --level=1 --reject "index.html*" --wait=1 https://monkey.org/~jose/phishing/
cp ./monkey.org/~jose/phishing/* ./

cd ~/projects/phishing/data/legitimate/enron
wget https://www.cs.cmu.edu/~enron/enron_mail_20150507.tar.gz
tar -x -f enron_mail_20150507.tar.gz


```
step1: data_handle 将下载数据合并存储为csv
step2: dataset-cleanup 数据清晰

Text Data Preprocessing.ipynb Conversion of the email strings to lemmatized lists of words for vectorization features and preprocessing for style features.
Text Feature Extraction and Feature Selection.ipynb Vectorization of the text to create numeric features usig Word2Vec and TF-IDF and selection of top TF-IDF features.
Text Data Classification (baseline).ipynb Baseline algorithm training, predictions and evaluation metrics using the vectorized text as features.
Stylometric Feature Extraction.ipynb Creation of stylometric features.
Style Features Classification (baseline).ipynb Baseline algorithm training, predictions and evaluation metrics using style features.
Style and Content Classification.ipynb Final predictions and evaluation using feature set merging and model stacking to combine the two feature sets

```


