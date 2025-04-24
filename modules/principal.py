import streamlit as st


Receita = 350.00
Despesa = 150.00
Saldo = Receita - Despesa

# Exibe valores formatados em reais
st.write("Receita:", f"R$ {Receita:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
st.write("Despesa:", f"R$ {Despesa:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
st.write("Saldo:", f"R$ {Saldo:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))


    
    
    
    
