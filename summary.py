import streamlit as st
import requests
import time
from newspaper import Article


st.title("📰 Newspaper Article Summarizer")
st.markdown(
    """
    <style>
    /* Button style */
    .stButton>button {
        background-color: #ff7e5f;  /* Button background */
        color: white;               /* Button text color */
        border-radius: 10px;        /* Rounded corners */
        padding: 0.5em 1em;         /* Padding */
        border: none;               /* Remove default border */
    }
    .stButton>button:hover {
        background-color: #feb47b;  /* Hover background color */
        color: #333;                /* Hover text color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("News article summarization is crucial in today’s fast-paced information environment, where readers are often overwhelmed by the sheer volume of content available. By distilling lengthy articles into concise summaries, it allows individuals to quickly grasp the main ideas and key facts without having to read the full text. This is particularly important for busy professionals and students who need to stay informed but have limited time. Moreover, effective summarization can enhance understanding and retention of information, helping readers to engage more deeply with the news while promoting better decision-making based on accurate insights.")
st.markdown("<hr>", unsafe_allow_html=True)

# Inputs 
st.subheader(" 🔗 Article URL")
default_url = "https://"
url = st.text_input("URL:", default_url)

headers_ = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

fetch_button = st.button("Fetch article")

if fetch_button:
    article_url = url
    session = requests.Session()

    try:
        response_ = session.get(article_url, headers=headers_, timeout=10)
    
        if response_.status_code == 200:
            with st.spinner('Fetching your article...'):
                time.sleep(3)
                st.success('Your article is ready for summarization!')
        else:
            st.write("Error occurred while fetching article.")
    except Exception as e:
        st.write(f"Error occurred while fetching article: {e}")

# HuggingFace API KEY input
st.subheader(" 🔐 API Key")
API_KEY = st.text_input("Enter your HuggingFace API key", type="password")

# HuggingFace API inference URL
API_URL = "https://api-inference.huggingface.co/models/google/pegasus-cnn_dailymail"
headers = {"Authorization": f"Bearer {API_KEY}"}

submit_button = st.button("Get Summary")

if submit_button:
    article = Article(url)
    article.download()
    article.parse()

    title = article.title
    text = article.text

    # HuggingFace API request function
    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
    
    with st.spinner('Doing some AI magic, please wait...'):
        time.sleep(1)
        output = query({"inputs": text, "parameters": {"truncation": "only_first"}})
        summary = output[0]["summary_text"].replace("<n>", " ")
        
        st.divider()
        st.subheader("Summary")
        st.write(f"Your article: **{title}**")
        st.write(f"**{summary}**")