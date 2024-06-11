import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    movie_index = movies[movies ['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:10]




    # its givings us top 5 similar movies
    recommended_movies = []
    for i in movies_list:
         recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

def disrec(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), key=lambda x: x[1])[1:10]

    #its gonna give top 5 dissimalrity movies
    dis_recommended_movies = []
    for i in movies_list:
            dis_recommended_movies.append(movies.iloc[i[0]].title)
    return dis_recommended_movies


movie_load = pickle.load(open('/Users/raunitsingh.vc/ML Projects/GIT/Coffeee-BootCamp-Projects/Netflix Movie Recommender/recommender_model.pkl', 'rb'))
movies = pd.DataFrame(movie_load)

similarity = pickle.load(open('/Users/raunitsingh.vc/ML Projects/GIT/Coffeee-BootCamp-Projects/Netflix Movie Recommender/similarity.pkl', 'rb'))



st.title("Netflix Movie Recommending/Discommend Model")

st.header('To check for similar movies')

selected_movies_name = st.selectbox(

"Here are the list of movies, Select your movie :", movies['title'].values
)

if st.button('Recommend'):
    recommendations =  recommend((selected_movies_name))
    for i in recommendations:
        st.write(i)


st.header("To check for Dissimilar movies :")

selected_movies_name = st.selectbox(

"Here are the list of movies, Select one :", movies['title'].values
)


if st.button('Discommend'):
    dis_recommendations = disrec((selected_movies_name))
    for i in dis_recommendations:
        st.write(i)
