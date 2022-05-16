import sqlite3
dbpath = 'multi.db'
conn = sqlite3.connect(dbpath)
cursor = conn.cursor()

sql= "CREATE TABLE  if not exists user (id TEXT, sex TEXT, age INTEGER)"
cursor.execute(sql)
sql= """
INSERT INTO
  user ("id", "sex", "age")
VALUES
  ('uid01', '男性', '19'),
  ('uid02', '女性', '35'),
  ('uid03', '男性', '57'),
  ('uid04', '女性', '22'),
  ('uid05', '男性', '31'),
  ('uid06', '女性', '32')
"""
cursor.execute(sql)

conn.commit()
conn.close()
