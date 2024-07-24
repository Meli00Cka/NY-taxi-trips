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


st.header("Analysis")
with st.expander(label="",expanded=show_analysis):
    plot_caption = {
        1:"Let's start with first column '<b>VendorID</b>' which indicates 2 types of technologies used in taxis<br><br>1= Creative Mobile Technologies,LLC<br>2= VeriFone Inc<br><br>As you can see the pickup frequency in the dataset, It's obvious that the first technology had the most frequency.",
        2:"Now let's see which months had more taxi requests.<br>Okay, seems like this dataset contains taxi data from <i>January</i> and <i>February</i>, and rarely from other months.<br>In this case, we can't analyse this chart.",
        3:"This plot shows different payment types passengers used, Here is a guide so you don't get confused:<br>1= Credit card<br>2= Cash<br>3= No charge<br>4= Dispute<br>5= Unknown<br>6= Voided trip<br><br>Data show that most of the time passengers preferred credit cards than cash.",
        4:"This correlation between trip distance and fare amount shows that the farther you go,<br> the more expensive it gets :)<br><br>And also there are some data with 0 distance that should be handled later, or if its possible ask someone who works in this industry for more information.",
        5:"In NY around 72% of cabs had 1 passenger<br>and somehow 0.00022% of people managed to take 1 cab for them and their 8 other friends.",
        6:"The least fare amount is $11 in taxi zone 193, after a quick lookup I found the zone information:<br><br>Borough: Manhattan<br>Zone: Randall's Island",
        7:"I was curious if the technology used in taxis could change the price or no,<br>And it seems like they are actually the same. But you might pay $0.77 more for taxis that use _VeriFone Inc_ in them.",
        8:"And the last one is about rush hour.<br>The plot shows that the lowest pickups are at __1 AM__ to __5 AM__,<br>And around __5 PM__ to __7 PM__ it can be hard to find a cab, or maybe cabs get stuck in a traffic jam."
    }
    
    for i in range(1,9):
        col1, col2 = st.columns([5.3,4])
        
        with open(f"./plots/p{i}.html", "r") as f:
            st.markdown("---")
            # plots[f"p{i}"] = f.read() # to save plots in a dict
            with col1:
                st.components.v1.html(f.read(),height=620, width=820)
            with col2:
                if i==6:
                    st.write(f"<br>{plot_caption[i]}",unsafe_allow_html=True)
                    st.image("./img/randalls_island.png", caption="Randall's Island", output_format="PNG",  width=500)
                    st.write("You can use the tools on the plot to take a closer look if you wish,\n\nOr look up other zones with the tool I put in _left sidebar_.")
                else:
                    st.write(f"<br><br><br><br><br>{plot_caption[i]}",unsafe_allow_html=True)