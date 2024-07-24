import streamlit as st
import functions as fu
import pandas as pd


st.set_page_config(
    initial_sidebar_state="collapsed",menu_items=None,
    page_icon="./img/taxi_logo.png",layout="wide",
    page_title="NY Taxi trips"
)
fu.local_css("style.css")
data = fu.load_data()
data_taxi_zones = fu.load_data("data/taxi-zone-lookup.csv")

with st.sidebar:
    st.markdown("### Taxi zones lookup")
    selected_zone = st.slider(label="pick a zone",label_visibility="hidden",min_value=min(data_taxi_zones["LocationID"]),max_value=max(data_taxi_zones["LocationID"]))
    selected_zone_data = data_taxi_zones.iloc[selected_zone,:]
    st.write(f'Borough: {selected_zone_data["Borough"]}\n\nZone: {selected_zone_data["Zone"]}')
    
    st.markdown("----")
    st.markdown("### Main Controls")
    show_dataset = st.toggle("Dataset", value=True)
    show_analysis= st.toggle("Analyse", value=True)
    show_predict = st.toggle("Predict", value=True)
    st.markdown("----")
    


st.title("NY Taxi trips")

st.header("Dataset")
with st.expander(label="",expanded=show_dataset):
    col3, col4 = st.columns([5,1.3])
    selected_col = col3.multiselect(label="select",label_visibility="hidden",options=data.columns,default=list(data.columns))
    with col4:
        st.write("<br>",unsafe_allow_html=True)
        st.link_button("Dataset columns dictionary","https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf",use_container_width=True)
        st.link_button("Dataset Source","https://www.kaggle.com/datasets/anandshaw2001/taxi-dataset",use_container_width=True,help="For more details")
    
    st.write(data[selected_col].head(8))