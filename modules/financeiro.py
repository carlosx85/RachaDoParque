import streamlit as st
import pandas as pd
from database import buscar_clientes_por_periodo,resumodespesa,resumoreceita,resumodespesames,resumoreceitames
from datetime import datetime
 

   
    
# Cache para listas fixas

def carregar_meses():
    return list(range(1, 13))


def carregar_anos():
    return list(range(2025, 2031))

# Formatação de moeda
def formatar_moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def show():
    
    
    
    st.subheader("Financeiro")
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
            <img src="https://boladecapotao.com/img/Racha_Logo_P.png" width="50" style="margin-right: 13px;">
            <h5 style="margin: 0;">RDP Financeiro ({mes}/{ano})</h5> 
        
        </div>
        """
        st.markdown(header_html, unsafe_allow_html=True)       
              
        
       

        receitames = resumoreceitames(mes,ano)
        totalrecmes = receitames[0] if receitames and receitames[0] is not None else 0
        despesames = resumodespesames(mes,ano)
        totaldespmes = despesames[0] if despesames and despesames[0] is not None else 0          
        saldomes= totalrecmes - totaldespmes
        
        
         
         
        
        
        
        
        receita = resumoreceita()
        totalx = receita[0] if receita and receita[0] is not None else 0
        despesa = resumodespesa()
        total = despesa[0] if despesa and despesa[0] is not None else 0
        saldo = totalx - total 
        
        
        
        
                

  
        st.markdown("""
            <style>
            div[data-testid="column"] {
                width: auto !important;
                flex: none !important;
                margin-right: 1px !important;
                padding: 1px !important;
            }
            div[data-testid="stHorizontalBlock"] {
                gap: 1px !important;
            }
            </style>
        """, unsafe_allow_html=True)


        # Agora coloca os badges
        col1, col2, col3 = st.columns(3)

        with col1:
            st.badge(
                f"Saldsso: R$ {saldomes:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
                icon=":material/check:",
                color="green",
                
                
                
            )

        with col2:
            st.badge(
                f"Receita: R$ {totalrecmes:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
                icon=":material/trending_up:",
                color="blue"
            )

        with col3:
            st.badge(
                f"Despesa R$ {totaldespmes:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
                icon=":material/trending_down:",
                color="red"
            )

                
                
                    

        
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
                    <div style="font-size: 12px;">
                        <b>{i}. {login} ({status})</b> {situacao} {formatar_moeda(valor)} {obs_str}
                    </div>
                """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Erro ao buscar dados: {e}")
