import streamlit as st

st.set_page_config(
    page_title="Florique",
    page_icon="🌸",
    layout="wide"
)

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Parisienne&display=swap');

.stApp{
    background-color:#fff7fa;
}

.hero{
    background-image:url("https://raw.githubusercontent.com/pavlovamichaela220-ai/flower/main/frame.png");
    background-repeat:no-repeat;
    background-position:center;
    background-size:contain;

    height:900px;

    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;
}

.title{
    font-family:'Parisienne', cursive;
    font-size:170px;
    color:#c98aa3;

    margin-bottom:20px;

    transition:0.4s;
}

.title:hover{
    color:#e6b3c8;

    text-shadow:
        0 0 10px rgba(230,179,200,.7),
        0 0 25px rgba(230,179,200,.5),
        0 0 45px rgba(230,179,200,.3);

    transform:scale(1.05);
}

.slogan{
    font-size:28px;
    color:#86747d;
    letter-spacing:2px;
}

</style>

<div class="hero">
    <div class="title">Florique</div>
    <div class="slogan">Flowers on your schedule.</div>
</div>

""", unsafe_allow_html=True)
