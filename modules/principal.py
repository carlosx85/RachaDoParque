import streamlit as st


 
def show():
    Receita = 350.00
    Despesa = 150.00
    Saldo = Receita - Despesa
    

 
    b, c, d = st.columns(3)
    b.metric("💰 Saldo",          f"R$ {Saldo:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") , border=True)
    c.metric("📈 Receita",        f"R$ {Receita:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") , border=True)
    d.metric("📉 DespesaDespesa", f"R$ {Despesa:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") , border=True)
    
    
    
    
