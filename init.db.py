import sqlite3

connection = sqlite3.connect('database.db')

with open('squema.sql') as f:
    connection.executescript (f.read())

cur=connection.cursor()

cur.execute("INSERT INTO posts (id, created, os, nome, sobrenome, endereço, cep, telefone, email, placa, fabricante, modelo, serviços, dataAgend, horario, dataEntrada, dataEntrega, valorPrevisto, valorRecebido, serviçoRealizado, mensagem) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", ('', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''))

connection.commit()
connection.close()
