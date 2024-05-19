import sqlite3

connection_string=sqlite3.connect("users.db")
cursor=connection_string.cursor()

#create table

create_table="CREATE TABLE IF NOT EXISTS user(name TEXT, password TEXT, age INTEGER)"
cursor.execute(create_table)

#insert data
# cursor.execute("INSERT INTO user VALUES ('SAKIB', 'open1', 35)")
# cursor.execute("INSERT INTO user VALUES ('TAMIM', 'open2', 40)")
# cursor.execute("INSERT INTO user VALUES ('JIHAN', 'open3', 45)")
# cursor.execute("INSERT INTO user VALUES ('SAMIR', 'open4', 50)")
# connection_string.commit()

#delete data
# cursor.execute("DELETE FROM user WHERE name='SAMIR'")
# connection_string.commit()

#update data
cursor.execute("UPDATE user SET age=60 WHERE age=45")
connection_string.commit()
