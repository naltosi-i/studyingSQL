import sqlite3
dbpath = 'multi.db'
conn = sqlite3.connect(dbpath)
cursor = conn.cursor()
sql= "CREATE TABLE  if not exists user_action_log (action_date TEXT , uid TEXT)"
cursor.execute(sql)
sql= """
INSERT INTO
  user_action_log ("action_date", "uid")
VALUES
  ('2021-05-20', 'uid01'),
  ('2021-05-20', 'uid02'),
  ('2021-05-20', 'uid02'),
  ('2021-05-21', 'uid04'),
  ('2021-05-22', 'uid03'),
  ('2021-05-22', 'uid05'),
  ('2021-05-23', 'uid01'),
  ('2021-05-24', 'uid05'),
  ('2021-05-25', 'uid01'),
  ('2021-05-26', 'uid02'),
  ('2021-05-27', 'uid02'),
  ('2021-05-27', 'uid04'),
  ('2021-05-28', 'uid03'),
  ('2021-05-28', 'uid01'),
  ('2021-05-28', 'uid02'),
  ('2021-05-29', 'uid02')
"""
cursor.execute(sql)
conn.commit()
conn.close()
