from fastapi import FastAPI, Query
from recommender import prepare_data, recommend

app = FastAPI(title="GenreGuard Recommender API 🎵")

# Load data & precompute similarity matrix on startup
df, similarity_matrix = prepare_data()

@app.get("/")
def root():
    return {"message": "Welcome to GenreGuard Recommender API 🎶"}

@app.get("/recommend")
def get_recommendations(
    title: str = Query(..., description="Song title to base recommendations on"),
    genre: str = Query(..., description="Genre to filter recommendations by")
):
    recs = recommend(title, genre, df, similarity_matrix)
    if not recs:
        return {"message": f"No similar songs found for '{title}' in genre '{genre}'."}
    return recs
