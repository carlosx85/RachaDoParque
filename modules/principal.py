import streamlit as st


 
def show():
    Receita = 350.00
    Despesa = 150.00
    Saldo = Receita - Despesa
    

    # Mostrando como métrica
# Formatação
    def formatar(valor):
        return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    # Definir cor via delta_color
    if Saldo > 0:
        cor_saldo = "normal"  # verde
        delta = "+1"           # qualquer positivo simula verde
    elif Saldo < 0:
        cor_saldo = "inverse"  # vermelho
        delta = "-1"
    else:
        cor_saldo = "off"      # cinza
        delta = "0"

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("💰 Saldo", formatar(Saldo), delta=delta, delta_color=cor_saldo)

    with col2:
        st.metric("📈 Receita", formatar(Receita))

    with col3:
        st.metric("📉 Despesa", formatar(Despesa))



    
