import streamlit as st

st.set_page_config(page_title="Reddot Photography", layout="wide")

st.title("📸 Welcome to Reddot Photography")
st.write("Explore our beautiful work across weddings, portraits, and nature!")

st.header("Featured Photos")

cols = st.columns(3)
with cols[0]:
    st.image("https://raw.githubusercontent.com/Devesh9213/Reddot/main/images/wedding1.png", caption="Wedding")
    st.image("https://raw.githubusercontent.com/Devesh9213/Reddot/main/images/portrait1.png", caption="Portrait")
with cols[1]:
    st.image("https://raw.githubusercontent.com/Devesh9213/Reddot/main/images/wedding2.png", caption="Wedding")
    st.image("https://raw.githubusercontent.com/Devesh9213/Reddot/main/images/portrait2.png", caption="Portrait")
with cols[2]:
    st.image("https://raw.githubusercontent.com/Devesh9213/Reddot/main/images/nature1.png", caption="Nature")
    st.image("https://raw.githubusercontent.com/Devesh9213/Reddot/main/images/nature2.png", caption="Nature")

st.markdown("---")
st.subheader("🌐 Visit Full Website")
st.markdown("[Click here to open the full site](https://devesh9213.github.io/Reddot/)")
st.markdown("© 2025 Reddot Photography")
