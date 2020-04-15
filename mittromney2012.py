#Cleaning, Tokenizing, and Analyzing data for Mitt Romney
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

#getting data for mitt romney 2012
def get_url (q, begin_date, end_date):
    url = ("https://api.nytimes.com/svc/search/v2/articlesearch.json?q="+q+"&facet_fields=source&facet=true&begin_date="+begin_date+"&end_date="+end_date+"&api-key=MRAJUxGvim9gZYw4sGZ0ZH9hAgLrAeDR")
    return url

r = requests.get(get_url("romney, mitt", "20120101", "20121231"))

r= r.json()['response']['docs']

#getting abstracts for the articles where Romney is mentioned in 2012
romney12 = ""

for i in r:
    romney12 += (" "+ i['abstract'])
    
romney12

#TOKENIZING AND ANALYZING SENTENCES
tokenized_text=sent_tokenize(romney12)
print(tokenized_text)


#CLEANING AND TOKENIZING WORDS
#getting rid of punctuation
romney12 = re.sub(r'[^(a-zA-Z)\s]','', romney12)


#tokenize words
tokenized_word=word_tokenize(romney12)


#make everything lowercase and remove stop words
stop_words = stopwords.words('english')
tokenized_word = [each_string.lower() for each_string in tokenized_word]
tokenized_word = [word for word in tokenized_word if word not in stop_words]


#plot freq dist of the words used to describe Romney
fdist = FreqDist(tokenized_word)
fdist.plot(30,cumulative=False)
plt.show()
