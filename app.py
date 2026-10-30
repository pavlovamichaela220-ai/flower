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
    font-family: Georgia, serif;
    font-size: 100px;
    color: #c98aa3;
    text-align: center;
    margin-top: 50px;
    margin-bottom: 50px;
}

.frame {
    background-color: white;
    max-width: 900px;
    margin: auto;
    padding: 60px;
    border-radius: 30px;
    box-shadow: 0px 10px 40px rgba(0,0,0,0.08);
}

.frame-title {
    text-align: center;
    font-size: 70px;
    color: #c98aa3;
    margin-bottom: 25px;
    font-family: Georgia, serif;
}

.frame-text {
    text-align: center;
    font-size: 22px;
    color: #6d6d6d;
    line-height: 1.8;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <div class="title">Florique</div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="frame">
        <div class="frame-title">Florique</div>
        <div class="frame-text">

        Welcome to a new generation flower studio.

        Florique is open 24 hours a day, 7 days a week.
        Choose exactly the flowers you love and create a bouquet that feels uniquely yours.

        During working hours from 8:00 to 17:00, our florists are available to hand-tie your bouquet and help bring your vision to life.

        Outside of these hours, Florique transforms into a fully self-service flower bar where you can select, arrange and wrap your own flowers at your own pace.

        Because flowers should fit your schedule, not the other way around.

        </div>
    </div>
    """,
    unsafe_allow_html=True
)
