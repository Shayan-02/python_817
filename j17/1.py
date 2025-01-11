import sqlite3
connection = sqlite3.connect("./my-database.db")
cursor = connection.cursor()
sql = """
 CREATE TABLE IF NOT EXISTS user (
 userId INTEGER ,
 name VARCHAR (60),
 family VARCHAR (60),
 email VARCHAR (60)
 );
"""
sql2 = """
 CREATE TABLE IF NOT EXISTS seller (
 sellerId INTEGER ,
 sellername VARCHAR (60),
 sellerfamily VARCHAR (60),
 selleremail VARCHAR (60)
 );
"""
cursor.execute(sql)
cursor.execute(sql2)
connection.commit()
connection.close()
