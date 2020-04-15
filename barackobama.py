#Collecting, Cleaning, and Analyzing data for Barack Obama
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


#Obama 2008 Article Search
def get_url (q, begin_date, end_date):
    url = ("https://api.nytimes.com/svc/search/v2/articlesearch.json?q="+q+"&facet_fields=source&facet=true&begin_date="+begin_date+"&end_date="+end_date+"&api-key=MRAJUxGvim9gZYw4sGZ0ZH9hAgLrAeDR")
    return url

r = requests.get(get_url("obama, barack", "20080101", "20081231"))

r= r.json()['response']['docs']

obama = ""

for i in r:
    obama += (" "+ i['abstract'])
    
obama


#Obama 2012 Article Search
r = requests.get(get_url("obama, barack", "20120101", "20121231"))

r=r.json()['response']['docs']

#obama12 = ""

for i in r:
    obama += (" "+ i['abstract'])
    
obama


#TOKENIZING AND ANALYZING SENTENCES
tokenized_text=sent_tokenize(obama)
print(tokenized_text)


#CLEANING AND TOKENIZING WORDS
#removing punctuation
obama_w = re.sub(r'[^(a-zA-Z)\s]','', obama)
obama_w


#tokenize words
tokenized_word=word_tokenize(obama_w)
tokenized_word


#make everything lowercase and remove stop words
stop_words = stopwords.words('english')
tokenized_word = [each_string.lower() for each_string in tokenized_word]
tokenized_word = [word for word in tokenized_word if word not in stop_words]


#PLOT freq dist of the words used to describe obama
fdist = FreqDist(tokenized_word)
fdist.plot(30,cumulative=False)
plt.show()
