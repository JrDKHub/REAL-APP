import streamlit as st
import streamlit_authenticator as stauth
import base64



if st.session_state['authentication_status']:

    try:
        if st.session_state['authenticator'].reset_password(st.session_state['username'], 'Reinitialisation du mot de passe'):
            st.success("Mot de passe modifié avec succès")
            # ⚠️ updaye yaml each time , read yaml dump doc
            # with open('../config.yaml', 'w') as file:
            #     yaml.dump(config, file, default_flow_style=False)
    except Exception as e:
        st.error(e)

    try:
        if st.session_state['authenticator'].update_user_details(st.session_state['username'], 'Mettre à jour les informations sur le profil'):
            st.success('Données mises à jour avec succès')
            # ⚠️ updaye yaml each time , read yaml dump doc
            # with open('../config.yaml', 'w') as file:
            #     yaml.dump(config, file, default_flow_style=False)
    except Exception as e:
        st.error(e)
else:
    st.write("Connectez vous!!")
    ### gif from local file
    file_ = open("assets/images/denied.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
        unsafe_allow_html=True,
    )

