import sqlite3

conn = sqlite3.connect('one.db')
cursor = conn.cursor()

sql= """
    CREATE TABLE purchase(
        purchase_date TEXT,
        name TEXT,
        quantity INTEGER
    )
"""
cursor.execute(sql)
sql= """
    INSERT INTO
        purchase (
            "purchase_date",
            "name",
            "quantity"
        )
    VALUES
        ('2021/5/18', 'マスク', '20'),
        ('2021/5/18', '石けん', '2'),
        ('2021/5/18', 'アルコール液', '2'),
        ('2021/5/19', '除菌スプレー', '10'),
        ('2021/5/20', '使い捨て手袋', '10'),
        ('2021/5/21', 'ガーゼ', '2');
"""
cursor.execute(sql)

conn.commit()
conn.close()
