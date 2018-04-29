import os
import datetime
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
        rows = cursor.execute("DELETE FROM Friends WHERE name = 'bob';")
        connection.commit()
finally:
    #Close the connection, regardless whether the query('ies') above worked
    connection.close()

