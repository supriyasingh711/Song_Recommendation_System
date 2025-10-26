from googleapiclient.discovery import build
import pandas as pd

# ----------------- CONFIG -----------------
API_KEY = "AIzaSyAONMfgBBK0pyfVqAsVwMr6fiNCvG5LNsU"  # replace with your API key
youtube = build('youtube', 'v3', developerKey=API_KEY)


# ----------------- FUNCTION -----------------
def get_youtube_videos(query, max_results=20):
    request = youtube.search().list(
        q=query,
        part="snippet",
        type="video",
        maxResults=max_results
    )
    response = request.execute()

    videos = []
    for item in response['items']:
        video_data = {
            'Title': item['snippet']['title'],
            'Description': item['snippet']['description'],
            'Channel': item['snippet']['channelTitle']
        }
        videos.append(video_data)

    return pd.DataFrame(videos)


# ----------------- FETCH GENRES -----------------
def fetch_all_genres():
    bhakti_df = get_youtube_videos("bhakti songs", 30)
    bhakti_df["Genre"] = "Bhakti"

    romantic_df = get_youtube_videos("romantic songs", 30)
    romantic_df["Genre"] = "Romantic"

    pop_df = get_youtube_videos("pop songs", 30)
    pop_df["Genre"] = "Pop"

    lofi_df = get_youtube_videos("lofi chill beats", 30)
    lofi_df["Genre"] = "Lofi"

    final_df = pd.concat([bhakti_df, romantic_df, pop_df, lofi_df], ignore_index=True)
    return final_df


# ----------------- SAVE CSV -----------------
if __name__ == "__main__":
    df = fetch_all_genres()
    df.to_csv("youtube_songs.csv", index=False)
    print("youtube_songs.csv generated successfully!")
    print(df.head())
