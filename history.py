import streamlit as st
from datetime import datetime
import pandas as pd

# Initialize session state for article history if it doesn't exist
if 'article_history' not in st.session_state:
    st.session_state.article_history = []

st.title("🕗 Analysis History")

st.markdown("""The sentiment analysis history page serves as a comprehensive repository for tracking the 
            emotional insights derived from various newspaper articles over time. Each entry includes 
            details such as the article title, publication date, sentiment score, and a brief overview of the analysis, 
            enabling users to easily compare and contrast different articles and their corresponding emotional tones.""")
st.markdown("<hr>", unsafe_allow_html=True)

if not st.session_state.article_history:
    st.markdown("No analysis history available yet. Start by analyzing some articles!")
else:
    # Create DataFrame for analysis
    df = pd.DataFrame(st.session_state.article_history)

    # Display summary statistics
    st.subheader("Analysis Overview")
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Articles Analyzed", len(df))

    with col2:
        sentiment_counts = df['sentiment'].apply(lambda x: x[0] if x else None).value_counts()
        st.write("Sentiment Distribution:")
        st.write(sentiment_counts)

    # Display full history
    st.subheader("Full History")
    for idx, item in enumerate(reversed(st.session_state.article_history)):
        with st.expander(f"#{len(st.session_state.article_history) - idx}. {item['title']}"):
            st.write(f"Analyzed on: {item['timestamp']}")
            st.write(f"URL: {item['url']}")
            if item.get('summary'):
                st.write("Summary:", item['summary'])
            if item.get('sentiment'):
                st.write(f"Sentiment: {item['sentiment'][0]} (Score: {item['sentiment'][1]:.2f})")
