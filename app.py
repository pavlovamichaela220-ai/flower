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
    margin-top: 80px;
    transition: all 0.5s ease;
}

.title:hover {
    color: #e6b0c5;
    transform: scale(1.05);
    text-shadow:
        0 0 10px rgba(230,176,197,0.7),
        0 0 25px rgba(230,176,197,0.5);
}

.description {
    max-width: 800px;
    margin: 40px auto;
    text-align: center;
    color: #8d7680;
    font-size: 22px;
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
    A self-service flower studio open 24/7.<br><br>

    Choose your flowers individually and create a bouquet that feels uniquely yours.

    Between 8:00 and 17:00, our florists are available to hand-tie your bouquet.

    Outside these hours, Florique becomes a fully self-service flower bar where you can create and wrap your own arrangement at any time.
    </div>
    """,
    unsafe_allow_html=True
)
