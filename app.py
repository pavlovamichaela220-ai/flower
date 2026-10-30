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
    position: absolute;
    left: 50%;
    top: 38%;
    transform: translate(-50%, -50%);

    font-family: 'Parisienne', cursive;
    font-size: 130px;
    color: #c98aa3;

    transition: all 0.4s ease;
}

.title:hover {
    color: #e6b5c9;

    text-shadow:
        0 0 15px rgba(230,181,201,0.8),
        0 0 35px rgba(230,181,201,0.6);

    transform: translate(-50%, -50%) scale(1.05);
}

.wrapper {
    position: relative;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="wrapper">', unsafe_allow_html=True)

st.image("frame.png", use_container_width=True)

st.markdown(
    """
    <div class="title">
        Florique
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)
