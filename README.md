Dated: 28 October 2025
Product Documentation:

Problem: As a youtube premium user, I have using youtube music for a while now, and each time the recommended songs get played I realize they are out of mood/context. 
In the queue of Bhakti songs, romantic recently played songs get played, In the loop of romantic soft songs, hard core songs starts getting played.

Solution: A recommendation system that keeps adding songs to the playlist that matches the vibe of the song currently getting played.

v1.0.0
In this recommendation system, I have to give a song as input and as op the recommendation system give the top 5 most similar songs.
I’ve actually built a content-based recommendation system using text similarity (CountVectorizer + cosine similarity).

Issue1: Getting romantic songs recommended for Bhakti genre. In new hindi romantic songs getting 90's music recommended(Not preferrable)

The reason for this :
Here’s what’s going on inside my code:

creating  "tags" = Description + Channel + Genre.

Then using CountVectorizer to get word frequencies.

Cosine similarity is calculated on word counts only (no context or category understanding).

So if both bhakti and romantic songs share common words like "new", "songs", "love", "hits", "music", "trending", etc. — they will appear textually similar, even though they are from different genres.

v1.0.1

Fix: 
1. Filtered using genre, removed all the out of genre recommendations, Now for Bhakti songs-> getting Bhakti songs recommended
2. Using TF-IDF Vectorizer Instead of CountVectorizer, giving weightage to unique words, hence reducing the influence of generic words
3. Increased the weightage of Genre

Results:
Similar songs to 'Sabrina Carpenter - Espresso' in genre 'Pop':

Sabrina Carpenter - Manchild (Official Video)
Taylor Swift - The Fate of Ophelia (Official Music Video)
Lady Gaga, Bruno Mars - Die With A Smile (Official Music Video)
K-POP DEMON HUNTERS PLAYLIST OST
Tyla - IS IT (Official Music Video)

Issue2: Giving same song twice in recommendation, and still the 90's song is coming in latest songs vibe(Weird, Needs a fix!)
Similar songs to 'Best of ATIF ASLAM Songs | Bollywood Romantic Love Songs | Audio Jukebox | Hindi Hit Songs' in genre 'Romantic':

New Trending Love Songs | Hindi Romantic Songs Collection | New Hindi Love Songs #viral
Best Romantic Hindi Songs 2025 |  New Romantic Song | Bollywood Love Hits Jukebox
Vibes Of Love Mashup || Latest Bollywood Songs Jukebox 2025  || Romantic Jukebox Nonstop
90’S Old Hindi Songs🥰 90s Love Song💘 Udit Narayan, Alka Yagnik, Kumar Sanu, Sonu Nigam
90’S Old Hindi Songs🥰 90s Love Song💘 Udit Narayan, Alka Yagnik, Kumar Sanu, Sonu Nigam

Git push~



