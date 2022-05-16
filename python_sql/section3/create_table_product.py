import sqlite3
dbpath = 'multi.db'
conn = sqlite3.connect(dbpath)
cursor = conn.cursor()

sql= "CREATE TABLE product (id TEXT , name TEXT)"
cursor.execute(sql)
sql= """
INSERT INTO "product" ("id", "name") VALUES 
('1', 'マスク'),
('2', 'フェイスシールド'),
('3', 'アルコール液'),
('4', '除菌シート'),
('5', '手袋'),
('6', 'アクリルパーティション')
"""
cursor.execute(sql)

conn.commit()
conn.close()
