import streamlit as st
# ⚠️ fork the project and create the french version
import streamlit_authenticator as stauth
import yaml
import home
import datetime


st.set_page_config(
    page_title="Login Real",
    page_icon="🏬",
    layout="wide",
    initial_sidebar_state="expanded",
    # menu_items={
    #     # 'Get Help': 'https://www.linkedin.com/in/ars%C3%A8ne-bakandakan/',
    #     'About': "# cool app! Made with 💖"
    # }
)

# importing yaml config file for logging

# class PrettySafeLoader(yaml.SafeLoader):
#     def construct_python_tuple(self, node):
#         return tuple(self.construct_sequence(node))

# PrettySafeLoader.add_constructor(
#     u'tag:yaml.org,2002:python/tuple',
#     PrettySafeLoader.construct_python_tuple)

with open('assets/config/auth.yaml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)
    # config = yaml.load(file, Loader=yaml.PrettySafeLoader) #alternative not tested yet

# importing cookies for authentication
st.session_state['authenticator'] = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)


# variables 

info = st.sidebar.empty()
c1,c2,c3 = st.columns([1,1,1])



# creating logging form (sidebar or main 🤔?)
name, authentication_status, username = st.session_state['authenticator'].login('Connexion', 'sidebar')

# when logged in
if st.session_state["authentication_status"]:
    # logout button
    st.session_state['authenticator'].logout('❌Déconnexion', 'sidebar')
    # login message
    st.sidebar.success(f'Welcome *{st.session_state["name"]}*👋')

    if st.button("Explorez, visualisez, Estimez!!!"):
        home.main()

# logging fail
elif st.session_state["authentication_status"] == False:
    st.error('la combinaison Username/password est incorrecte')


# Not logged in
elif st.session_state["authentication_status"] == None:
        
        info.info("💡Connexion nécessaire")

        if st.sidebar.button("Créer un compte"):
            try:
                with c3:
                    if st.session_state['authenticator'].register_user('Création de compte', preauthorization=False):
                        #preauthorization preauthorized emails of users who can register and add their credentials to the auth.yaml configuration file
                        # Setting the preauthorization argument to False allow anyone to sign up
                        st.success('Utilisateur crée avec succès!🎊')
                        st.balloons()
            except Exception as e:
                st.error(e)

        if st.sidebar.button("Mot de passe oublié?"):
            try:
                with c3 :
                    username_forgot_pw, email_forgot_password, random_password = st.session_state['authenticator'].forgot_password('Mot de passe oublié')
                    if username_forgot_pw:
                        st.success('Nouveau mot de passe envoyé avec succès')
                        # Random password to be transferred to user securely
                    elif username_forgot_pw == False:
                        st.error('Utilisateur non trouvé! 😓')
            except Exception as e:
                st.error(e)
        sig = st.sidebar.write(f"Copyright Tous Droits Reservés {datetime.datetime.now().year}")



        # centering REAL logo
        # ⚠️ desactivate image expansion
        
        with c1:
            st.image("assets/images/logo.png")
            st.markdown(
            """
            **REAL** vous fournit des informations précises et concises sur l'immobilier en France.
            """)
            st.info("ℹ️ France métropolitaine et les DOM-TOM, à l’exception de l’Alsace, de la Moselle et de Mayotte")
            
            

        with c2:
            st.markdown(
            """
            ### Avec **REAL**, vous pouvez : 
            - 🤑Obtenir des informations à jour sur la valeur marchande actuelle des propriétés (Même les biens vendus aux enchères).  
            - 🗺️📊Consulter représentations visuelles(graphiques , cartes).
            - Comparer les prix et suivre les tendances et évolutions du marché.
            - Voir les statistiques détaillées (basée sur les estimations de nos algorithmes et l'analyse de nos experts) et prendre une décision sur l'achat de votre prochaine maison. 
            - 
            
            """)
            # st.markdown(
            # """  
            # ### Les plus
            # - La valeur des biens( valeurs foncières, prix au m2 ) 
            # - Les dates, L'âge des biens et les types de transactions
            # - Les surfaces (loi carrez & surface du terrain)
            # - Le nombre de pièces
            # - Des informations sur les proches commodités
            # - Des statistiques Démographiques par zone de recherche
            
            # """
            # )
            # Nous vous fournissons des  qui donnent un aperçu de la répartition des prix dans le pays et vous pouvez naviguer par prix, emplacement et type de propriété.  
              
            # Avec RealEstatePriceView, les utilisateurs peuvent comparer le prix des propriétés dans différentes zones et suivre les tendances du marché , permettant aux utilisateurs de prendre des décisions éclairées concernant l'achat de leur prochaine maison..  
            # L'application fournit également des informations détaillées sur les prix moyens de différents types de propriétés, 
            # Nos algorithmes puissants et nos analyses d'experts vous fourniront une estimation précise des prix moyens des propriétés par régions , par type

        with c3:
            pass
       
          
        
