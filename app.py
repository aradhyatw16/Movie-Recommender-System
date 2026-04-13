import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster_and_rating(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={st.secrets["API_KEY"]}&language=en-US')
    data = response.json()
    poster_path = data.get('poster_path')
    rating = round(data.get('vote_average', 0), 1)
    if poster_path:
        poster = "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        poster = "https://placehold.co/500x750?text=No+Poster"
    return poster, rating
    
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_posters = []
    recommended_movies_ratings = []
    recommended_movies_ids = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        poster, rating = fetch_poster_and_rating(movie_id)
        recommended_movies_posters.append(poster)
        recommended_movies_ratings.append(rating)
        recommended_movies_ids.append(movie_id)
    
    return recommended_movies, recommended_movies_posters, recommended_movies_ratings, recommended_movies_ids

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')
st.write("Select a movie and get 5 similar movie recommendations!")

selected_movie_name = st.selectbox(
    'Select a Movie',
    movies['title'].values
)


if st.button('Recommend'):
    with st.spinner('Fetching recommendations...'):
        names, posters, ratings, ids = recommend(selected_movie_name)
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(names[0])
            st.image(posters[0])
            st.write(f"⭐ {ratings[0]}/10")
            st.markdown(f"[More Info](https://www.themoviedb.org/movie/{ids[0]})")
        with col2:
            st.text(names[1])
            st.image(posters[1])
            st.write(f"⭐ {ratings[1]}/10")
            st.markdown(f"[More Info](https://www.themoviedb.org/movie/{ids[1]})")
        with col3:
            st.text(names[2])
            st.image(posters[2])
            st.write(f"⭐ {ratings[2]}/10")
            st.markdown(f"[More Info](https://www.themoviedb.org/movie/{ids[2]})")
        with col4:
            st.text(names[3])
            st.image(posters[3])
            st.write(f"⭐ {ratings[3]}/10")
            st.markdown(f"[More Info](https://www.themoviedb.org/movie/{ids[3]})")
        with col5:
            st.text(names[4])
            st.image(posters[4])
            st.write(f"⭐ {ratings[4]}/10")
            st.markdown(f"[More Info](https://www.themoviedb.org/movie/{ids[4]})")
