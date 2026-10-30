import streamlit as st

st.set_page_config(
    page_title="Florique",
    page_icon="🌸",
    layout="wide"
)

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Parisienne&display=swap');

.stApp {
    background: #fff7fa;
}

.title {
    font-family: 'Parisienne', cursive;
    font-size: 150px;
    color: #c98aa3;
    text-align: center;
    margin-top: 60px;
    margin-bottom: 15px;
    line-height: 1;

    transition: all 0.5s ease;
    cursor: default;
}

.title:hover {
    color: #e6b0c5;

    text-shadow:
        0 0 10px rgba(230,176,197,0.6),
        0 0 25px rgba(230,176,197,0.5),
        0 0 45px rgba(230,176,197,0.4);

    transform: scale(1.05);
}

.ornament {
    text-align:
