import streamlit as st


Receita = 350
Despesa = 150

Saldo= Receita - Despesa

def show():
    st.subheader("Resumo Geral")    
    
    col1, col2 = st.columns(2)

    with col1:  
        st.write("Receita",f"{Receita}")
        st.write("Despesa",f"{Despesa}")


    with col2:
        st.write("Produção - 12/2022",f"{Saldo}")
  


    
    
    
    
