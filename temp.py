import mysql.connector as c

con=c.connect(host="localhost",
              user="root",
              password="root",
              database="student")
cursor=con.cursor()

cursor.execute("show tables from student")

for i in cursor:
    print(i)
