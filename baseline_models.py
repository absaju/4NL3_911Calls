import gensim
from gensim.models import Word2Vec, KeyedVectors
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import re
from datasets import load_dataset
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from wefe.metrics import WEAT
from wefe.datasets import load_weat
from wefe.query import Query
from wefe.word_embedding_model import WordEmbeddingModel
from wefe.utils import run_queries

import nltk
nltk.download('wordnet')

def lower(text):
    return text.lower()

def rem_punc(text):
    return re.sub(r'[^\w\s]', ' ', text)

def rem_stopwords(list):
    stop_words = stopwords.words('english')
    return [word for word in list if word not in stop_words]

def lem(list):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for word in list]

def stem(list):
    ps = PorterStemmer()
    return [ps.stem(word) for word in list]

def preprocessing(text, stemy=False):
    text = lower(text)
    text = rem_punc(text)
    text = re.sub(r'\d+', '', text)
    list = text.split()
    list = lem(list)
    if stemy: list = stem(list)
    list = rem_stopwords(list)
    return " ".join(list)

bOw = pd.read_csv("./Bag_of_Words/Restaurant_Reviews.tsv",delimiter='\t')

corpus=[]
y = bOw['Liked'].values
for i in range(0,1000):
    corpus.append(preprocessing(bOw['Review'][i]))

cv = CountVectorizer()
x = cv.fit_transform(corpus).toarray()


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)
#GenAI used
classifier = LogisticRegression()
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy:.4f}")
print("\nClassification Report (bOw Approach):")
print(report)