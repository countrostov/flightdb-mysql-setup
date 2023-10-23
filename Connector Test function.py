import mysql.connector
from mysql.connector import Error
from Connector_Close import *
from Create_Tables import *
from execute_sql_command import *

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='flightDB1',
                                         user='root',
                                         password='flightDB')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)

database = 'flightDB'
#execute_sql_command (cursor , database, query)
create_tables(cursor, database)
connection_close(cursor, connection)
