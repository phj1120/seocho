import sqlite3


con = sqlite3.connect("test.db")
cur = con.cursor()
sql = """
INSERT INTO temperature (temperature, status, datetime)
VALUES
(?,?,?)
"""

cur.execute(sql,("36.5", "NORMAL","20210905135535"))
con.commit()

con.close()