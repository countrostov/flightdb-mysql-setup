import mysql.connector
from mysql.connector import Error
from Connector_Close import *
from book_flight import *
from Search_query import *
from flight_booking_query import *
from Create_Tables import *
from execute_sql_command import *
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

insert_data = ('2', '1000000002','N','5')
book_flight(cursor, connection , database,insert_data)

connection_close(cursor, connection)