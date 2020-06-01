import pandas as pd
import matplotlib.pyplot as plt
from gensim.models import LdaModel
import re
from gensim import corpora
import numpy as np
from textblob import TextBlob

from sklearn.cluster import KMeans

dates = ["5-14-2020"]
df = pd.read_csv("../tweets/%s.csv" % dates[0])
english_df = df[df['lang'] == 'en']
shortened_df = english_df.iloc[0:5000, :]
tweets = english_df.iloc[0:5000, 1].values
print(tweets.shape)
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

def cleanTweets(tweets):
    text_data = []
    for i in range(0, tweets.size):
        text = re.sub(r'@[A-Za-z0-9]+', '', tweets[i])
        text = re.sub('RT', '', text)
        text = text.replace("\r", "")
        text = text.replace("\n", "")
        text = re.sub('fuck[a-zA-Z0-9]', ' ', text)
        text = re.sub('fucking', ' ', text)
        text = re.sub('fuckign', ' ', text)
        text = re.sub('bitch', ' ', text)
        text = re.sub('ufe', ' ', text)
        text = re.sub('https?://[A-Za-z0-9./]+', '', text)
        text = re.sub('[^a-zA-Z]', ' ', text)
        text = text.lower()
        text = re.sub('covid', ' ', text)
        text = re.sub('coronavirus', ' ', text)
        text = text.split()
        ps = PorterStemmer()
        wnl = WordNetLemmatizer()
        text = [word for word in text if len(word) > 4]
        text = [wnl.lemmatize(word) for word in text if not word in set(stopwords.words('english'))]
        text_data.append(text)
    return text_data

def getTweetSentiment(text_data):
    tweet_sentiment_list = []
    for i in range(len(text_data)):
        analysis = TextBlob(" ".join(text_data[i]))
        tweet_sentiment_list.append(int(analysis.sentiment.polarity > 0))
    return tweet_sentiment_list


def prepareTweetsForLDA(text_data):
    dictionary = corpora.Dictionary(text_data)
    corpus = [dictionary.doc2bow(t) for t in text_data]
    return dictionary, corpus

cleaned_data = cleanTweets(tweets)
dictionary, corpus = prepareTweetsForLDA(cleaned_data)
sentiment_list = getTweetSentiment(cleaned_data)
print(len(sentiment_list))
shortened_df['sentiment'] =  sentiment_list
pos_tweets_df = shortened_df[shortened_df['sentiment']==1]
num_pos_tweets = pos_tweets_df.shape[0]
neg_tweets_df = shortened_df[shortened_df['sentiment']==0]
num_neg_tweets = neg_tweets_df.shape[0]
sentiment_tweets = [num_pos_tweets, num_neg_tweets]
labels = ("Positive Sentiment", "Negative Sentiment")
plt.pie(sentiment_tweets, labels=labels, colors = ['green', 'red'], autopct='%1.1f%%', shadow=True,startangle=140)
plt.axis('equal')
plt.title("%s Sentiment" % dates[0])
plt.savefig("../images/%sSentiment.png" % dates[0])



import gensim
NUM_TOPICS=1

ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = NUM_TOPICS, id2word=dictionary, passes=15)
topics = ldamodel.print_topics()

for topic in topics:
    print(topic)
from wordcloud import WordCloud, STOPWORDS
for t in range(len(topics)):
    plt.figure()
    plt.imshow(WordCloud().fit_words(dict(ldamodel.show_topic(t, 200))))
    plt.title(dates[0])
    plt.savefig("../images/" + dates[0] + ".png")




