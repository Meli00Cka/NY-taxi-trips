import streamlit as st
import pandas as pd



def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


@st.cache_data
def load_data():
    data = pd.read_csv("./data/taxi_trips.csv", low_memory=False)
    return data.drop(data.index[11916662:])