import streamlit as st
import json
import requests
import time
from newspaper import Article
from textblob import TextBlob
import pandas as pd
from datetime import datetime

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

# Initialize session state for article history
if 'article_history' not in st.session_state:
    st.session_state.article_history = []


def save_to_history(url, title, summary, sentiment=None):
    """Save article analysis to history"""
    st.session_state.article_history.append({
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'url': url,
        'title': title,
        'summary': summary,
        'sentiment': sentiment
    })

def get_sentiment(text):
    """Analyze sentiment of text"""
    analysis = TextBlob(text)
    # Get polarity score (-1 to 1)
    polarity = analysis.sentiment.polarity
    
    # Convert score to category
    if polarity > 0.1:
        return 'Positive', polarity
    elif polarity < -0.1:
        return 'Negative', polarity
    else:
        return 'Neutral', polarity

st.title("😊 Sentiment Analysis")
st.markdown("""Sentiment analysis of newspaper articles plays a vital role in interpreting public sentiment 
            and societal trends reflected in the media. By analyzing the emotional tone of news coverage,
            researchers and organizations can gauge how different events, policies, or social issues are 
            perceived by the public. This understanding can help journalists, editors, and policymakers identify 
            biases, assess the impact of coverage on public opinion, and respond appropriately to emerging narratives.""")
st.markdown("<hr>", unsafe_allow_html=True)


url = st.text_input("Enter article URL:", "https://")

if st.button("Analyze Sentiment"):
    with st.spinner('Analyzing sentiment...'):
        try:
            # Download and parse article
            article = Article(url)
            article.download()
            article.parse()
            
            # Get sentiment
            sentiment, score = get_sentiment(article.text)
            
            # Create visual representation using Streamlit components
            st.subheader("Sentiment Analysis Results")
            
            # Display score as a progress bar
            progress_value = (score + 1) / 2  # Convert from [-1,1] to [0,1]
            st.progress(progress_value)
            
            # Display metrics in columns
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Sentiment", sentiment)
            with col2:
                st.metric("Score", f"{score:.2f}")
            with col3:
                st.metric("Word Count", len(article.text.split()))
            
            # Article details
            st.subheader("Article Details")
            st.write(f"Title: **{article.title}**")
            
            # Show excerpt in expander
            with st.expander("Show article excerpt"):
                st.write(article.text[:500] + "...")
            
            # Save to history
            save_to_history(url, article.title, None, (sentiment, score))
            
        except Exception as e:
            st.error(f"Error: {e}")

