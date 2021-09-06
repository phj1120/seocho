import pymysql

con = pymysql.connect(
    user="seocho",
    #passwd="노션 참고",
    host="jeongps.com",
    port=3306,
    db="seocho",
    charset="utf8"
)

con.close()