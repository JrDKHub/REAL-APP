import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bokeh.plotting import figure
import plotly.figure_factory as ff
import seaborn as sns
import pydeck as pdk
import time

import functions as fck


from streamlit_folium import st_folium
import folium


st.set_page_config(
    page_title="REAL APP",
    page_icon="🏬",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        # 'Get Help': 'https://www.linkedin.com/in/ars%C3%A8ne-bakandakan/',
        'About': "# cool app! Made with 💖"
    }
)



st.title('** REAL **')
st.info('ℹ️ Bienvenue sur notre appli de visualisation de données!')

def main():

    with st.sidebar:
        st.subheader('Welcome on Real Estate Auctions Lab APP')

    option = st.selectbox('Choisissez une année 📅',('2022','2021','2022'))

    if(option == '2022'):
        data_url = 'data/full_2022.csv'
    elif(option == '2021'):
        data_url = 'data/full_2021.csv'
    elif(option == '2020'):
        data_url = 'data/full_2020.csv'

    # Mis à jour du chargement à chaque itération.
    data_load_state = st.empty()
    bar = st.progress(0)
    for i in range(100):
        data_load_state.text(f'Chargement des données... {i+1}➗')
        bar.progress(i + 1)
        time.sleep(0.1)
    df = fck.load_data(data_url)
    data_load_state.text('Chargement des données...Terminé 💯!!')

    with st.container():
        st.header('🎚️FILTRES')
        local , pieces , surface = st.columns([0.3,0.3,0.3])

        with local.expander("🏘️ Type de local"):
            st.write("Choisir le type de local")
            houses = st.checkbox("Maison")
            appart = st.checkbox("Appartement")
            dep =  st.checkbox("Dépendance")
            lic = st.checkbox("Local industriel et commercial")

        pieces.slider("🔢Choisir le nombre de pièces", min_value = 1, max_value = 6)

        start_surf, end_surf = surface.select_slider(
            "Choisir l'intervalle de la surface",
            options=[1, 100,200,300,400,500,700,800,30000],
            value=(1,100)
        )
        
        

    # with st.container():
    #     points = df[['latitude','longitude']]
    #     points['lat'] = points.latitude
    #     points['lon'] = points.longitude
    #     points.drop(['latitude','longitude'],axis=1,inplace=True)
    #     # st.write(type(points))
    #     st.map(points)




main()