import streamlit as st
from database import buscar_logins, buscar_anos, buscar_meses, atualizar_valor, buscar_usuario_por_seq1
from datetime import datetime
import pandas as pd

st.subheader("Financeiro")

# Aplicar cache nas funções que trazem dados fixos
@st.cache_data
def get_meses():
    return buscar_meses()

@st.cache_data
def get_anos():
    return buscar_anos()

@st.cache_data
def get_logins():
    return buscar_logins()

def show():
    mes_atual = datetime.now().month
    ano_atual = datetime.now().year

    # Usar versões em cache
    meses = get_meses()
    anos = get_anos()
    dados_logins = get_logins()
    
    
    @st.cache_data
    def get_logins():
        return buscar_logins()

    dados_logins = get_logins()

    if not dados_logins:
        st.warning("⚠️ Nenhum login encontrado.")
    else:
        # Garante estrutura correta
        try:
            opcoes = [f"{login} ({nome} - {seq})" for seq, login, nome in dados_logins]
            selecionado = st.selectbox("Selecione o Jogador:", opcoes)
        except Exception as e:
            st.error(f"Erro ao montar lista: {e}")
            st.write("Dados brutos:", dados_logins)

 
    indice = opcoes.index(selecionado)
    seq, login_real, nome = dados_logins[indice]

    col1, col2, _ = st.columns([2, 4, 6])
    with col1:
        mes = st.selectbox("Mês", meses, index=meses.index(mes_atual))
    with col2:
        ano = st.selectbox("Ano", anos, index=anos.index(ano_atual) if ano_atual in anos else 0)

    tipopagamento = [" ", "Pago", "Em Negociacao"]
    tipo = st.selectbox("Selecione o Status do Pagamento:", tipopagamento)

    valor = st.number_input("Digite o Valor (exato):", min_value=0.0)

    if st.button("Efetuar o pagamento"):
        atualizar_valor(seq, mes, ano, valor, tipo)
        st.success("✅ Pagamento atualizado com sucesso!")

        usuario = buscar_usuario_por_seq1(seq)
        df_usuario = pd.DataFrame(usuario, columns=["Seq", "Login", "Mês", "Ano", "Pago_SN", "ValorPago"])

        df_usuario["ValorPago"] = df_usuario["ValorPago"].apply(
            lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") if pd.notnull(x) else "R$ 0,00"
        )

        st.dataframe(df_usuario.reset_index(drop=True), use_container_width=True)
