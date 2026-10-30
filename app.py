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
    background-color: #fff5f8;
}

.title {
    font-family: 'Parisienne', cursive;
    font-size: 140px;
    color: #d88ca8;
    text-align: center;
    margin-top: 90px;
    line-height: 1;
}

.subtitle {
    text-align: center;
    color: #a07d8e;
    font-size: 22px;
    letter-spacing: 4px;
    margin-top: 10px;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <div class="title">Florique</div>
    <div class="subtitle">FLOWERS • GIFTS • LIFESTYLE</div>
    """,
    unsafe_allow_html=True
)
