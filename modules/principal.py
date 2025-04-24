import streamlit as st


 
def show():
    Receita = 350.00
    Despesa = 150.00
    Saldo = Receita - Despesa

    # Exibe valores formatados em reais
    st.write("Receita:", f"R$ {Receita:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") , border=True)
    st.write("Despesa:", f"R$ {Despesa:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") , border=True)
    st.write("Saldo:", f"R$ {Saldo:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") , border=True)

  

    a = st.columns(1)
    c, d = st.columns(1)

    a.metric("Saldo", f"R$ {Saldo:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") , border=True)
    
    c.metric("Receita", f"R$ {Receita:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") , border=True)
    d.metric("Despesa", f"R$ {Despesa:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") , border=True)
    
    
    
    
