from datetime import *
import pymysql

user = input("which user would you like to spam? ")

#try connect_to_server():
conn = pymysql.connect(host="192.168.4.108",
                       port=3306,
                       user="root",
                       passwd="Ethernet.1",
                       db="poef")

input1 = input("What is your name? ")
input2 = input("What is your email? ")
input3 = input("What is your password? ")

try:
    with conn.cursor() as cur:
        sql = ("inset into 'users' ('name', 'email', 'password') values (%s, %s, %s)")



        cur.execute(sql, ('derpster', 'jim', 'bob'))
    connection.commit()
        #print(cur.description)

        for row in cur:
             print(row)

finally:
cur.close()
conn.close()