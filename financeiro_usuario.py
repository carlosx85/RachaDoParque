import streamlit as st

# Esconde o menu lateral padrão
hide_sidebar_style = """
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        [data-testid="collapsedControl"] {
            display: none;
        }
    </style>
"""
st.markdown(hide_sidebar_style, unsafe_allow_html=True)


if "usuario" not in st.session_state:
    st.session_state.usuario = ""

# Inicializa estado
if "logado" not in st.session_state:
    st.session_state.logado = False


cliente_id = st.session_state.get("cliente_id")
if cliente_id:
    st.write(f"Carregando dados do cliente {cliente_id}")
else:
    st.error("ID do cliente não encontrado.")