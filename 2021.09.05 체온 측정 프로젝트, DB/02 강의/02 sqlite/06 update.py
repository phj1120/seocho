import sqlite3

con = sqlite3.connect("test.db")
cur = con.cursor()
sql = """
UPDATE temperature SET
temperature = ?, status = ?
WHERE id == ?
"""
cur.execute(sql, ("38", "EMERGENCEY", 2))

con.commit()
con.close