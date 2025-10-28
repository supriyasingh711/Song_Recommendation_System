import numpy as np
import pandas as pd
import nltk
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

songs=pd.read_csv('youtube_songs.csv')
#print(songs.head()['Title'].values)
#to apply tags on single channel uniquely removing from the spaces in between names
songs['Channel'] = songs['Channel'].astype(str).str.replace(" ", "", regex=False)


#print(songs['Channel'])
songs['tags']=songs['Description']+" "+songs['Channel']+" "+songs['Genre']*3

new_df=songs[['Title','tags']]
new_df['tags']=new_df['tags'].apply(lambda x:x.lower())



print(new_df['tags'][0])
#calculate similarity

cv = TfidfVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(new_df['tags']).toarray()


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
    song_genre = songs.iloc[song_index]['Genre']  # get genre of input song
    distances=similarity[song_index]
    song_list=sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:]

    print(f"\nSimilar songs to '{song}' in genre '{song_genre}':\n")
    count = 0
    for i in song_list:
        if songs.iloc[i[0]]['Genre'] == song_genre:  # filter by same genre
            print(new_df.iloc[i[0]]['Title'])
            count += 1
        if count == 5:
            break
recommend('Best of ATIF ASLAM Songs | Bollywood Romantic Love Songs | Audio Jukebox | Hindi Hit Songs')








