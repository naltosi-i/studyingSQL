import sqlite3

conn = sqlite3.connect('one.db')
cursor = conn.cursor()

f=open("execute.sql","r")
sql=f.read()
cursor.execute(sql)
# 列名を表示
for desc in cursor.description:
    print(desc[0]) 
# SQL実行結果を全て取得し、行ごとに表示
results=cursor.fetchall()
for row in results:
    print(row)

f.close()
conn.commit()
conn.close()
