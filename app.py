import os
import streamlit as st
import requests
from streamlit_lottie import st_lottie
import Main
st.set_page_config(page_title="Jake The Assistant", page_icon="wave", layout= "wide")
def loadlottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_coding = loadlottieurl("https://assets4.lottiefiles.com/packages/lf20_w51pcehl.json")
with st.container():
    st.subheader(":wave: Wellcome to Jake The Assistant!")
    st.title("Guruha Studios")
    st.write("Start")
with st.container():
    st.write("---")
    left_coloumn, right_coloumn = st.columns(2)
    with left_coloumn:
        st.write("Jake is still under construction...")
        st.write("##")
        if st.button("Start"):
           Main()
    with right_coloumn:
        st_lottie(lottie_coding, height = 450, key = "coding")
