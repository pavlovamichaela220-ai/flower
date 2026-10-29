import streamlit as st

st.set_page_config(
    page_title="Moje stránka",
    page_icon="🚀",
    layout="wide"
)

st.title("Ahoj světe!")
st.write("Moje první Streamlit stránka.")

jmeno = st.text_input("Jak se jmenuješ?")

if jmeno:
    st.success(f"Ahoj {jmeno}!")

