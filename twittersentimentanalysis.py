#trump tweet sentiment analysis https://www.kaggle.com/ritzdevp/sentiment-analysis-using-nltk
trump = pd.read_csv("trump.csv") 
trump.head()
data_df2 = pd.DataFrame(trump)
data_df2

#data_df2.head()

all_trump = data_df2['tweet']
all_sent_values2 = []
all_sentiments2 = []

for i in range(0,3789):
    all_sent_values2.append(sentiment_value(all_trump[i]))
    
all_sent_values2

#biden tweet sentiment analysis
biden = pd.read_csv("biden.csv") 
biden.head()
data_df = pd.DataFrame(biden)
data_df
all_biden = data_df['tweet']
all_sent_values = []
all_sentiments = []
for i in range(0,823):
    all_sent_values.append(sentiment_value(all_biden[i]))
all_sent_values
