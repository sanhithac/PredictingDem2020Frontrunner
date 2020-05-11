#Biden Twitter POS Tagging
from nltk import word_tokenize, pos_tag

data = ' '.join(data_df['tweet'].tolist())
#data

#TOKENIZING AND ANALYZING SENTENCES
tokenized_text=sent_tokenize(data)
#print(tokenized_text)


#CLEANING AND TOKENIZING WORDS
#getting rid of punctuation
data = re.sub(r'[^(a-zA-Z)\s]','', data)


#tokenize words
tokenized_word=word_tokenize(data)


#make everything lowercase and remove stop words
stop_words = stopwords.words('english')
tokenized_word = [each_string.lower() for each_string in tokenized_word]
tokenized_word = [word for word in tokenized_word if word not in stop_words]


#POS Tagging
pos = nltk.pos_tag(tokenized_word)
#pos

#print([s for s in pos if s[1] == 'JJ'])
