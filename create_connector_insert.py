import mysql.connector
from mysql.connector import Error
from Connector_Close import *
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
#flight_manager
# emp_id = cursor.lastrowid
# query = ("INSERT INTO flight_manager "
#                 "(emp_id, first_name, last_name, airline , designation, phone_number) "
#                 "VALUES (%s, %s, %s, %s, %s, %s)")
# insert_data = (emp_id, 'san', 'sri', 'Lufthansa', 'flight_manager', '1000000002')

#flight
# query = ("INSERT INTO flight "
#          "(flight_id, from_destination, to_destination, seat_capacity, travel_time, cost, emp_id) "
#          "VALUES (%s, %s, %s, %s, %s, %s, %s)")
# insert_data = ('LH102', 'Bengaluru', 'Amsterdam', '300', '18', '53000', '5')

# #flight_schedule
# flightschedule_id = cursor.lastrowid
# query = ("INSERT INTO flight_schedule "
#          "(flightschedule_id ,start_date, reaching_date,flight_id) "
#          "VALUES (%s, %s, %s, %s)")
# insert_data = (flightschedule_id, '2023-11-3', '2023-11-4','LH102')

# #Customer
# query = ("INSERT INTO customer "
#          "(phone_number ,first_name,last_name, birth_date, gender ,house_number, street, city,emergency_contact) "
#          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
# insert_data = ('1000000001', 'san', 'sri','2000-10-15', 'M', '12', ' 21 st street' , ' Bengaluru' , '1100000001')

# #copassenger
# dep_id = cursor.lastrowid
# query = ("INSERT INTO copassenger "
#          "(dep_id ,first_name,last_name, emergency_contact, cust) "
#          "VALUES (%s, %s, %s, %s, %s)")
# insert_data = (dep_id, 'san', 'tha', '1100000011', '1000000001')


insert_query(cursor, connection , database,query , insert_data)
connection_close(cursor, connection)