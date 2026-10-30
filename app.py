import streamlit as st

st.set_page_config(
    page_title="Florique",
    page_icon="🌸",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background-color: #fff7fa;
}

.title {
    font-family: 'Parisienne', cursive;
    font-size: 140px;
    color: #c98aa3;
    text-align: center;
    margin-top: 20px;
    margin-bottom: 0;
}

.text {
    max-width: 700px;
    margin: auto;
    color: #8f7a84;
    text-align: center;
    font-size: 20px;
    line-height: 1.8;
}

</style>
""", unsafe_allow_html=True)

st.image("textures/ornament_top.png", use_container_width=True)

st.markdown(
    '<div class="title">Florique</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="text">

A flower studio open 24/7.

Choose every stem yourself and create a bouquet that reflects your style.
Between 8:00 and 17:00, our florists are available to hand-tie your arrangement.

Outside these hours, Florique becomes a fully self-service flower bar where creativity blooms at any time of day.

</div>
""", unsafe_allow_html=True)

st.image("textures/ornament_bottom.png", use_container_width=True)
