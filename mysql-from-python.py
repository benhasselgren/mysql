import os
import pymysql

#Get username from cloud9 workspace
#Modify this variable if running on a different environment
username = os.getenv('C9_USER')

#Connect to database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')
                             
try:
    #Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * from Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    #Close the connection, regardless whether the query('ies') above worked
    connection.close()

