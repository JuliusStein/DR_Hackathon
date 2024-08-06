import streamlit as st
import pandas as pd


st.text('DataRobot Summer Intern Hackathon 2024')
st.write("**Generative Wrangler Operations**")

df = pd.read_csv('data/movieReviews/critic_reviews.csv')
st.write(df)
