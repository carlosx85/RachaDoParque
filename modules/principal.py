import streamlit as st


 
def show():
    Receita = 350.00
    Despesa = 150.00
    Saldo = Receita - Despesa
    

    # Mostrando como métrica
    st.metric(
        label="💰 Saldo",
        value=f"R$ {Saldo:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
)
    c, d = st.columns(2)
    c.metric("Receita", f"R$ {Receita:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") , border=True)
    d.metric("Despesa", f"R$ {Despesa:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") , border=True)
    
    
    
    
