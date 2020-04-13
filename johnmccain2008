#Cleaning, tokenizingm, and analyzing data for John McCain in 2008
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

#getting data for john mccain 2008
def get_url (q, begin_date, end_date):
    url = ("https://api.nytimes.com/svc/search/v2/articlesearch.json?q="+q+"&facet_fields=source&facet=true&begin_date="+begin_date+"&end_date="+end_date+"&api-key=MRAJUxGvim9gZYw4sGZ0ZH9hAgLrAeDR")
    return url

r = requests.get(get_url("mccain, john", "20080101", "20081231"))

r= r.json()['response']['docs']

#getting abstracts for the articles where Mccain is mentioned in 2008
mccain08 = ""

for i in r:
    mccain08 += i['abstract']
    
mccain08


#TOKENIZING AND ANALYZING SENTENCES
tokenized_text=sent_tokenize(mccain08)
print(tokenized_text)


#CLEANING AND TOKENIZING WORDS
#getting rid of punctuation
mccain08 = re.sub(r'[^(a-zA-Z)\s]','', mccain08)


#tokenize words
tokenized_word=word_tokenize(mccain08)


#make everything lowercase and remove stop words
stop_words = stopwords.words('english')
tokenized_word = [each_string.lower() for each_string in tokenized_word]
tokenized_word = [word for word in tokenized_word if word not in stop_words]


#plot freq dist of the words used to describe Romney
fdist = FreqDist(tokenized_word)
fdist.plot(30,cumulative=False)
plt.show()
