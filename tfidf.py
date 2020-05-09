#tfidf
#pip install sklearn
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer()
x = tfidf.fit_transform(tokenized_text)

indices = np.argsort(tfidf.idf_)[::-1]
features = tfidf.get_feature_names()

top_features = [features[i] for i in indices[:5]]
print (top_features)

#tfs = tfidf.fit_transform(t.split(" "))
#str = 'tree cat travellers fruit jupiter'
#response = tfidf.transform([str])
#feature_names = tfidf.get_feature_names()

#for col in response.nonzero()[1]:
#    print(feature_names[col], ' - ', response[0, col])
