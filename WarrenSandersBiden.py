import requests
import json
import re
import pandas as pd
import matplotlib.pyplot as plt

#install before running if you don't have NLTK
#!pip install nltk
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize


def get_url (q, begin_date, end_date):
    url = ("https://api.nytimes.com/svc/search/v2/articlesearch.json?q="+q+"&facet_fields=source&facet=true&begin_date="+begin_date+"&end_date="+end_date+"&api-key=MRAJUxGvim9gZYw4sGZ0ZH9hAgLrAeDR")
    return url



#Cleaning, Tokenizing, and Analyzing data for Bernie Sanders 2020
#getting data for Bernie Sanders
def get_url (q, begin_date, end_date):
    url = ("https://api.nytimes.com/svc/search/v2/articlesearch.json?q="+q+"&facet_fields=source&facet=true&begin_date="+begin_date+"&end_date="+end_date+"&api-key=MRAJUxGvim9gZYw4sGZ0ZH9hAgLrAeDR")
    return url

r = requests.get(get_url("sanders, bernie", "20190101", "20200301"))

r= r.json()['response']['docs']

#getting abstracts for the articles where Trump is mentioned in 2016
bernie = ""

for i in r:
    bernie += i['abstract']
    
bernie


#TOKENIZING AND ANALYZING SENTENCES
tokenized_text=sent_tokenize(bernie)
print(tokenized_text)


#CLEANING AND TOKENIZING WORDS
#getting rid of punctuation
bernie = re.sub(r'[^(a-zA-Z)\s]','', bernie)


#tokenize words
tokenized_word=word_tokenize(bernie)


#make everything lowercase and remove stop words
stop_words = stopwords.words('english')
tokenized_word = [each_string.lower() for each_string in tokenized_word]
tokenized_word = [word for word in tokenized_word if word not in stop_words]
print(tokenized_word)

#plot freq dist of the words used to describe Romney
fdist = FreqDist(tokenized_word)
fdist.plot(30,cumulative=False)
plt.show()



#Cleaning, Tokenizing, and Analyzing data for Elizabeth Warren 2020
#getting data for Elizabeth Warren
def get_url (q, begin_date, end_date):
    url = ("https://api.nytimes.com/svc/search/v2/articlesearch.json?q="+q+"&facet_fields=source&facet=true&begin_date="+begin_date+"&end_date="+end_date+"&api-key=MRAJUxGvim9gZYw4sGZ0ZH9hAgLrAeDR")
    return url

r = requests.get(get_url("warren, elizabeth", "20190101", "20200301"))

r= r.json()['response']['docs']

#getting abstracts for the articles where Trump is mentioned in 2016
warren = ""

for i in r:
    warren += i['abstract']
    
warren


#TOKENIZING AND ANALYZING SENTENCES
tokenized_text=sent_tokenize(warren)
print(tokenized_text)


#CLEANING AND TOKENIZING WORDS
#getting rid of punctuation
warren = re.sub(r'[^(a-zA-Z)\s]','', warren)


#tokenize words
tokenized_word=word_tokenize(warren)


#make everything lowercase and remove stop words
stop_words = stopwords.words('english')
tokenized_word = [each_string.lower() for each_string in tokenized_word]
tokenized_word = [word for word in tokenized_word if word not in stop_words]
print(tokenized_word)

#plot freq dist of the words used to describe Romney
fdist = FreqDist(tokenized_word)
fdist.plot(30,cumulative=False)
plt.show()



#Cleaning, Tokenizing, and Analyzing data for Joe Biden 2020
#getting data for Joe Biden
def get_url (q, begin_date, end_date):
    url = ("https://api.nytimes.com/svc/search/v2/articlesearch.json?q="+q+"&facet_fields=source&facet=true&begin_date="+begin_date+"&end_date="+end_date+"&api-key=MRAJUxGvim9gZYw4sGZ0ZH9hAgLrAeDR")
    return url

r = requests.get(get_url("biden, joe", "20190101", "20200301"))

r= r.json()['response']['docs']

#getting abstracts for the articles where Trump is mentioned in 2016
biden = ""

for i in r:
    biden += i['abstract']
    
biden


#TOKENIZING AND ANALYZING SENTENCES
tokenized_text=sent_tokenize(biden)
print(tokenized_text)


#CLEANING AND TOKENIZING WORDS
#getting rid of punctuation
biden = re.sub(r'[^(a-zA-Z)\s]','', biden)


#tokenize words
tokenized_word=word_tokenize(biden)


#make everything lowercase and remove stop words
stop_words = stopwords.words('english')
tokenized_word = [each_string.lower() for each_string in tokenized_word]
tokenized_word = [word for word in tokenized_word if word not in stop_words]
print(tokenized_word)

#plot freq dist of the words used to describe Romney
fdist = FreqDist(tokenized_word)
fdist.plot(30,cumulative=False)
plt.show()
