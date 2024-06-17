import streamlit as st
import functions as fu
import pandas as pd


st.set_page_config(
    initial_sidebar_state="expanded",menu_items=None,
    page_icon="./img/taxi_logo.png",layout="wide",
    page_title="NY Taxi trips"
)
fu.local_css("style.css")
data = fu.load_data()


with st.sidebar:
    st.markdown("----")
    st.markdown("### Main Controls")
    show_dataset = st.toggle("Dataset details", value=True)
    show_1 = st.toggle("show_1", value=True)
    show_2 = st.toggle("show_2", value=True)
    show_3 = st.toggle("show_3", value=True)
    st.markdown("----")
    
    st.markdown("### Plots")
    st.markdown("##### First plot")
    show_4 = st.toggle("show_4", value=True)
    show_5 = st.toggle("show_5", value=True)
    st.markdown("##### second plot")
    show_6 = st.toggle("show_6", value=True)
    show_7 = st.toggle("show_7", value=True)
    st.markdown("----")


with st.container():
    st.markdown("# NY Taxi trips")


if show_dataset:
    with st.container(border=True):
        col3, col4 = st.columns([5,1.3])
        selected_col = col3.multiselect(label="select",label_visibility="hidden",options=data.columns,default=["passenger_count","trip_distance","fare_amount","tip_amount","total_amount","payment_type","PULocationID","tolls_amount"])
        col4.write("<br>",unsafe_allow_html=True)
        col4.link_button("Dataset Source","https://www.kaggle.com/datasets/anandshaw2001/taxi-dataset",use_container_width=True,help="For more details")
        
        col1, col2 = st.columns(2)
        col1.write(data.describe())
        col2.write(data[selected_col].head(8))