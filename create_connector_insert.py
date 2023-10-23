import mysql.connector
from mysql.connector import Error
from Connector_Close import *
from Create_Tables import *
from execute_sql_command import *
from insert_query import *

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='flightDB',
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
emp_id = cursor.lastrowid
data = (emp_id, 'Count', 'Rostov', 'Air Russia', 'flight_manager', '1000000003')
insert_query(cursor, connection , database, data)
connection_close(cursor, connection)