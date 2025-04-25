import streamlit as st
from database import resumodespesa,resumoreceita
 
def show():
    
    despesa = resumodespesa()
    total = despesa[0] if despesa and despesa[0] is not None else 0
    st.write(f"Total de despesas: R$ {total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    
    receita = resumoreceita()
    totalx = receita[0] if receita and receita[0] is not None else 0
    st.write(f"Total de despesas: R$ {totalx:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    
 
    saldo = totalx - total
     
    st.subheader("Situação do Financeiro ✍🏻", divider=True)
  
    def formatar(valor):
        return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


    # Define cor visual com truque de delta
    if saldo > 0:
        delta = "+1"
        cor_saldo = "normal"   # Verde
    elif saldo < 0:
        delta = "-1"
        cor_saldo = "inverse"  # Vermelho
    else:
        delta = "0"
        cor_saldo = "off"      # Cinza

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("💰 Saldo", formatar(saldo), delta=delta, delta_color=cor_saldo, border=True)

    with col2:
        st.metric("📈 Receita",  formatar(totalx), delta=delta, delta_color=cor_saldo, border=True)

    with col3:
        st.metric("📉 Despesa", formatar(total), delta=delta, delta_color=cor_saldo, border=True)
        
    

