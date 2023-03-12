Varios comandos de excecusao com a linguagem Python.
#matheusdeperon



create table users (
  id int not null auto_increment primary key,
  name varchar(100) not null,
  email varchar(100) not null,
  created datetime not null
);

# -*- encoding: utf-8 -*-

import mysql.connector
import datetime

connection = mysql.connector.connect(
  host="localhost",
  user="usuariobancodados",
  password="senhausuario",
  database="bancodados"
)

cursor = connection.cursor()

sql = "INSERT INTO users (name, email, created) VALUES (%s, %s, %s)"
data = (
  'Primeiro Usuário',
  'primeirousuario@teste.com.br',
  datetime.datetime.today()
)

cursor.execute(sql, data)
connection.commit()

userid = cursor.lastrowid

cursor.close()
connection.close()

print("Foi cadastrado o novo usuário de ID:", userid)

# -*- encoding: utf-8 -*-

import mysql.connector
import datetime

connection = mysql.connector.connect(
  host="localhost",
  user="usuariobancodados",
  password="senhausuario",
  database="bancodados"
)

cursor = connection.cursor()

sql = "SELECT * FROM users"

cursor.execute(sql)
results = cursor.fetchall()

cursor.close()
connection.close()

for result in results:
  print(result)

  # -*- encoding: utf-8 -*-

import mysql.connector
import datetime

connection = mysql.connector.connect(
  host="localhost",
  user="usuariobancodados",
  password="senhausuario",
  database="bancodados"
)

cursor = connection.cursor()

sql = "UPDATE users SET name = %s, email = %s WHERE id = %s"
data = (
  'Primeiro Usuário Editado',
  'primeirousuarioeditado@teste.com.br',
  1
)

cursor.execute(sql, data)
connection.commit()

recordsaffected = cursor.rowcount

cursor.close()
connection.close()

print(recordsaffected, " registros alterados")

# -*- encoding: utf-8 -*-

import mysql.connector
import datetime

connection = mysql.connector.connect(
  host="localhost",
  user="usuariobancodados",
  password="senhausuario",
  database="bancodados"
)

cursor = connection.cursor()

sql = "DELETE FROM users WHERE id = %s"
data = (2,)

cursor.execute(sql, data)
connection.commit()

recordsaffected = cursor.rowcount

cursor.close()
connection.close()

print(recordsaffected, " registros excluídos")

