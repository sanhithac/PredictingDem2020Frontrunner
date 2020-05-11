from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelBinarizer
from sklearn import metrics
from sklearn.model_selection import train_test_split 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('train.csv')

#preprocessing
lb = LabelBinarizer()
data = dataset[['Education', 'Religion', 'Ethnicity', 'Occupation', 'Party']]
enc = pd.get_dummies(data)
result = pd.concat([dataset['Name'], dataset['Age'], enc, dataset.iloc[:,7:]], axis = 1)

#splitting into test, train, and validate sets
res = result.fillna(method='ffill')
li=list(res.columns)
train = res[:-2]
validate = res[22:]

X = train[li[1:-2]].values
V = validate [li[1:-2]].values
y = train['Won'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#fitting our model
regressor = LogisticRegression()  
regressor.fit(X_train, y_train)

#testing
y_pred = regressor.predict(X_test)

df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})

accuracy = accuracy_score(y_test ,y_pred)

print("Accuracy: ")
print(accuracy)

v_pred = regressor.predict(V)

df = pd.DataFrame({'Predicted': v_pred})
df
