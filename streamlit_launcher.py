import streamlit as st
import pandas as pd
from generative_wrangling import summarize_message, rephrase_message, label_categories, encode_variables, translate_message, analyze_sentiment
global df, button, feature, length, tone, title, exclusive, category1, category2, category3, variable1, variable2, variable3, inputLang, outputLang, emotion1, emotion2, emotion3, quotes

if 'summarize' not in st.session_state:
    st.session_state.summarize = False
if 'rephrase' not in st.session_state:
    st.session_state.rephrase = False
if 'categorize' not in st.session_state:
    st.session_state.categorize = False
if 'variable' not in st.session_state:
    st.session_state.variable = False
if 'translate' not in st.session_state:
    st.session_state.translate = False
if 'sentiment' not in st.session_state:
    st.session_state.sentiment = False

def display_subfields_summarize():
    st.session_state.summarize = True
    st.session_state.rephrase = False
    st.session_state.categorize = False
    st.session_state.variable = False
    st.session_state.translate = False
    st.session_state.sentiment = False

def display_subfields_rephrase():
    st.session_state.summarize = False
    st.session_state.rephrase = True
    st.session_state.categorize = False
    st.session_state.variable = False
    st.session_state.translate = False
    st.session_state.sentiment = False

def display_subfields_categorize():
    st.session_state.summarize = False
    st.session_state.rephrase = False
    st.session_state.categorize = True
    st.session_state.variable = False
    st.session_state.translate = False
    st.session_state.sentiment = False

def display_subfields_variable():
    st.session_state.summarize = False
    st.session_state.rephrase = False
    st.session_state.categorize = False
    st.session_state.variable = True
    st.session_state.translate = False
    st.session_state.sentiment = False

def display_subfields_translate():
    st.session_state.summarize = False
    st.session_state.rephrase = False
    st.session_state.categorize = False
    st.session_state.variable = False
    st.session_state.translate = True
    st.session_state.sentiment = False

def display_subfields_sentiment():
    st.session_state.summarize = False
    st.session_state.rephrase = False
    st.session_state.categorize = False
    st.session_state.variable = False
    st.session_state.translate = False
    st.session_state.sentiment = True

st.set_page_config(layout="wide")
st.text("Intern Hackathon - Summer 2024 - Julius Stein & Lucas Ferreira")
st.image('images/datarobot_logo.png', width=320)
st.subheader("Generative Wrangler Operations")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    feature = df.columns[0]

col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    summarize_button = st.button('Summarize Text', on_click=display_subfields_summarize)
with col2:
    rephrase_button = st.button('Rephrase Text', on_click=display_subfields_rephrase)
with col3:
    categorize_button = st.button('Label Categories', on_click=display_subfields_categorize)
with col4:
    variable_button = st.button('Encode Variables', on_click=display_subfields_variable)
with col5:
    translate_button = st.button('Translate Text', on_click=display_subfields_translate)
with col6:
    sentiment_button = st.button('Analyze Sentiment', on_click=display_subfields_sentiment)

#df = pd.read_csv('data/movieReviews/test_reviews.csv')
#df = pd.read_csv('data/jira_bugs/jira_bugs.csv')
#quotes = list(df['Description'])

if st.session_state.summarize:
    feature = st.text_input("Input Feature Name", df.columns[0])
    length = st.number_input("Max Tokens", 10, 100, 30)
    title = st.text_input("New Feature Name", "new_feature")
    add_summarize_operation = st.button("Add Operation")
elif st.session_state.rephrase:
    feature = st.text_input("Input Feature Name", df.columns[0])
    length = st.number_input("Max Tokens", 10, 100, 30)
    tone = st.selectbox("Tone", ['friendly', 'professional', 'sarcastic'])
    title = st.text_input("New Feature Name")
    add_rephrase_operation = st.button("Add Operation")
elif st.session_state.categorize:
    feature = st.text_input("Input Feature Name", df.columns[0])
    inner1, inner2, inner3 = st.columns(3)
    with inner1:
        category1 = st.text_input("Category 1")
    with inner2:
        category2 = st.text_input("Category 2")
    with inner3:
        category3 = st.text_input("Category 3")
    exclusive = st.checkbox("Exclusive")
    title = st.text_input("New Feature Name", "new_feature")
    add_categorize_operation = st.button("Add Operation")
elif st.session_state.variable:
    feature = st.text_input("Input Feature Name", df.columns[0])
    inner1, inner2, inner3 = st.columns(3)
    with inner1:
        variable1 = st.text_input("Variable 1")
    with inner2:
        variable2 = st.text_input("Variable 2")
    with inner3:
        variable3 = st.text_input("Variable 3")
    title = st.text_input("New Feature Name", "new_feature")
    add_variable_operation = st.button("Add Operation")
elif st.session_state.translate:
    feature = st.text_input("Input Feature Name", df.columns[0])
    outputLang = st.text_input("Output Language")
    title = st.text_input("New Feature Name", "new_feature")
    add_translate_operation = st.button("Add Operation")
elif st.session_state.sentiment:
    feature = st.text_input("Input Feature Name", df.columns[0])
    inner1, inner2, inner3 = st.columns(3)
    with inner1:
        emotion1 = st.text_input("Emotion 1")
    with inner2:
        emotion2 = st.text_input("Emotion 2")
    with inner3:
        emotion3 = st.text_input("Emotion 3")
    title = st.text_input("New Feature Name", "new_feature")
    add_sentiment_operation = st.button("Add Operation")

if uploaded_file is not None:
    quotes = list(df[feature])

if st.session_state.summarize:
    if add_summarize_operation:
        new_quotes = []
        for quote in quotes:
            new_quotes.append(summarize_message(quote, length))
        df[title] = new_quotes
        st.session_state.summarize = False
elif st.session_state.rephrase:
    if add_rephrase_operation:
        new_quotes = []
        for quote in quotes:
            new_quotes.append(rephrase_message(quote, tone, length))
        df[title] = new_quotes
        st.session_state.rephrase = False
elif st.session_state.categorize:
    if add_categorize_operation:
        new_quotes = []
        for quote in quotes:
            new_quotes.append(label_categories(quote, [category1, category2, category3], exclusive))
        df[title] = new_quotes
        st.session_state.categorize = False
elif st.session_state.variable:
    if add_variable_operation:
        new_quotes = []
        for quote in quotes:
            new_quotes.append(encode_variables(quote, [variable1, variable2, variable3]))
        df[title] = new_quotes
        st.session_state.variable = False
elif st.session_state.translate:
    if add_translate_operation:
        new_quotes = []
        for quote in quotes:
            new_quotes.append(translate_message(quote, outputLang))
        df[title] = new_quotes
        st.session_state.translate = False
elif st.session_state.sentiment:
    if add_sentiment_operation:
        new_quotes = []
        for quote in quotes:
            new_quotes.append(analyze_sentiment(quote, [emotion1, emotion2, emotion3]))
        df[title] = new_quotes
        st.session_state.sentiment = False

if uploaded_file is not None:
    st.dataframe(df)