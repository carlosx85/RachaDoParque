import streamlit as st
from modules import principal, cadastro, financeiro, pagamento,despesa
import header  # novo módulo com o cabeçalho

if "usuario" not in st.session_state:
    st.session_state.usuario = ""
    
def show():
    # Mostra o cabeçalho
    header.show()

    # Menu lateral
    menu = st.sidebar.radio("Menu", ["Principal", "Cadastro", "Financeiro", "Pagamento", "Despesa", "Sair"])

    if menu == "Principal":
        principal.show()
    elif menu == "Cadastro":
        cadastro.show()
    elif menu == "Financeiro":
        financeiro.show()
    elif menu == "Pagamento":
        pagamento.show()
    elif menu == "Despesa":
        despesa.show()
    elif menu == "Sair":
        st.session_state.logado = False
        st.session_state.usuario = ""
        st.rerun()
