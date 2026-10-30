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

.frame-container {
    position: relative;
    width: 100%;
    text-align: center;
    margin-top: 30px;
}

.frame-title {
    position: absolute;
    top: 38%;
    left: 50%;
    transform: translate(-50%, -50%);

    font-family: 'Parisienne', cursive;
    font-size: 120px;
    color: #c98aa3;

    transition: all 0.5s ease;
}

.frame-title:hover {
    color: #e8b4ca;

    text-shadow:
        0 0 10px rgba(232,180,202,.6),
        0 0 25px rgba(232,180,202,.5),
        0 0 40px rgba(232,180,202,.4);

    transform: translate(-50%, -50%) scale(1.05);
}

.frame-text {
    position: absolute;

    top: 56%;
    left: 50%;

    transform: translateX(-50%);

    width: 60%;

    font-size: 22px;
    color: #7d7278;
    line-height: 1.8;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="frame-container">', unsafe_allow_html=True)

st.image("frame.png", use_container_width=True)

st.markdown("""
<div class="frame-title">
Florique
</div>

<div class="frame-text">

A flower studio open 24/7.

Choose your own flowers, create your bouquet exactly the way you like it,
or have it professionally tied by our florists between 8:00 and 17:00.

Outside florist hours, Florique becomes a fully self-service flower bar,
allowing you to shop and create whenever inspiration strikes.

</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
