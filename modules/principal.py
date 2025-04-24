import streamlit as st


 
def show():
    Receita = 350.00
    Despesa = 150.00
    Saldo = Receita - Despesa

    # Exibe valores formatados em reais
    st.write("Receita:", f"R$ {Receita:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") , border=True)
    st.write("Despesa:", f"R$ {Despesa:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") , border=True)
    st.write("Saldo:", f"R$ {Saldo:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") , border=True)

  

    a, b = st.columns(2)
    c, d = st.columns(2)

    a.metric("Temperature", "30°F", "-9°F", border=True)
    b.metric("Wind", "4 mph", "2 mph", border=True)

    c.metric("Humidity", "77%", "5%", border=True)
    d.metric("Pressure", "30.34 inHg", "-2 inHg", border=True)
    
    
    
    
