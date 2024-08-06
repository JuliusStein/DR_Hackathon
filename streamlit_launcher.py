import streamlit as st
import pandas as pd
import numpy as np

st.text('DataRobot Summer Intern Hackathon 2024')
st.title("Generative Wrangler Operations")
st.write("**Julius Stein & Lucas Ferreira**")

col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    button1 = st.button('Button 1')
with col2:
    button2 = st.button('Button 2')
with col3:
    button3 = st.button('Button 3')
with col4:
    button4 = st.button('Button 4')
with col5:
    button5 = st.button('Button 5')
with col6:
    button6 = st.button('Button 6')

if button1:
    pass

if button2:
    pass

if button3:
    pass

if button4:
    pass

if button5:
    pass

if button6:
    pass

df = pd.read_csv('data/movieReviews/test_reviews.csv')
st.write(df)