import mysql.connector
import streamlit as st
import pandas as pd


def conectar():
    return mysql.connector.connect(
        host="mysql4.iphotel.com.br",       # ou IP do servidor
        user="umotimoempreen02",
        password="82es44fa2A!",
        database="umotimoempreen02"
    )
   
 
       
 
            
            

def validar_login(usuario, senha):
    conexao = conectar()
    cursor = conexao.cursor(buffered=True)  # <-- corrigido aqui
    consulta = "SELECT * FROM Racha_Usuario WHERE Login = %s AND Senha = %s"
    cursor.execute(consulta, (usuario, senha))
    resultado = cursor.fetchone()
    cursor.close()
    conexao.close()
    return resultado is not None



    
def inserir_cliente(nome,Login,ddd,telefone,StatusdePagamento):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        query = "INSERT INTO Racha_Usuario (Nome,Login,DDD,Telefone,StatusdePagamento) VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(query, (nome,Login,ddd,telefone,StatusdePagamento))
        conexao.commit()
        cliente_id = cursor.lastrowid  # 👈 captura o ID gerado
        cursor.close()
        conexao.close()
        return cliente_id
    except Exception as e:
        print("Erro ao inserir cliente:", e)
        return None

    

def buscar_cliente_por_id(cliente_id):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        query = "SELECT Seq, Nome FROM Racha_Usuario WHERE Seq = %s"
        cursor.execute(query, (cliente_id,))
        cliente = cursor.fetchone()
        cursor.close()
        conexao.close()
        return cliente
    except Exception as e:
        print("Erro ao buscar cliente:", e)
        return None


def atualizar_cliente(cliente_id, novo_nome):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        query = "UPDATE clientes SET nome = %s WHERE id = %s"
        cursor.execute(query, (novo_nome, cliente_id))
        conexao.commit()
        cursor.close()
        conexao.close()
        return True
    except Exception as e:
        print("Erro ao atualizar cliente:", e)
        return False
    
    
def buscar_todos_clientes():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        query = "SELECT seq, nome FROM Racha_Usuario ORDER BY Seq DESC"  # Lista do mais recente para o mais antigo
        cursor.execute(query)
        clientes = cursor.fetchall()
        cursor.close()
        conexao.close()
        return clientes
    except Exception as e:
        print("Erro ao buscar clientes:", e)
        return []
    
    
        
def inserir_racha_financeiro(id_cliente):
    conexao = conectar()
    cursor = conexao.cursor()

    # Executar o insert com select
    query = """
    INSERT INTO Racha_Financeiro (Seq, IDP, Ano, Mes, MesAbrev, MesCompl)
    SELECT Seq, IDP, Ano, Mes, MesAbrev, MesCompl
    FROM Racha_Financeiro_Incluir
    WHERE Seq = %s
    """
    cursor.execute(query, (id_cliente,))
    conexao.commit()

    cursor.close()
    conexao.close()
    
    
        
# database.py

def buscar_clientes_por_periodo(ano, mes):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    query = """
        SELECT *  FROM Racha_Financeiro_Geral WHERE Ano = %s AND Mes = %s order by Login
        
    """
    cursor.execute(query, (ano, mes))
    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()
    return resultados



def buscar_logins():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT DISTINCT Seq, Login, Nome FROM Racha_Financeiro_Geral ORDER BY Seq, Login, Nome;")
    logins = cursor.fetchall()  # Agora pega Seq, Login e Nome juntos
    cursor.close()
    conexao.close()
    return logins  # Lista de tuplas (Seq, Login, Nome)




# Buscar dados por login
def buscar_por_login(login):
    conexao = conectar()
    query = """
        SELECT Seq, Nome, Login  
        FROM Racha_Usuario 
        WHERE Login = %s ;
    """
    df = pd.read_sql(query, conexao, params=(login,))
    conexao.close()
    return df


# Buscar meses distintos
def buscar_meses():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT DISTINCT Mes FROM Racha_Financeiro ORDER BY Mes;")
    meses = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conexao.close()
    return meses

# Buscar anos distintos
def buscar_anos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT DISTINCT Ano FROM Racha_Financeiro ORDER BY Ano Asc;")
    anos = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conexao.close()
    return anos

# Buscar dados filtrando por login, mes e ano
def buscar_dados_filtrados(login):
    conexao = conectar()
    query = """
        SELECT Seq, Nome, Login, Mes, Ano, , mes, anoValor 
        FROM Racha_Financeiro 
        WHERE Login = %s AND Mes = %s AND Ano = %s
        ORDER BY Ano DESC, Mes DESC;
    """
    df = pd.read_sql(query, conexao, params=(login, mes, ano))
    conexao.close()
    return df

def atualizar_pagamentk(cliente_id, mes, ano):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        query = "UPDATE clientes SET nome = %s WHERE id = %s"
        cursor.execute(query, (novo_nome, cliente_id))
        conexao.commit()
        cursor.close()
        conexao.close()
        return True
    except Exception as e:
        print("Erro ao atualizar cliente:", e)
        return False
    
    
    
def atualizar_valor(seq, mes, ano, valor,tipo):
    # Garantir que os valores não sejam listas
    seq = int(seq[0]) if isinstance(seq, list) else int(seq)
    mes = int(mes[0]) if isinstance(mes, list) else int(mes)
    ano = int(ano[0]) if isinstance(ano, list) else int(ano)
    valor = int(valor[0]) if isinstance(valor, list) else int(valor)
    tipo =tipo

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE Racha_Financeiro
        SET ValorPago = %s, PAgo_Sn =%s, Data_Cad = now()
        WHERE Seq = %s AND Mes = %s AND Ano = %s;
    """, (valor, tipo, seq, mes, ano))

    conexao.commit()
    cursor.close()
    conexao.close()


def buscar_usuario_por_seq(seq):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT Seq, Login, Nome, Mes, Ano, ValorPago
        FROM Racha_Financeiro_Geral
        WHERE Seq = %s 
        Order by Data_Cad desc, Ano Asc, Mes Asc;
    """, (seq,))
    dados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return dados

def buscar_usuario_por_seq1(seq):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT Seq, Login, Mes, Ano, Pago_SN, ValorPago
        FROM Racha_Financeiro_Geral
        WHERE Seq = %s 
        Order by Data_Cad desc, Ano Asc, Mes Asc;
    """, (seq,))
    dados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return dados

    
    
 

      

def atualizar_valor_despesa(mes, ano, tipoDespesa, descricao, valor):
    try:
        mes = int(mes[0]) if isinstance(mes, list) else int(mes)
        ano = int(ano[0]) if isinstance(ano, list) else int(ano)
        tipoDespesa = tipoDespesa
        descricao   = descricao
        valor = int(valor[0]) if isinstance(valor, list) else int(valor)
        conexao = conectar()
        cursor = conexao.cursor()
        query = "INSERT INTO Racha_Despesa (Data_cad, mes, ano, tipoDespesa, descricao, valor) VALUES (now(),%s,%s,%s,%s,%s)"
        cursor.execute(query, (mes, ano, tipoDespesa, descricao, valor))
        conexao.commit()
        cliente_id = cursor.lastrowid  # 👈 captura o ID gerado
        cursor.close()
        conexao.close()
        return cliente_id
    except Exception as e:
        print("Erro ao inserir cliente:", e)
        return None




def listarpagamento():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT  Mes, Ano, Valor, tipoDespesa, descricao
        FROM Racha_Despesa        
        Order by Data_Cad desc ;
    """, ())
    dados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return dados

