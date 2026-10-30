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
    margin-top: 100px;
    line-height: 1;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <div class="title">Florique</div>
    """,
    unsafe_allow_html=True
)
