import streamlit as st
from modules.principal import show as principal_show
from modules.cadastro import show as cadastro_show
from modules.financeiro import show as financeiro_show
from modules.pagamento import show as pagamento_show
from modules.despesa import show as despesa_show 
import header  # se tiver


if "usuario" not in st.session_state:
    st.session_state.usuario = ""

def show():
    header.show()

    menu = st.sidebar.radio("Menuaa", ["Principal", "Cadastro", "Financeiro", "Pagamento", "Despesa", "Sair"])


    if menu == "Principal":
        principal_show()
    elif menu == "Cadastro":
        cadastro_show()
    elif menu == "Financeiro":
        financeiro_show()
    elif menu == "Pagamento":
        pagamento_show()
    elif menu == "Despesa":
        despesa_show()
    elif menu == "Sair":
        st.session_state.logado = False
        st.session_state.usuario = ""
        st.rerun()
        
        
        
 
    header_html = f"""
    <div style="display: flex; align-items: center; padding: 10px 0 5px 0;">
        <img src="https://boladecapotao.com/img/Racha_Logo_G.png" width="50" style="margin-right: 15px;">
        <h5 style="margin: 0;">Racha do Parque  ({st.session_state.usuario})</h5>
    </div>
    <hr style="margin-top: 5px; margin-bottom: 15px;">
    """
    st.markdown(header_html, unsafe_allow_html=True)

