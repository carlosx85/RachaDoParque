import streamlit as st
from database import  atualizar_valor_despesa, listarpagamento
from datetime import datetime
import pandas as pd

st.subheader("Financeiro")

# Caches para evitar chamadas repetidas ao banco
 
def carregar_meses():
    return list(range(1, 13))
 
def carregar_anos():
    return list(range(2025, 2031))

# Formatação manual de moeda brasileira
def formatar_moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def show():
    mes_atual = datetime.now().month
    ano_atual = datetime.now().year

    # Carregar listas com cache
    meses = carregar_meses()
    anos = carregar_anos()

    # Tipos de despesa
    opcoes = [ "Lavagem dos Coletes", "Compra de Bola", "Compra de Coletes", "Material de Farmácia"]
    tipo_despesa = st.selectbox("Selecione o Tipo de Despesa:", opcoes)

    # Seleção de mês e ano
    col1, col2, _ = st.columns([2, 4, 6])
    with col1:
        mes = st.selectbox("Mês", meses, index=meses.index(mes_atual) if mes_atual in meses else 0)
    with col2:
        ano = st.selectbox("Ano", anos, index=anos.index(ano_atual) if ano_atual in anos else 0)

    # Inputs de valor e descrição
    valor = st.number_input("Digite o Valor da Despesa:",min_value=0, step=1, format="%d")
    descricao = st.text_input("Descrição", max_chars=100)

    if st.button("Efetuar o pagamento"):
        if tipo_despesa.strip() == "":
            st.error("O campo 'Tipo de Despesa' é obrigatório.")
        else:
            atualizar_valor_despesa(mes, ano, tipo_despesa, descricao, valor)
            st.success("✅ Pagamento efetuado com sucesso!")
            
            
 
            
    usuario = listarpagamento() 

    if usuario:
        # Converte lista de tuplas em DataFrame
        df_usuario = pd.DataFrame(usuario, columns=["Mes", "Ano", "Valor", "tipodespesa", "Descricao"])

        # Formata Valor como moeda brasileira
        df_usuario["ValorFormatado"] = df_usuario["Valor"].apply(
            lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        )

        st.write("### Lista de Despesas:")

        # Mostra a lista linha por linha com botões
        for idx, row in df_usuario.iterrows():
            col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 1, 2, 2, 2, 1, 1])

            with col1:
                st.write(row["Mes"])
            with col2:
                st.write(row["Ano"])
            with col3:
                st.write(row["ValorFormatado"])
            with col4:
                st.write(row["tipodespesa"])
            with col5:
                st.write(row["Descricao"])
            with col6:
                if st.button("Alterar", key=f"alterar_{idx}"):
                    st.session_state['pagina'] = 'alterar'
                    st.session_state['despesa_idx'] = idx
                    st.experimental_rerun()
            with col7:
                if st.button("Excluir", key=f"excluir_{idx}"):
                    # Aqui você teria que criar uma função para excluir
                    from database import excluir_despesa
                    excluir_despesa(row["Mes"], row["Ano"], row["tipodespesa"], row["Descricao"])
                    st.success(f"Despesa excluída!")
                    st.experimental_rerun()
    else:
        st.warning("Nenhuma despesa cadastrada ainda.")
