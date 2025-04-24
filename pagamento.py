import streamlit as st
from database import buscar_logins,buscar_anos,buscar_meses,buscar_logins,atualizar_valor,buscar_usuario_por_seq1
from datetime import datetime
import pandas as pd
import locale

import locale

try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except locale.Error:
    locale.setlocale(locale.LC_ALL, '')  # Usa o default do sistema
 
st.subheader("Financeiro")
 


def show():
    
    # Pegar mês e ano atual
    mes_atual = datetime.now().month
    ano_atual = datetime.now().year

    # Listas de opções
    meses = list(range(1, 13))
    anos = list(range(2025, 2031))
    
    # Carregar opções 
    meses = buscar_meses()
    anos = buscar_anos()
    seq = buscar_anos()

    
            
    # Buscar os dados
    dados_logins = buscar_logins()  # Lista de tuplas: (Seq, Login, Nome)

    # Formatar as opções para exibição
    opcoes =  [f"{login} ({nome} - {seq})" for seq, login, nome in dados_logins]
    # Criar o selectbox
    selecionado = st.selectbox("Selecione o Jogador:", opcoes)

    # Recuperar os dados reais com base na seleção
    indice = opcoes.index(selecionado)
    seq, login_real, nome = dados_logins[indice]

    # Criar colunas para mês e ano
    col1, col2, _ = st.columns([2, 4, 6])
    with col1:
        mes = st.selectbox("Mês", meses, index=meses.index(mes_atual))
    with col2:
        if ano_atual in anos:
            ano = st.selectbox("Ano", anos, index=anos.index(ano_atual))
        else:
            ano = st.selectbox("Ano", anos)
            
        # Formata" ",r as opções para exibição
    tipopagamento =  [ " ","Pago", "Em Negociacao"]
    # Criar o selectbox
    tipo = st.selectbox("Selecione o Status do Pagamento:", tipopagamento)

    # Input do valor
    valor = st.number_input("Digite o Valor (exato):", min_value=0.0)

    if st.button("Efetuar o pagamento"):
        atualizar_valor(seq, mes, ano, valor,tipo)
        st.success("✅ Pagamento atualizado com sucesso!")
        

        # Buscar e exibir o usuário atualizado
        usuario = buscar_usuario_por_seq1(seq)
        
 
        # Converte lista de tuplas em DataFrame
        df_usuario = pd.DataFrame(usuario, columns=["Seq", "Login",  "Mês", "Ano", "Pago_SN", "ValorPago"])

        df_usuario["ValorPago"] = df_usuario["ValorPago"].apply(
            lambda x: locale.currency(x, grouping=True) if pd.notnull(x) and isinstance(x, (int, float)) else "R$ 0,00"
        )

        # Remove o índice completamente
        st.dataframe(df_usuario.reset_index(drop=True), use_container_width=True)

        # Exibe o DataFrame
        st.dataframe(df_usuario, use_container_width=True)

    else:
        st.warning("")


        
        
