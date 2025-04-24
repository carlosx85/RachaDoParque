import streamlit as st
from database import buscar_logins, buscar_anos, buscar_meses, atualizar_valor, buscar_usuario_por_seq1
from datetime import datetime
import pandas as pd

st.subheader("Financeiro")

# Caches para evitar chamadas repetidas
@st.cache_data
def carregar_meses():
    return buscar_meses()

@st.cache_data
def carregar_anos():
    return buscar_anos()

@st.cache_data
def carregar_logins():
    return buscar_logins()

# Formatação alternativa para moeda (sem locale)
def formatar_moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")


def show():
    mes_atual = datetime.now().month
    ano_atual = datetime.now().year

    # Carregar dados com cache
    meses = carregar_meses()
    anos = carregar_anos()
    dados_logins = carregar_logins()

    # Formatar opções de login
    opcoes = [f"{login} ({nome} - {seq})" for seq, login, nome in dados_logins]
    selecionado = st.selectbox("Selecione o Jogador:", opcoes)

    # Recuperar dados reais da seleção
    indice = opcoes.index(selecionado)
    seq, login_real, nome = dados_logins[indice]

    # Seleção de mês e ano
    col1, col2, _ = st.columns([2, 4, 6])
    with col1:
        mes = st.selectbox("Mês", meses, index=meses.index(mes_atual) if mes_atual in meses else 0)
    with col2:
        ano = st.selectbox("Ano", anos, index=anos.index(ano_atual) if ano_atual in anos else 0)

    tipo = st.selectbox("Selecione o Status do Pagamento:", [" ", "Pago", "Em Negociacao"])

    valor = st.number_input("Digite o Valor (exato):", min_value=0.0)

    if st.button("Efetuar o pagamento"):
        atualizar_valor(seq, mes, ano, valor, tipo)
        st.success("✅ Pagamento atualizado com sucesso!")

        usuario = buscar_usuario_por_seq1(seq)
        df_usuario = pd.DataFrame(usuario, columns=["Seq", "Login", "Mês", "Ano", "Pago_SN", "ValorPago"])
        df_usuario["ValorPago"] = df_usuario["ValorPago"].apply(
            lambda x: formatar_moeda(x) if pd.notnull(x) and isinstance(x, (int, float)) else "R$ 0,00"
        )

        st.dataframe(df_usuario.reset_index(drop=True), use_container_width=True)
