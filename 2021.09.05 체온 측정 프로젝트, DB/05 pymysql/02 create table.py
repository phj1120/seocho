import pymysql

con = pymysql.connect(
    user="seocho",
    #passwd="노션 참고",
    host="jeongps.com",
    port=3306,
    db="seocho",
    charset="utf8"
)

cur = con.cursor(pymysql.cursors.DictCursor)
sql = """
CREATE TABLE IF NOT EXISTS `TB_hj` (
`ID` INT(11) PRIMARY KEY AUTO_INCREMENT,
`TEMPERATURE` VARCHAR(10) NOT NULL,
`STATUS` VARCHAR(10) NOT NULL,
`DATETIME` VARCHAR(14) NOT NULL
);
"""
cur.execute(sql)
con.commit()
con.close()