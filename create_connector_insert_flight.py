import mysql.connector
from mysql.connector import Error
from Connector_Close import *
from insert_flight import *
from insert_query import *

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

database = 'flightDB1'

insert_data = ('LH106', 'Bengaluru', 'Bali', '300', '18', '53000', '5')
insert_data1 = ('2023-11-3', '2023-11-4','LH106')

insert_flight(cursor, connection , database , insert_data , insert_data1 )
connection_close(cursor, connection)