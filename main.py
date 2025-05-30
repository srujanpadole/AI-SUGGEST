import pandas as pd
import streamlit as st

data = {
     "title": [
        "John Wick", "Naruto", "The Office", "Breaking Bad", "Attack on Titan",
        "Demon Slayer", "Stranger Things", "Money Heist", "Jujutsu Kaisen", "Vikings",
        "Peaky Blinders", "The Boys", "One Piece", "Death Note", "Dark",
        "Interstellar", "Inception", "Black Mirror", "The Witcher", "Sherlock",
        "The Mandalorian", "Chainsaw Man", "Narcos", "Rick and Morty", "The 100",
        "Bleach", "Tokyo Revengers", "The Crown", "Friends", "Better Call Saul",
        "Drive", "The Batman", "Tenet", "The Matrix", "Reacher",
        "Baki", "Vinland Saga", "My Hero Academia", "Spy x Family", "Code Geass",
        "Haikyuu", "Brooklyn Nine-Nine", "Gintama", "Squid Game", "Mob Psycho 100",
        "Solo Leveling", "Dragon Ball Z", "Avatar", "The Expanse", "The Flash",
        "Loki", "Black Panther", "WandaVision", "Stranger Things S2", "Naruto Shippuden",
        "Fullmetal Alchemist", "Death Parade", "The Queen's Gambit", "Chernobyl", "Better Call Saul S2",
        "The Boys S2", "Money Heist S2", "Demon Slayer S2", "Attack on Titan S4", "Jujutsu Kaisen S2",
        "Peaky Blinders S6", "The Witcher S2", "Squid Game S2", "Vikings: Valhalla", "The Mandalorian S2",
        "Narcos Mexico", "My Hero Academia S5", "Chainsaw Man S1", "Rick and Morty S6", "Bleach S2",
        "Gintama: The Final", "Tenet (Movie)", "Inception (Movie)", "Dark S3", "Black Mirror S6",
        "The Crown S4", "Friends Reunion", "Dragon Ball Super", "Spy x Family S2", "Haikyuu S4",
        "Brooklyn Nine-Nine S8", "Mob Psycho 100 S3", "Solo Leveling Webtoon", "Avatar The Last Airbender", "The Expanse S5",
        "The Flash S8", "Loki S2", "Black Panther 2", "WandaVision S2", "Fullmetal Alchemist Brotherhood",
        
    ],
    
    "type": [
        "movie", "anime", "webseries", "webseries", "anime",
        "anime", "webseries", "webseries", "anime", "webseries",
        "webseries", "webseries", "anime", "anime", "webseries",
        "movie", "movie", "webseries", "webseries", "webseries",
        "webseries", "anime", "webseries", "webseries", "webseries",
        "anime", "anime", "webseries", "webseries", "webseries",
        "movie", "movie", "movie", "movie", "webseries",
        "anime", "anime", "anime", "anime", "anime",
        "anime", "webseries", "anime", "webseries", "anime",
        "webseries", "movie", "movie", "webseries", "anime",
        "anime", "anime", "webseries", "webseries", "webseries",
        "webseries", "webseries", "webseries", "anime", "anime",
        "webseries", "webseries", "webseries", "webseries", "webseries",
        "webseries", "webseries", "webseries", "webseries", "webseries",
        "webseries", "webseries", "movie", "movie", "webseries",
        "webseries", "movie", "movie", "webseries", "webseries",
        "webseries", "webseries", "webseries", "webseries", "webseries",
        "webseries", "webseries", "webseries", "webseries", "webseries",
        "movie", "movie", "movie", "webseries", "movie",
      
    ],
    
    "genre": [
        "action", "action", "comedy", "drama", "action",
        "action", "thriller", "crime", "action", "history",
        "crime", "superhero", "adventure", "mystery", "sci-fi",
        "sci-fi", "sci-fi", "sci-fi", "fantasy", "detective",
        "sci-fi", "action", "crime", "comedy", "sci-fi",
        "action", "action", "drama", "comedy", "drama",
        "thriller", "action", "sci-fi", "sci-fi", "action",
        "fighting", "action", "superhero", "comedy", "strategy",
        "sports", "comedy", "comedy", "thriller", "psychological",
        "fantasy", "fighting", "adventure", "sci-fi", "superhero",
        "superhero", "action", "fantasy", "thriller", "drama",
        "drama", "crime", "action", "action", "action",
        "crime", "fantasy", "thriller", "fantasy", "action",
        "crime", "fantasy", "thriller", "action", "fantasy",
        "crime", "action", "action", "sci-fi", "sci-fi",
        "drama", "comedy", "fantasy", "comedy", "psychological",
        "fantasy", "adventure", "superhero", "fantasy", "sci-fi",
        "superhero", "superhero", "fantasy", "drama", "action",
        "drama", "action", "action", "sci-fi", "sci-fi"
    ],
    
    "platform": [
        "Netflix", "Crunchyroll", "Netflix", "Netflix", "Crunchyroll",
        "Netflix", "Netflix", "Netflix", "Crunchyroll", "Netflix",
        "Netflix", "Prime Video", "Netflix", "Netflix", "Netflix",
        "Prime Video", "Netflix", "Netflix", "Netflix", "Prime Video",
        "Disney+", "Crunchyroll", "Netflix", "Netflix", "Netflix",
        "Crunchyroll", "Disney+", "Netflix", "Netflix", "Netflix",
        "Netflix", "Prime Video", "Prime Video", "Netflix", "Prime Video",
        "Netflix", "Netflix", "Crunchyroll", "Crunchyroll", "Crunchyroll",
        "Netflix", "Netflix", "Crunchyroll", "Netflix", "Crunchyroll",
        "Disney+", "Netflix", "Netflix", "Netflix", "Crunchyroll",
        "Crunchyroll", "Crunchyroll", "Netflix", "Netflix", "Netflix",
        "Netflix", "Netflix", "Netflix", "Crunchyroll", "Crunchyroll",
        "Netflix", "Netflix", "Netflix", "Netflix", "Netflix",
        "Netflix", "Netflix", "Prime Video", "Prime Video", "Netflix",
        "Netflix", "Disney+", "Disney+", "Netflix", "Netflix",
        "Netflix", "Netflix", "Netflix", "Netflix", "Netflix",
        "Netflix", "Netflix", "Netflix", "Netflix", "Netflix",
        "Netflix", "Netflix", "Netflix", "Netflix", "Netflix",
        "Prime Video", "Prime Video", "Netflix", "Netflix", "Netflix"
    ]

}

print(len(data["title"]))
print(len(data["type"]))
print(len(data["genre"]))
print(len(data["platform"]))


df=pd.DataFrame(data)

st.set_page_config(page_title="AI content recommender by sruj",layout="wide")

st.title("🎬AI MOVIE/ANIME/ web searies recommender")
st.write("choose your vibe,and get real suggestion with where to watch them!")

genre = st.selectbox("🎯 choose genre",sorted(df["genre"].unique()))
content_type = st.selectbox("🎞️ choose type",["any"]+ sorted(df["type"].unique()))

filtered = df[df["genre"]==genre]
if content_type!= "any":
    filtered = filtered[filtered["type"]== content_type]

if not filtered.empty:
    st.subheader("📺 recommended for you:")
    for i, row in filtered.iterrows():
        st.markdown(f"""

                    🎬{row['title']}
                    📽️type:{row['type']}
                    🧠genre:{row['genre']}
                    📍platform:{row['platform']} 
                  """  )
else:
    st.warning("No result found.try a different combo.")

