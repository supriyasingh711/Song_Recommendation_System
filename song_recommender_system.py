import numpy as np
import pandas as pd
import nltk
from nltk.stem.porter import PorterStemmer

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

songs=pd.read_csv('youtube_songs.csv')
#print(songs.head()['Title'].values)
#to apply tags on single channel uniquely removing from the spaces in between names
songs['Channel'] = songs['Channel'].astype(str).str.replace(" ", "", regex=False)


#print(songs['Channel'])
songs['tags']=songs['Description']+" "+songs['Channel']+" "+songs['Genre']

new_df=songs[['Title','tags']]
new_df['tags']=new_df['tags'].apply(lambda x:x.lower())



print(new_df['tags'][0])
#calculate similarity

cv=CountVectorizer(max_features=5000,stop_words='english')

vectors=cv.fit_transform(new_df['tags']).toarray()

#print()

ps=PorterStemmer()
def stem(text):
    y=[]
    for i in text.split():
        ps.stem(i)
        y.append(ps.stem(i))
    return " ".join(y)

new_df['tags']=new_df['tags'].apply(stem)

#calculate cosine similarity between two songs

similarity=cosine_similarity(vectors)

#print(cosine_similarity(vectors).shape)

def recommend(song):
    song_index=new_df[new_df['Title']==song].index[0]
    distances=similarity[song_index]
    song_list=sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    for i in song_list:
        print(new_df.iloc[i[0]])

recommend('New Trending Love Songs | Hindi Romantic Songs Collection | New Hindi Love Songs #viral')








