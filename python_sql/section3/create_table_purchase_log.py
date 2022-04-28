import sqlite3
dbpath = 'multi.db'
conn = sqlite3.connect(dbpath)
cursor = conn.cursor()

sql= "CREATE TABLE if not exists purchase_log(purchase_date TEXT,product_id TEXT,user_id TEXT,quantity INTEGER)"
cursor.execute(sql)
sql= """
INSERT INTO
  purchase_log ("purchase_date","product_id","user_id","quantity")
VALUES
  ('2021-5-20', '1', 'uid01', '20'),
  ('2021-5-20', '2', 'uid02', '2'),
  ('2021-5-20', '3', 'uid02', '2'),
  ('2021-5-21', '4', 'uid04', '10'),
  ('2021-5-22', '5', 'uid03', '10'),
  ('2021-5-22', '6', 'uid99', '2');
"""
cursor.execute(sql)

conn.commit()
conn.close()
