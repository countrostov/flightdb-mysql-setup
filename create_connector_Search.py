import mysql.connector
from mysql.connector import Error
from Connector_Close import *
from Search_query import *
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
query = ("SELECT f.flight_id, f.from_destination, f.to_destination , f.travel_time , f.cost  ,"
         "fs.start_date, fs.reaching_date "
         "FROM flight f , flight_schedule fs "
         "WHERE  f.flight_id = fs.flight_id and "
         "f.from_destination=%s and  f.to_destination= %s and fs.start_date=%s "
         )
query_data = ['Bengaluru','frankfurt', ' 2023-11-3']
search_query(cursor, connection , database,query, query_data)

connection_close(cursor, connection)