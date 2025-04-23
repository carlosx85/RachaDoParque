import streamlit as st
import pandas as pd
from database import buscar_cliente_por_id
 

# Simula uma função de buscar cliente (verifique se sua função de busca está funcionando corretamente)
def buscar_cliente_por_id(cliente_id):
    # Simulando uma função de busca, substitua isso pela sua função real
    return {"Nome": "João Silva", "Status": "Ativo", "ValorPago": 100.0}  # Exemplo

query_params = st.query_params
cliente_id = query_params.get("id")

if cliente_id:
    cliente = buscar_cliente_por_id(cliente_id)
    if cliente:
        st.write(f"Editando dados do cliente: {cliente['Nome']}")
    else:
        st.error("Cliente não encontrado.")
else:
    st.warning("Nenhum cliente selecionado.")
