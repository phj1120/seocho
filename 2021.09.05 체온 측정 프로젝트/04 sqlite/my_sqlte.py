"""
CREATE TABLE [테이블 명](
    칼럼1 TEXT/INTEGER/NUMBER,
    칼럼2 ,
    칼럼3,
    칼럼4
}

"""

import sqlite3

con = sqlite3.connect("test.db")

con.close()