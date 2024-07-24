import streamlit as st
import pandas as pd



def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


@st.cache_data
def load_data(path="./data/dataset_sample.csv"):
    return pd.read_csv(path)