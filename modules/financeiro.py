import streamlit as st
import pandas as pd
from database import buscar_clientes_por_periodo
from datetime import datetime

# Cache para listas fixas
@st.cache_data
def carregar_meses():
    return list(range(1, 13))

@st.cache_data
def carregar_anos():
    return list(range(2025, 2031))

# Formatação de moeda
def formatar_moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def show():
    mes_atual = datetime.now().month
    ano_atual = datetime.now().year

    # Carregar listas
    meses = carregar_meses()
    anos = carregar_anos()

    # Seleção de período
    col1, col2, _ = st.columns([2, 4, 6])
    with col1:
        mes = st.selectbox("Mês", meses, index=meses.index(mes_atual) if mes_atual in meses else 0)
    with col2:
        ano = st.selectbox("Ano", anos, index=anos.index(ano_atual) if ano_atual in anos else 0)

    if st.button("🔍 Buscar"):
        
        header_html = f"""
        <div style="display: flex; align-items: center; padding: 5px 0 5px 0;">
            <img src="https://boladecapotao.com/img/Racha_Logo_P.png" width="50" style="margin-right: 15px;">
            <h5 style="margin: 0;">Racha do Parque (Financeiro)</h5> 
        
        </div>
        <div style="font-size: 13px;">
        <b>Periodo: {mes}/{ano}</b>    <b>Receita: R$ 250,00      Despesa: R$ 250,00 </b> 
        </div>
        <hr style="margin-top: 5px; margin-bottom: 15px;">
        """
        st.markdown(header_html, unsafe_allow_html=True)       
        
        
        
        
        try:
            dados = buscar_clientes_por_periodo(ano, mes)

            if not dados:
                st.warning("Nenhum dado encontrado.")
                return          
            
           
            

            for i, item in enumerate(dados, start=1):
                seq = item.get("Seq", "—")
                login = item.get("Login", "—")
                obs = item.get("Obs", "—")
                status = item.get("StatusDePagamento", "")
                pago = item.get("Pago_SN", "—")
                valor = item.get("ValorPago") or 0

                situacao = "✅" if pago == "Pago" else "🕓" if pago == "Em Negociacao" else "❌"
 
                obs_str = f"({obs})" if obs not in [None, "None", ""] else ""
                

                
                
                st.markdown(f"""
                    <div style="font-size: 13px;">
                        <b>{i}. {login} ({status})</b> {situacao} {formatar_moeda(valor)} {obs_str}
                    </div>
                """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Erro ao buscar dados: {e}")
