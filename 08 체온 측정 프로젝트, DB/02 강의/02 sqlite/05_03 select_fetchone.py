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
WHERE id = ? AND status = ?
"""

cur.execute(sql,(2, "EMERGENCEY"))
row = cur.fetchone()

print(row)
con.close()