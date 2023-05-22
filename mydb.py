import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root@123',

)

#create a cursor object

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE ashborne")

print("All Done")