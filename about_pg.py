import streamlit as st


col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("./images/image.png", width=250)

with col2:
    st.title("NewsCrunch")
    st.write("""In today's fast-paced world, staying informed can be a challenge. 
             Our mission is to help you grasp essential information quickly, allowing you to 
             stay updated on current events without feeling overwhelmed. By distilling complex news into easily 
             digestible formats, we empower you to engage with the stories that matter most, fostering a more 
             informed and connected community.""")
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<h4> Key Features: </h4>", unsafe_allow_html=True)
st.markdown("""
<ul>
    <li> <b>Text Summarization</b>: Utilizes Pegasus for efficient and accurate summarization of news articles.</li>
    <li> <b>Sentiment Analysis</b>: Implements TextBlob's polarity analysis to gauge the sentiment of news content.</li>
    <li> <b>Interactive Chatbot</b>: Powered by Llama 3.1, our chatbot allows users to ask questions and engage in discussions related to articles.</li>
    <li> <b>Analysis History</b>: Users can access a dedicated page to view their analysis history, making it easy to revisit previous insights.</li>
            
</ul>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

summ = "./images/summary.png"
sent = "./images/sentiment.png" 
hist = "./images/history.png"
chat = "./images/chat.png"

with col1:
    st.image(summ, use_column_width=True)
    st.subheader("Article Summaries")
    st.write("Perform quick bite-sized summaries.")

with col2:
    st.image(sent, use_column_width=True)
    st.subheader("Sentiment Analysis")
    st.write("Decipher inherent emotions of articles.")

with col3:
    st.image(hist, use_column_width=True)
    st.subheader("History Display")
    st.write("Displays full analysis history.")

with col4:
    st.image(chat, use_column_width=True)
    st.subheader("Interactive Chatbot")
    st.write("Ultra-fast Llama 3.1 Chatbot.")

st.markdown("<hr>", unsafe_allow_html=True)
st.write("Made by Rhea Menon (A029) and Nidhi Dahiya (A037)")


