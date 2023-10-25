import mysql.connector
from mysql.connector import Error
from Connector_Close import *
from book_flight import *
from Search_query import *
from flight_booking_query import *
from Create_Tables import *
from execute_sql_command import *
from insert_query import *
from insert_flight import *
from insert_flight_schedule import *

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

while (input("Do you want to continue ? (y/n)")=='y'):
    #print ("while loop in action")

    match (int(input ("1:Create flight and flight schedule \n"
                      "2: Search for flights \n"
                      "3: Book flights \n"
                      "4: Cancel a flight \n"
                      "5: Prepare a passenger list \n"
                      "\nEnter your choice : "))):
        case 1:
            match (int(input(print("1: flight creation \n 2: flight schedule creation\n Provide your choice : ")))):
                case 1:

                    print("Insert you data separated by space in this order : flight_id, from_destination, to_destination,"
                          "seat_capacity, travel_time, cost, emp_id: \n")
                    insert_data = tuple(input().split())
                    insert_flight(cursor, connection , database, insert_data)

                case 2:
                    print(
                        "Insert you data separated by space in this order : start_date, reaching_date,flight_id"
                        ": \n")
                    insert_data = tuple(input().split())
                    insert_flight_schedule(cursor, connection, database, insert_data)

        case 2:
            print( "2")
        case 3:
            print( "3")
        case 4:
            print("two")
        case 5:
            print("two")
        case default:
            print( "Enter from 1 to 5 only")





connection_close(cursor, connection)