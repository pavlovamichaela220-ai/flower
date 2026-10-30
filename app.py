import streamlit as st

st.set_page_config(
    page_title="Florique",
    page_icon="🌸",
    layout="wide"
)

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Parisienne&display=swap" rel="stylesheet">

<style>
.stApp {
    background-color: #fff7fa;
}

.title {
    font-family: 'Parisienne', cursive;
    font-size: 140px;
    color: #c98aa3;
    text-align: center;
    margin-top: 90px;
    margin-bottom: 10px;
    line-height: 1;
}

.description {
    max-width: 700px;
    margin: auto;
    text-align: center;
    color: #8f7a84;
    font-size: 20px;
    line-height: 1.8;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">Florique</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="description">
    A self-service flower studio open 24/7.<br>
    Choose your favourite flowers, create your own bouquet,
    or let one of our florists hand-tie it for you between 8:00 and 17:00.
    </div>
    """,
    unsafe_allow_html=True
)
