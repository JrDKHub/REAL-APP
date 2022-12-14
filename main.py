import streamlit as st
import pandas as pd
import numpy as np
import time
import re

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
        st.subheader('Real Estate Auctions Lab APP')
        st.image("assets/logo.png")

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

        commune, cp, voie   = st.columns([0.3,0.3,0.3])

        commune = commune.text_input("Commune", placeholder="Saisir la commune")
        voie = voie.text_input("Voie", placeholder="Le nom de la rue , avenue, place etc ...")
        cp = cp.number_input("Code Postal")
        
       

        st.subheader('🎚️FILTRES')

        local, pieces, surface = st.columns([0.3, 0.3, 0.3])

        with local.expander("🏘️ Type de local"):
            st.write("Choisir le type de local")
            houses = st.checkbox("Maison")
            appart = st.checkbox("Appartement")
            dep = st.checkbox("Dépendance")
            lic = st.checkbox("Local industriel et commercial")

        pieces = pieces.slider("🔢Choisir le nombre de pièces", min_value=1, max_value=6)

        start_surf, end_surf = surface.select_slider(
            "Choisir l'intervalle de la surface (en m²)",
            options=[1, 100, 200, 300, 400, 500, 700, 800, 30000],
            value=(1, 100)
        )

        local_filter = []
        if houses:
            local_filter.append('Maison')
        if appart:
            local_filter.append('Appartement')
        if dep:
            local_filter.append('Dépendance')
        if lic:
            local_filter.append('Local industriel et commercial')

        search = st.empty()
        if search.button("Rechercher"):
            
            df1 = clean_data(df)
            

            if len(local_filter) == 0:

                if len(commune) > 0:
                    st.write("Bien de la commune ",commune)
                    df2 = df1.loc[(df1['commune'].str.contains(commune,flags=re.IGNORECASE, case=True))]
                    # df1 = df1[df['type local'].isin(local_filter)]
                    df2 = df2[(df2['surface reelle bati'] >= start_surf) & (df2['surface reelle bati'] <= end_surf) ]
                    df2 = df2[df2['nombre pieces principales'] == pieces]
                    st.write(df2)

                if len(voie) > 0 :
                    st.write("Bien de la voie ",voie)
                    df3 = df1.loc[(df1['voie'].str.contains(voie,flags=re.IGNORECASE, case=True))]
                    # df1 = df1[df['type local'].isin(local_filter)]
                    df3 = df3[(df3['surface reelle bati'] >= start_surf) & (df3['surface reelle bati'] <= end_surf) ]
                    df3 = df3[df3['nombre pieces principales'] == pieces]
                    st.write(df3)
                
                if cp > 0 :
                    st.write("Bien au code postal ",cp)
                    df4 = df1[df1['code postal'] == cp]
                    # df1 = df1[df['type local'].isin(local_filter)]
                    df4 = df4[(df4['surface reelle bati'] >= start_surf) & (df4['surface reelle bati'] <= end_surf) ]
                    df4 = df4[df4['nombre pieces principales'] == pieces]
                    st.write(df4)
                
                if ( cp > 0 and len(voie) > 0 and len(commune) > 0):
                    df5 = df1.loc[(df1['voie'].str.contains(voie,flags=re.IGNORECASE , case=True)) & (df1['code postal'] == cp) & (df1['commune'].str.contains(commune,flags=re.IGNORECASE, case=True)) ]
                    # df1 = df1[df['type local'].isin(local_filter)]
                    df5 = df5[(df5['surface reelle bati'] >= start_surf) & (df5['surface reelle bati'] <= end_surf) ]
                    df5 = df5[df5['nombre pieces principales'] == pieces]
                    st.write(df5)

            if len(local_filter) > 0:

                if len(commune) > 0:
                    st.write("Bien de la commune ",commune)
                    df2 = df1.loc[(df1['commune'].str.contains(commune,flags=re.IGNORECASE, case=True))]
                    df2 = df2[df2['type local'].isin(local_filter)]
                    df2 = df2[(df2['surface reelle bati'] >= start_surf) & (df2['surface reelle bati'] <= end_surf) ]
                    df2 = df2[df2['nombre pieces principales'] == pieces]
                    st.write(df2)

                if len(voie) > 0 :
                    st.write("Bien de la voie ",voie)
                    df3 = df1.loc[(df1['voie'].str.contains(voie,flags=re.IGNORECASE, case=True))]
                    df3 = df3[df3['type local'].isin(local_filter)]
                    df3 = df3[(df3['surface reelle bati'] >= start_surf) & (df3['surface reelle bati'] <= end_surf) ]
                    df3 = df3[df3['nombre pieces principales'] == pieces]
                    st.write(df3)
                
                if cp > 0 :
                    st.write("Bien au code postal ",cp)
                    df4 = df1[df1['code postal'] == cp]
                    df4 = df4[df4['type local'].isin(local_filter)]
                    df4 = df4[(df4['surface reelle bati'] >= start_surf) & (df4['surface reelle bati'] <= end_surf) ]
                    df4 = df4[df4['nombre pieces principales'] == pieces]
                    st.write(df4)
                
                if ( cp > 0 and len(voie) > 0 and len(commune) > 0):
                    df5 = df1.loc[(df1['voie'].str.contains(voie,flags=re.IGNORECASE , case=True)) & (df1['code postal'] == cp) & (df1['commune'].str.contains(commune,flags=re.IGNORECASE, case=True)) ]
                    df5 = df5[df5['type local'].isin(local_filter)]
                    df5 = df5[(df5['surface reelle bati'] >= start_surf) & (df5['surface reelle bati'] <= end_surf) ]
                    df5 = df5[df5['nombre pieces principales'] == pieces]
                    st.write(df5)
                

            

    # with st.container():
    #     points = df[['latitude','longitude']]
    #     points['lat'] = points.latitude
    #     points['lon'] = points.longitude
    #     points.drop(['latitude','longitude'],axis=1,inplace=True)
    #     # st.write(type(points))
    #     st.map(points)


def clean_data(df):
    df["valeur fonciere"] = [float(str(i).replace(",", "")) for i in df["valeur fonciere"]]
    df['code postal']= df['code postal'].fillna(0)
    df['code postal'] = df['code postal'].astype(int)
    df1 = df[['date mutation','nature mutation','valeur fonciere','no voie','voie','code postal','commune','type local','surface reelle bati','nombre pieces principales','surface terrain']]
    df1['valeur fonciere'] = df1['valeur fonciere'].fillna(0)
    df1['surface terrain'] = df1['surface terrain'].fillna(0)
    df1['surface reelle bati'] = df1['surface reelle bati'].fillna(0)

    df1 = df1[df1['surface reelle bati'] > 0]
    df1 = df1[df1['valeur fonciere'] > 0]
    df1 = df1[df1['surface terrain'] >= 0]

    df1.loc[df1['surface terrain'] > 1, 'prix m2'] = df1['valeur fonciere']/(df1['surface reelle bati']+ np.log(df1['surface terrain']))
    df1.loc[df1['surface terrain'] <= 1, 'prix m2'] = df1['valeur fonciere']/df1['surface reelle bati'] 
    df1.dropna(inplace=True)
    # df1["valeur fonciere"] = df1["valeur fonciere"].astype(int)
    df1["no voie"] = df1["no voie"].astype(int)
    df1["nombre pieces principales"] = df1["nombre pieces principales"].astype(int)
    return df1  

main()
