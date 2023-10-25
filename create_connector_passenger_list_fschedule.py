import mysql.connector
from mysql.connector import Error
from Connector_Close import *
from Search_query import *
from Search_query_bookinglist import *
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
query = ("SELECT c.last_name,c.first_name, c.phone_number , b.bid , b.boarding_status , f.from_destination, "
         "f.to_destination , fs.flightschedule_id , fs.flight_id , b.no_of_seats, "
         "fs.start_date , fs.reaching_date "
         "FROM customer c , booking b , flight_schedule fs , flight f "
         "WHERE  fs.flightschedule_id = %s and b.customer = c.phone_number and "
         "b.flightschedule_id = fs.flightschedule_id  "
         "and fs.flight_id = f.flight_id  "
         )
query_data = ['3']
cursor = search_query_bookinglist (cursor, connection , database,query, query_data)
records  = cursor.fetchall()
for row in records:
     print (row)


query = ("SELECT c.last_name,c.first_name, c.cust , cp.bid "
         "FROM copassenger c , copassenger_list cp, flight_schedule fs, booking b "
         "WHERE  b.flightschedule_id = fs.flightschedule_id and fs.flightschedule_id = %s and b.bid = cp.bid "
         "and cp.dep_id = c.dep_id  "
         )
query_data = ['3']

search_query_bookinglist (cursor, connection , database,query, query_data)
records  = cursor.fetchall()
for row in records:
     print (row)

connection_close(cursor, connection)