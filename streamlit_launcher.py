import streamlit as st
import pandas as pd
import numpy as np
from generative_wrangling import summarize_text, rephrase_text, categorize_text, encode_variables, translate_text, analyze_sentiment

st.set_page_config(layout="wide")
st.text("Intern Hackathon - Summer 2024 - Julius Stein & Lucas Ferreira")
st.image('images/datarobot_logo.png', width=320)
st.subheader("Generative Wrangler Operations")

col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    summarize_button = st.button('Summarize Text')
with col2:
    rephrase_button = st.button('Rephrase Text')
with col3:
    categorize_button = st.button('Label Categories')
with col4:
    variable_button = st.button('Encode Variables')
with col5:
    translate_button = st.button('Translate Text')
with col6:
    sentiment_button = st.button('Analyze Sentiment')

df = pd.read_csv('data/movieReviews/test_reviews.csv')
quotes = list(df['quote'])
new_quotes = []

if summarize_button:
    for quote in quotes:
        new_quotes.append(summarize_text(quote, 30))
    df['summary'] = new_quotes

if rephrase_button:
    for quote in quotes:
        new_quotes.append(rephrase_text(quote, 'friendly', 30))
    df['rephrased'] = new_quotes

if categorize_button:
    for quote in quotes:
        new_quotes.append(categorize_text(quote, ['positive', 'negative'], True))
    df['categories'] = new_quotes

if variable_button:
    for quote in quotes:
        new_quotes.append(encode_variables(quote, ['movie', 'actor', 'director']))
    df['variable_encodings'] = new_quotes

if translate_button:
    for quote in quotes:
        new_quotes.append(translate_text(quote, 'en', 'es'))
    df['translated_en_es'] = new_quotes

if sentiment_button:
    for quote in quotes:
        new_quotes.append(analyze_sentiment(quote, ['happy', 'sad', 'angry', 'neutral']))
    df['sentiment_analysis'] = new_quotes

st.dataframe(df)