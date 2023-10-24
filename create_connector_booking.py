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

# #copassenger
# dep_id = cursor.lastrowid
# query = ("INSERT INTO copassenger "
#          "(dep_id ,first_name,last_name, emergency_contact, cust) "
#          "VALUES (%s, %s, %s, %s, %s)")
# insert_data = (dep_id, 'san', 'tha', '1100000011', '1000000001')

database = 'flightDB1'
bid = cursor.lastrowid
query = ("INSERT INTO booking "
        "(bid ,no_of_seats, customer, boarding_status,flightschedule_id ) "
        "VALUES (%s, %s, %s, %s, %s)")
insert_data = (bid, '2', '1000000002','N','3')

flight_booking_query(cursor, connection , database,query, insert_data)

connection_close(cursor, connection)