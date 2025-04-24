import streamlit as st


 
 


 
def show():
    Receita = 350.00
    Despesa = 150.00
    Saldo = Receita - Despesa
     
    st.subheader("Situação geral do financeiro ", divider=True)
  

 
    b, c, d = st.columns(3)
    b.metric("💰 Saldo",          f"R$ {Saldo:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") , border=True)
    c.metric("📈 Receita",        f"R$ {Receita:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") , border=True)
    d.metric("📉 DespesaDespesa", f"R$ {Despesa:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") , border=True)
    
    
    

    def formatar(valor):
        return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


    # Define cor visual com truque de delta
    if Saldo > 0:
        delta = "+1"
        cor_saldo = "normal"   # Verde
    elif Saldo < 0:
        delta = "-1"
        cor_saldo = "inverse"  # Vermelho
    else:
        delta = "0"
        cor_saldo = "off"      # Cinza

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📈 Receita", formatar(Receita), border=True)

    with col2:
        st.metric("📉 Despesa", formatar(Despesa), border=True)

    with col3:
        st.metric("💰 Saldo", formatar(Saldo), delta=delta, delta_color=cor_saldo, border=True)

