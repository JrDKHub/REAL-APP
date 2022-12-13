import streamlit as st
import pandas as pd
import numpy as np
import time

import functions as fck


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


def main():

    with st.sidebar:
        st.subheader('Bienvenue sur Real Estate Auctions Lab APP')

    option = st.selectbox('Choisissez une année 📅', ('2022', '2021', '2022'))

    if(option == '2022'):
        data_url = "https://www.data.gouv.fr/fr/datasets/r/87038926-fb31-4959-b2ae-7a24321c599a"
    elif(option == '2021'):
        pass
    elif(option == '2020'):
        pass

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

        st.header("Localiser un bien")

        commune, cp, voie ,search  = st.columns([0.25,0.25,0.25,0.25])

        # search = st.empty()

        commune.text_input("Commune", placeholder="Saisir la commune")
        voie.text_input("Voie", placeholder="Le nom de la rue , avenue, place etc ...")
        cp.number_input("Code Postal")
        search.button("Rechercher")

        st.subheader('🎚️FILTRES')
        local, pieces, surface = st.columns([0.3, 0.3, 0.3])

        with local.expander("🏘️ Type de local"):
            st.write("Choisir le type de local")
            houses = st.checkbox("Maison")
            appart = st.checkbox("Appartement")
            dep = st.checkbox("Dépendance")
            lic = st.checkbox("Local industriel et commercial")

        pieces.slider("🔢Choisir le nombre de pièces", min_value=1, max_value=6)

        start_surf, end_surf = surface.select_slider(
            "Choisir l'intervalle de la surface",
            options=[1, 100, 200, 300, 400, 500, 700, 800, 30000],
            value=(1, 100)
        )
        if houses:
            df = df[df['type local'] == 'Maison']
        df = df.sample(frac=0.1)
        st.write(df[['date mutation','nature mutation',"valeur fonciere","no voie","voie","code postal","commune","surface carrez du 1er lot","type local","nombre pieces principales"]])
        

    # with st.container():
    #     points = df[['latitude','longitude']]
    #     points['lat'] = points.latitude
    #     points['lon'] = points.longitude
    #     points.drop(['latitude','longitude'],axis=1,inplace=True)
    #     # st.write(type(points))
    #     st.map(points)


main()
