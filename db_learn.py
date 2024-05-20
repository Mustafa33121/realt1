"""CREATE TABLE my_tabl"""


import sqlite3

data = [
    ('Vasiliy',54)
    ('alex',29)
]
#cur.execute("""DELETE FROM my_table WHERE id = 3""")
cur.executemany(f"""INSERT INTO my_table(name,age) VALUES (?, ?)""", data)
conn.commit()
conn = sqlite3.connect('test.db')
cur = conn.cursor()
cur.execute("""SELECT * FROM my_table""")
res = cur.fetchall()

conn.close()
