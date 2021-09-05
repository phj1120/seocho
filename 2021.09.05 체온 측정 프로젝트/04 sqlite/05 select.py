# fetchall 모두 로드
# fetchmany 정해준 개수 만큼 로드
# fetchone 하나만 로드


import sqlite3

con = sqlite3.connect("test.db")
cur = con.cursor()

cur.execute("SELECT * FROM temperature")
rows = cur.fetchall()

for row in rows:
	print(row)
con.close()