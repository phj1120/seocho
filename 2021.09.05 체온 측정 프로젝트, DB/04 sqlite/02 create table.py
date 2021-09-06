"""
	CREATE TABLE temperature(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	temperature TEXT,
  status TEXT
	datetime TEXT,
	칼럼2 타입 키,
	칼럼3,
	칼럼4
)
"""


import sqlite3


con = sqlite3.connect("test.db")
sql = """
	CREATE TABLE IF NOT EXISTS temperature(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	temperature TEXT,
    status TEXT,
	datetime TEXT
)
"""
con.execute(sql)
con.close()

"""
삭제


"""



