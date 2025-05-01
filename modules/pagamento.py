import streamlit as st
import pandas as pd
from datetime import datetime
from database import (
    buscar_logins,
    buscar_anos,
    buscar_meses,
    atualizar_valor,
    buscar_usuario_por_seq1
)

st.subheader("Financeiro")

def get_logins():
    return buscar_logins()


def show():
    mes_atual = datetime.now().month
    ano_atual = datetime.now().year

    meses = buscar_meses()
    anos = buscar_anos()
    
    dados_logins = get_logins()

    if not dados_logins:
        st.warning("⚠️ Nenhum jogador encontrado.")
        return

    try:
        opcoes = [f"{login} ({nome} - {seq})" for seq, login, nome in dados_logins]
        selecionado = st.selectbox("Selecione o Jogador:", opcoes)

        indice = opcoes.index(selecionado)
        seq, login_real, nome = dados_logins[indice]
    except Exception as e:
        st.error("Erro ao carregar jogadores.")
        st.exception(e)
        return

 

    # Layout com colunas
    col1, col2, _ = st.columns([2, 4, 6])
    with col1:
        mes_str = st.selectbox("Mês", meses, index=meses.index(mes_atual) if mes_atual in meses else 0)
        mes = int(mes_str)  # converte para inteiro, se necessário
    with col2:
        ano_str = st.selectbox("Ano", anos, index=anos.index(ano_atual) if ano_atual in anos else 0)
        ano = int(ano_str)  # converte para inteiro, se necessário



    tipopagamento = ["Pago", "Em Negociacao"]
    
    tipo = st.selectbox("Selecione o Status do Pagamento:", tipopagamento)

    obs = st.text_input("Obs", max_chars=100)
    
    valor = st.number_input("Digite o valor do pagamento:", min_value=0, step=1, format="%d" , value=15)
    
   

    if st.button("Efetuar o pagamento"):
        st.cache_data.clear()      
        atualizar_valor(seq, mes, ano, valor, tipo, obs)
        st.success(f"✅ Pagamento atualizado com sucesso!")

        usuario = buscar_usuario_por_seq1(seq)
        df_usuario = pd.DataFrame(usuario, columns=["Seq", "Login", "Mês", "Ano", "Pago_SN", "ValorPago"])

        df_usuario["ValorPago"] = df_usuario["ValorPago"].apply(
            lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            if pd.notnull(x) else "R$ 0,00"
        )

        st.dataframe(df_usuario.reset_index(drop=True), use_container_width=True)
