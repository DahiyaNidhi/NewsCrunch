import streamlit as st 
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #141e30 , #2c3e50);
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)
about_page = st.Page(
    page = "C:\\Users\\Rhea Menon\\Downloads\\streamlit-text-summarizer-main\\streamlit-text-summarizer-main\\views\\about_pg.py",
    title = "About this Application",
    icon = ":material/info:",
)

summary_page = st.Page(
    page = "C:\\Users\\Rhea Menon\\Downloads\\streamlit-text-summarizer-main\\streamlit-text-summarizer-main\\views\\summary.py",
    title = "Summariser",
    icon = ":material/summarize:",
)

sentiment_page = st.Page(
    page = "C:\\Users\\Rhea Menon\\Downloads\\streamlit-text-summarizer-main\\streamlit-text-summarizer-main\\views\\sentiment.py",
    title = "Sentiment Analyser",
    icon = ":material/sentiment_satisfied:",
)

history_page = st.Page(
    page = "C:\\Users\\Rhea Menon\\Downloads\\streamlit-text-summarizer-main\\streamlit-text-summarizer-main\\views\\history.py",
    title = "Analysis History",
    icon = ":material/history:",
)

chatbot_page = st.Page(
    page = "C:\\Users\\Rhea Menon\\Downloads\\streamlit-text-summarizer-main\\streamlit-text-summarizer-main\\views\\chatbot.py",
    title = "Chatbot",
    icon = ":material/headset_mic:",
)

st.logo("./images/image.png")

pg = st.navigation(
    {
        "Info" : [about_page],
        "Services": [summary_page, sentiment_page, history_page, chatbot_page]
    })

pg.run()
