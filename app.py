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
    margin-top: 30px;
    margin-bottom: 0px;
    line-height: 1;
}

.ornament {
    text-align: center;
    font-size: 42px;
    color: #d9b6c3;
    letter-spacing: 8px;
}

.description {
    max-width: 800px;
    margin: auto;
    margin-top: 40px;
    text-align: center;
    color: #8f7a84;
    font-size: 22px;
    line-height: 1.9;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <div class="ornament">
    ❀ ❦ ❀ ✿ ❀ ❦ ❀
    </div>
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
    <div class="ornament">
    ❀ ❦ ❀ ✿ ❀ ❦ ❀
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="description">
    Welcome to Florique.<br><br>

    A flower studio open 24 hours a day, 7 days a week.

    Choose each stem individually and create a bouquet that feels uniquely yours.
    During florist hours from 8:00 to 17:00, our team can professionally hand-tie your arrangement.

    Outside these hours, Florique transforms into a fully self-service flower bar, allowing you to select, arrange and wrap your flowers whenever inspiration strikes.
    </div>
    """,
    unsafe_allow_html=True
)
