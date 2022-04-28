import sqlite3

conn = sqlite3.connect('one.db')
cursor = conn.cursor()

sql = "SELECT * FROM purchase"
cursor.execute(sql)
# SQL実行結果を全て取得して表示する
print(cursor.fetchall())

conn.commit()
conn.close()
