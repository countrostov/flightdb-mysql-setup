import mysql.connector
from mysql.connector import Error
from Connector_Close import *
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
#bid = cursor.lastrowid
query = ("INSERT INTO copassenger_list "
        "(bid ,dep_id ) "
        "VALUES (%s, %s)")
insert_data = ('3', '3' )

insert_query(cursor, connection , database,query, insert_data)

connection_close(cursor, connection)