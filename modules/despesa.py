import streamlit as st
from database import buscar_logins,buscar_anos,buscar_meses,buscar_logins,atualizar_valor_despesa,listarpagamento
from datetime import datetime
import pandas as pd
 
st.subheader("Financeiro")
 
def show():
    
    # Pegar mês e ano atual
    mes_atual = datetime.now().month
    ano_atual = datetime.now().year

    # Listas de opções
    meses = list(range(1, 13))
    anos = list(range(2025, 2031))
    
    # Carregar opções 
    meses = buscar_meses()
    anos = buscar_anos()
 

    
            
    
    # Formata" ",r as opções para exibição
    opcoes =  [ " ","Lavagem dos Coletes", "Compra de Bola", "Compra de Coletes", "Material de Farmácia"]
    # Criar o selectbox
    selecionado = st.selectbox("Selecione o Jogador:", opcoes)

    # Recuperar os dados reais com base na seleção
    tipoDespesa =  (selecionado)
   

    # Criar colunas para mês e ano
    col1, col2, _ = st.columns([2, 4, 6])
    with col1:
        mes = st.selectbox("Mês", meses, index=meses.index(mes_atual))
    with col2:
        if ano_atual in anos:
            ano = st.selectbox("Ano", anos, index=anos.index(ano_atual))
        else:
            ano = st.selectbox("Ano", anos)

    # Input do valor
    valor = st.number_input("Digite o Valor da Despesa  :", min_value=0.0)
    
    descricao = st.text_input("Descrição", max_chars=100)

    if st.button("Efetuar o pagamento"):
        atualizar_valor_despesa(mes, ano, tipoDespesa, descricao , valor)
        st.success("✅ Pagamento efetuado com sucesso!")
        
        usuario = listarpagamento() 
 
        # Converte lista de tuplas em DataFrame
        df_usuario = pd.DataFrame( usuario,columns=["Mes", "Ano","Valor", "tipodespesa","Descricao"])

        # Formata ValorPago como moeda brasileira
        df_usuario["Valor"] = df_usuario["Valor"].apply(
            lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        )

        # Remove o índice completamente
        st.dataframe(df_usuario.reset_index(drop=True), use_container_width=True)

 

        

 
 
         
