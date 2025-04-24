import streamlit as st

def show():
    st.subheader("Resumo Geral")    
    
    col1, col2 = st.columns(2)

    with col1:  
        st.write("Produção - 12/2022")


    with col2:
        st.write("Produção - 12/2022",f"{2,2:}")
  


    
    
    
    
