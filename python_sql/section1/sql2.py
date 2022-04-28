import sqlite3

conn = sqlite3.connect('one.db')
cursor = conn.cursor()

f=open("execute.sql","r")
sql=f.read()
cursor.execute(sql)
# SQL実行結果を全て取得して表示する
print(cursor.fetchall())

f.close()
conn.commit()
conn.close()
