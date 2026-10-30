import streamlit as st

st.set_page_config(
    page_title="Florique",
    page_icon="🌸",
    layout="wide"
)

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap" rel="stylesheet">

<style>
.stApp {
    background-color: #ffe6f0;
}

.florique-title {
    font-family: 'Great Vibes', cursive;
    font-size: 120px;
    color: #d85a8f;
    text-align: center;
    margin-top: 80px;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    font-size: 24px;
    color: #8a5c71;
    margin-bottom: 70px;
}

div.stButton > button {
    background-color: #ffb6d5;
    color: white;
    border: none;
    border-radius: 30px;
    padding: 12px 30px;
    font-size: 18px;
}

div.stButton > button:hover {
    background-color: #e88ab6;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="florique-title">Florique</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Flowers • Gifts • Lifestyle</div>',
    unsafe_allow_html=True
)

st.markdown("<br><br>", unsafe_allow_html=True)

st.button("Prozkoumat kolekci 🌸")
