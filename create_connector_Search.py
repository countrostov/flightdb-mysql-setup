import mysql.connector
from mysql.connector import Error
from Connector_Close import *
from Search_flight import *
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
query_data = ['Bengaluru','frankfurt', ' 2023-11-3']
cursor = search_flight(cursor, connection , database, query_data)

for (flight_id, from_destination, to_destination , travel_time , cost, start_date, reaching_date ) in cursor:
    print((flight_id, from_destination, to_destination , travel_time , cost, start_date, reaching_date))
connection_close(cursor, connection)