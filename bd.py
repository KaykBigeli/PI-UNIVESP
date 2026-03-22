import mysql.connector

try:
    db = mysql.connector.connect(
        host="localhost",
        user="4dm1n",
        password="4dm1ndb",
        database="pi_univesp"
    )
    
    print("Sucesso! Python e MySQL estão conversando.")
    
    cursor = db.cursor()
    cursor.execute("SELECT DATABASE();")
    linha = cursor.fetchone()
    print(f"Conectado ao banco: {linha[0]}")

except Exception as e:
    print(f"Algo deu errado: {e}")

def adicionar_tarefa(titulo):
    try:
        conexao = mysql.connector.connect(host="localhost", user="root", password="", database="pi_univesp")
        cursor = conexao.cursor()
        
        sql = "INSERT INTO tarefas (titulo, concluido) VALUES (%s, %s)"
        valores = (titulo, 0) #
        
        cursor.execute(sql, valores)
        conexao.commit()
        print(f"Sucesso! Tarefa '{titulo}' adicionada.")
        
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        conexao.close()

nome_tarefa = input("O que você precisa fazer? ")
adicionar_tarefa(nome_tarefa)

