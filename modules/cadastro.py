import streamlit as st
from database import inserir_cliente, buscar_cliente_por_id,inserir_racha_financeiro
import streamlit.components.v1 as components

 
def show():
    if not st.session_state.get("logado", False):
        st.warning("Acesso negado. Faça login para continuar.")
        st.stop()

    st.subheader("Cadastro de Cliente")

    # --- FORMULÁRIO DE CADASTRO ---
    with st.form("form_cadastro"):
        nome     = st.text_input("Nome", max_chars=100)
        login  = st.text_input("Apelido", max_chars=100)
        
        col1, col2 = st.columns([1, 4])
        with col1:
            ddd = st.number_input("Telefone", min_value=0, max_value=99, step=1, format="%d")
        with col2:
            telefone = st.number_input("Telefone", min_value=0, max_value=999999999, step=1, format="%d")
            
            
           # Segunda linha: Dia Nasc e Mês Nasc
        col3, col4 = st.columns([1, 4])
        with col3:
            dianasc = st.text_input("Dia Nascimento", max_chars=2)
        with col4:
            mesnasc = st.text_input("Mês Nascimento", max_chars=4)
                
        # Mapeia o texto visível para o valor interno
        opcoes = {
            "Padrão": "P",
            "Dispensado": "D"
        }

        # Selectbox exibindo só os textos
        opcao_escolhida = st.selectbox("Selecione o Tipo de Status do Jogador:", list(opcoes.keys()))
        

        # Pega o valor real que você quer usar (N ou D)
        StatusdePagamento = opcoes[opcao_escolhida]
        
        botao_cadastrar = st.form_submit_button("Cadastrar")

    if botao_cadastrar:
        if nome.strip() == ""or  login.strip() == "":
            st.error("O campo 'Nome/Apelido' são obrigatório.")
        else:
            cliente_id = inserir_cliente(nome,login,ddd,telefone,StatusdePagamento,dianasc,mesnasc)
            if cliente_id:
                st.success(f"Jogador  '{nome}' Cadastrado com sucesso!)")

                # Buscar cliente e mostrar após o form
                cliente = buscar_cliente_por_id(cliente_id)
                if cliente:
                    inserir_racha_financeiro(cliente_id)# grava o cliente_id na session
                  
 
            else:
                st.error("Erro ao cadastrar o cliente.")
