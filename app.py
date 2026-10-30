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
    background-color: #fff7fa;
}

.title {
    font-family: 'Parisienne', cursive;
    font-size: 150px;
    color: #c98aa3;
    text-align: center;
    margin-top: 80px;
    margin-bottom: 20px;
    line-height: 1;
    transition: all 0.5s ease;
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
    text-align: center;
    font-size: 28px;
    color: #e4c1cf;
    letter-spacing: 10px;
}

.description {
    max-width: 850px;
    margin: 40px auto;
    text-align: center;
    color: #8d7680;
    font-size: 20px;
    line-height: 1.9;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <div class="ornament">❀ ✿ ❀ ❦ ❀ ✿ ❀</div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="title">Florique</div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="ornament">❀ ✿ ❀ ❦ ❀ ✿ ❀</div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="description">
    A
