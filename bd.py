import mysql.connector

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pi_univesp"
    )
    
    print("Sucesso! Python e MySQL estão conversando.")
    
    cursor = db.cursor()
    cursor.execute("SELECT DATABASE();")
    linha = cursor.fetchone()
    print(f"Conectado ao banco: {linha[0]}")

except Exception as e:
    print(f"Algo deu errado: {e}")