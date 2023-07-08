import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]  # fetch the movie index
    distances = similarity[movie_index]
    movies_list =sorted(list(enumerate (distances)), reverse=True, key=lambda x: x[1])[1:6] # fetch the similar movie imdex

    recommend_movies = []
    for i in movies_list:
        recommend_movies.append(movies.iloc[i[0]].title)  # print the nameof the similar movie
    return recommend_movies

movies_dict  = pickle.load(open('movie_dict.pkl','rb'))
movies= pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System Project')

selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)

if st.button('Recommend'):
    recomendations=  recommend(selected_movie_name )
    for i in recomendations:
        st.write(i)
