import streamlit as st
import pickle
import pandas as pd
import requests          # to fetch url 

# creating function to fetch poster of all movies 
def fetch_poster(movie_id):
    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=eb63f223dbc81a37791f28261644a590&language=en.US".format(movie_id))
    data=response.json()                                             # response in in json file
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


# created function for movies recommendations as i did in jupiter notebook
def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movies=[]         # insert movies name by fetching through loop 
    recommended_movies_poster=[]  # insert movies poster 
    for i in movie_list:
        movie_id=movies.iloc[i[0]]['movie_id']                 # giving movies id to fetch poster
        recommended_movies.append((movies.iloc[i[0]].title))    # movies name column (title)
        recommended_movies_poster.append(fetch_poster(movie_id))  # to fetch poster id came in movie_id passed here as parameter
    return recommended_movies, recommended_movies_poster

# open the file in readbinary and load  converts it python object
movie_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)

# how similar another movie to this movies 
similarity=pickle.load(open('similarity.pkl','rb'))

# title of movie recommendation system
st.title("Movie Recommendation  System")

# select movies from dropdown  
selected_movie_name=st.selectbox("Enter the name of a movie",movies['title'].values)

# recommend button action 
if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)
    
    
    col1,col2,col3,col4,col5=st.columns(5)
    
    with col1:
        st.text(names[0])
        st.image(posters[0])
        
    with col2:
        st.text(names[1])
        st.image(posters[1])
    
    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

