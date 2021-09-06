#fetchall
#fetchmany
#fetchone

import sqlite3

con = sqlite3.connect("test.db")
cur = con.cursor()

#cur.execute("SELECT * FROM temperature")
#cur.execute("SELECT id, temperature FROM temperature")
sql = """
SELECT * FROM temperature
"""
cur.execute(sql)
rows = cur.fetchmany(3)
for row in rows:
    print(row)

con.close()