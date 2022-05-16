import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('multi.db')
cursor = conn.cursor()

f = open("execute.sql", "r")
sql = f.read()
cursor.execute(sql)
# カラム名を表示
for desc in cursor.description:
    print(desc[0])
# SQL実行結果を全て取得し、行ごとに表示
results = cursor.fetchall()
for row in results:
    print(row)

conn.commit()
conn.close()

# グラフ表示
x = []
y1 = []
y2 = []
for row in results:
    x.append(row[0])
    y1.append(row[1])
    y2.append(row[2])

fig, ax = plt.subplots()
ax.plot(x, y1)
ax.plot(x, y2)
plt.show()
