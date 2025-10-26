import pandas as pd
import re
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

lemmatizer = WordNetLemmatizer()
#stop_words = set(stopwords.words('english')
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', str(text))
    text = text.lower()
    tokens = text.split()
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return ' '.join(tokens)

# ---------- Load and Prepare ----------
def prepare_data(path="youtube_songs.csv"):
    df = pd.read_csv(path)
    df['CleanText'] = (df['Title'] + " " + df['Description']).apply(clean_text)

    vectorizer = TfidfVectorizer(max_features=5000)
    tfidf_matrix = vectorizer.fit_transform(df['CleanText'])
    similarity_matrix = cosine_similarity(tfidf_matrix)

    return df, similarity_matrix

# ---------- Recommend ----------
def recommend(title, genre, df, similarity_matrix, n=5):
    title = title.strip().lower()
    df['Title_lower'] = df['Title'].str.lower().str.strip()
    if title not in df['Title_lower'].values:
        return []

    idx = df[df['Title_lower'] == title].index[0]
    scores = list(enumerate(similarity_matrix[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    recs = []
    print(df[['Title', 'Genre', 'CleanText']].head(10))
    for i, s in scores:
        if df.loc[i, 'Genre'] == genre and df.loc[i, 'Title'] != title:
            recs.append({
                "title": df.loc[i, 'Title'],
                "description": df.loc[i, 'Description'],
                "genre": df.loc[i, 'Genre'],
                "score": round(float(s), 3)
            })
        if len(recs) >= n:
            break

    return recs
