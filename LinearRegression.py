from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelBinarizer
from sklearn import metrics
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression

#one hot encoding
lb = LabelBinarizer()
data = dataset[['Education', 'Religion', 'Ethnicity', 'Occupation', 'Party']]
enc = pd.get_dummies(data)
result = pd.concat([dataset['Name'], dataset['Age'], enc, dataset.iloc[:,7:]], axis = 1)

#splitting into train and test
res = result.fillna(method='ffill')
li=list(res.columns)
train = res[:-2]
validate = res[22:]

X = train[li[1:-2]].values
V = validate [li[1:-2]].values
y = train['Won'].values

#fitting the model and testing
regressor = LinearRegression()  
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})

#checking accuracy
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

#checking who wins
v_pred = regressor.predict(V)

df = pd.DataFrame({'Predicted': v_pred})
df
