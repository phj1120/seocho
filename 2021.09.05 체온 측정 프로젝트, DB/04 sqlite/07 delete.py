import sqlite3

con = sqlite3.connect("test.db")

cur = con.cursor()
sql = """DELETE FROM temperature
WHERE id = ?
"""

cur.execute(sql, (1, ))
con.commit()

con.close