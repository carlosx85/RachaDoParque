import streamlit as st
import pandas as pd
from database import buscar_clientes_por_periodo
from datetime import datetime

 

def show():
    
        # Pegar mês e ano atual
    mes_atual = datetime.now().month
    ano_atual = datetime.now().year

    # Listas de opções
    meses = list(range(1, 13))
    anos = list(range(2025, 2031))

    # Criar colunas para mês e ano
    col1, col2, _ = st.columns([2, 4, 6])
    with col1:
        mes = st.selectbox("Mês", meses, index=meses.index(mes_atual))
    with col2:
        if ano_atual in anos:
            ano = st.selectbox("Ano", anos, index=anos.index(ano_atual))
        else:
            ano = st.selectbox("Ano", anos)

    if st.button("🔍 Buscar"):
        try:
            dados = buscar_clientes_por_periodo(ano, mes)
            if not dados:
                st.warning("Nenhum dado encontrado.")
                return

            st.success(f"{len(dados)} registro(s) encontrado(s).")

            for i, item in enumerate(dados, start=1):  # Começa do 1
                Seq = item.get("Seq", "—")
                login = item.get("Login", "—")
                Jogador = item.get("StatusDePagamento", "")
                pago = item.get("Pago_SN", "—")
                valor = item.get("ValorPago") or 0
                situacao = "✅" if pago == "Pago" else "🕓" if pago == "Em Negociacao" else "❌"
             

                            # Exibe a linha com as informações do cliente com font-size 12px
                st.markdown(f"""
                    <div style="font-size: 12px;">
                        <b>{i}. {login} ({Jogador})</b>  {situacao}  R$ {valor:.2f}
                       
                    </div>
                """, unsafe_allow_html=True)


        except Exception as e:
            st.error(f"Erro ao buscar dados: {e}")
