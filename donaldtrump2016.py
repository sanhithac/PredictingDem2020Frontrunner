#Cleaning, Tokenizing, and Analyzing data for Donald Trump
import requests
import json
import re
import pandas as pd
import matplotlib.pyplot as plt

#install before running if you don't have NLTK
!pip install nltk
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize

#getting data for donald trump 2016
def get_url (q, begin_date, end_date):
    url = ("https://api.nytimes.com/svc/search/v2/articlesearch.json?q="+q+"&facet_fields=source&facet=true&begin_date="+begin_date+"&end_date="+end_date+"&api-key=MRAJUxGvim9gZYw4sGZ0ZH9hAgLrAeDR")
    return url

r = requests.get(get_url("trump, donald", "20160101", "20161231"))

r= r.json()['response']['docs']

#getting abstracts for the articles where Trump is mentioned in 2016
trump16 = ""

for i in r:
    trump16 += (" "+ i['abstract'])
    
trump16


#TOKENIZING AND ANALYZING SENTENCES
tokenized_text=sent_tokenize(trump16)
print(tokenized_text)


#CLEANING AND TOKENIZING WORDS
#getting rid of punctuation
trump16 = re.sub(r'[^(a-zA-Z)\s]','', trump16)


#tokenize words
tokenized_word=word_tokenize(trump16)


#make everything lowercase and remove stop words
stop_words = stopwords.words('english')
tokenized_word = [each_string.lower() for each_string in tokenized_word]
tokenized_word = [word for word in tokenized_word if word not in stop_words]


#plot freq dist of the words used to describe Romney
fdist = FreqDist(tokenized_word)
fdist.plot(30,cumulative=False)
plt.show()
