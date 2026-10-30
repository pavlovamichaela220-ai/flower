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

.main {
    padding-top: 20px;
}

.frame-container {
    position: relative;
    max-width: 1300px;
    margin: auto;
}

.florique-title {
    position: absolute;
    top: 40%;
    left: 50%;
    transform: translate(-50%, -50%);

    font-family: 'Parisienne', cursive;
    font-size: 150px;
    color: #c98aa3;

    transition: all 0.4s ease;
}

.florique-title:hover {
    color: #e7b8cb;

    text-shadow:
        0 0 12px rgba(231,184,203,0.6),
        0 0 24px rgba(231,184,203,0.4),
        0 0 40px rgba(231,184,203,0.3);

    transform: translate(-50%, -50%) scale(1.05);
}

.slogan {
    position: absolute;
    top: 56%;
    left: 50%;
    transform: translate(-50%, -50%);

    font-size: 26px;
    color: #8d7a82;

    letter-spacing: 2px;
    font-weight: 300;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="frame-container">', unsafe_allow_html=True)

st.image("frame.png", use_container_width=True)

st.markdown("""
<div class="florique-title">
Florique
</div>

<div class="slogan">
Flowers on your schedule.
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
