import mysql.connector
from mysql.connector import Error
from Connector_Close import *
from Search_query import *
from flight_booking_query import *
from Create_Tables import *
from execute_sql_command import *
from insert_query import *
from delete_booking import *

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
query = ("DELETE FROM booking "
        "WHERE bid = %s "
        )
delete_data = ['2' ]
insert_query(cursor, connection , database,query, delete_data)

# query = ("DELETE FROM copassenger_list "
#         "WHERE bid = %s "
#         )
# delete_data = ['2' ]
#
# insert_query(cursor, connection , database,query, delete_data)

connection_close(cursor, connection)