import sqlite3

con = sqlite3.connect("test.db")

cur = con.cursor()
cur.execute("DROP TABLE temperature")

con.close