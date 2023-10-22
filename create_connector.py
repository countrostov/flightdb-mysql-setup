import mysql.connector
from mysql.connector import Error
from Connector_Close import *
from Create_Tables import *
from execute_sql_command import *

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
query = {}
query['customer'] = (
        "CREATE TABLE `customer` ("
        "  `phone_number` INT(255) NOT NULL,"
        "  `first_name` varchar(14) NOT NULL,"
        "  `last_name` varchar(16) NOT NULL,"
        "  `birth_date` date NOT NULL,"
        "  `gender` enum('M','F') NOT NULL,"
        "  `house_number` SMALLINT(255) NOT NULL,"
        "  `street` varchar(14) NOT NULL,"
        "  `city` varchar(14) NOT NULL,"
        "  `emergency_contact` INT(255) NOT NULL,"
        "  PRIMARY KEY (`phone_number`)"
        ") ")
execute_sql_command (cursor , database, query)
connection_close(cursor, connection)