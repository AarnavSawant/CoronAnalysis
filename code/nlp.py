import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
from mpl_toolkits import mplot3d
import nltk
from sklearn.cluster import KMeans
df = pd.read_csv("../tweets/2020-03-30.csv")
english_df = df[df['lang'] == 'en']
tweets = english_df.iloc[:, 4].values
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
corpus = []
for i in range(0, 1000):
    text = re.sub(r'@[A-Za-z0-9]+', '', tweets[i])
    text = re.sub('RT', '', text)
    text = text.replace("\r", "")
    text = text.replace("\n", "")
    text = re.sub('fuck[a-zA-Z0-9]', ' ', text)
    text = re.sub('fucking', ' ', text)
    text = re.sub('fuckign', ' ', text)
    text = re.sub('https?://[A-Za-z0-9./]+','', text)
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower()
    text = re.sub('covid', ' ', text)
    text = re.sub('coronavirus', ' ', text)
    text = text.split()
    wnl = WordNetLemmatizer()
    text = [wnl.lemmatize(word) for word in text if not word in set(stopwords.words('english'))]
    text = ' '.join(text)
    if text != ' ':
        corpus.append(text)

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer()
X = tfidf.fit_transform(corpus).toarray()
feature_names = tfidf.get_feature_names()

from sklearn.decomposition import NMF
nmf = NMF(n_components=5, random_state=0, alpha=.1, l1_ratio=.5, init='nndsvd')
nmf.fit(X)
first_topic = nmf.components_[0]
second_topic = nmf.components_[1]
third_topic = nmf.components_[2]
fourth_topic = nmf.components_[3]
fifth_topic = nmf.components_[4]
first_topic_words = [feature_names[i] for i in first_topic.argsort()[-20:]]
second_topic_words = [feature_names[i] for i in second_topic.argsort()[-20:]]
third_topic_words = [feature_names[i] for i in third_topic.argsort()[-20:]]
fourth_topic_words = [feature_names[i] for i in fourth_topic.argsort()[-20:]]
fifth_topic_words = [feature_names[i] for i in fifth_topic.argsort()[-20:]]

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=5)
y_predict = kmeans.fit_predict(X)



# Applying Principal Component Analysis
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)


from wordcloud import WordCloud, STOPWORDS
import matplotlib.colors as mcolors

fig, ax = plt.subplots(3, 2)
cols = [color for name, color in mcolors.TABLEAU_COLORS.items()]
firstcloud = WordCloud(background_color='black', width=2500, height=1800, max_words=50).generate(" ".join(first_topic_words))
secondcloud = WordCloud(background_color='black', width=2500, height=1800, max_words=20).generate(" ".join(second_topic_words))
thirdcloud = WordCloud(background_color='black', width=2500, height=1800, max_words=20).generate(" ".join(third_topic_words))
fourthcloud = WordCloud(background_color='black', width=2500, height=1800, max_words=20).generate(" ".join(fourth_topic_words))
fifthcloud = WordCloud(background_color='black', width=2500, height=1800, max_words=20).generate(" ".join(fifth_topic_words))
plt.imshow(firstcloud)
ax[0, 1].imshow(secondcloud)
ax[1, 0].imshow(thirdcloud)
ax[1, 1].imshow(fourthcloud)
ax[2, 0].imshow(fifthcloud)
ax[0, 0].scatter(X_reduced[:, 0], X_reduced[:, 1], c=kmeans.predict(X))
plt.show()