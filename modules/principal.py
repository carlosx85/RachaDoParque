import streamlit as st

def show():
    st.subheader("Resumo Geral")
    st.write("Aqui vai o formulário de cadastro.")
    
    
    
    col1, col2 = st.columns(2)

    with col1:  
        st.header("Produção - 12/2022")


    with col2:
        st.header("Produção - 12/2022")
        st.metric("",f"{2,2:}", "")  


    
    
    
    
