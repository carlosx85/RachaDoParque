import streamlit as st
from database import validar_login
import main_menu
 

# Inicializa variáveis da sessão, se ainda não existirem
if "usuario" not in st.session_state:
    st.session_state.usuario = ""

if "logado" not in st.session_state:
    st.session_state.logado = False

# Se estiver logado, mostra o menu principal
if st.session_state.logado:
    main_menu.show()

# Caso contrário, mostra tela de login
else:
    st.markdown(
        """
        <div style="text-align: center;">
            <img src="https://boladecapotao.com/img/Racha_Logo_G.png" width="150">
            <p style="font-size: 12px; margin-top: 5px;">Racha do Parque</p>
        </div>
        """,
        unsafe_allow_html=True
    )

 
login = st.text_input("Login")
senha = st.text_input("Senha", type="password")

if st.button("Entrar"):
    if validar_login(login, senha):
        st.session_state.logado = True
        st.session_state.usuario = login
        st.success("Login realizado com sucesso!")
    else:
        st.error("Usuário ou senha inválidos.")
  
