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
from Search_flight import *
from insert_copassenger import *
from Search_booking import *
from delete_booking import *
from book_flight_copassenger import *

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
            print(
                "SEARCH A FLIGHT FOR THE REQUIRED DATE\n"
                "Insert you data separated by space in this order : from_destination to_destination start_date :\n"
                "Example : Bengaluru Paris 2023-12-10 \n")
            query_data = tuple(input().split())
            search_flight(cursor, connection, database, query_data)
            records = cursor.fetchall()
            for row in records:
                print (row)
        case 3:
            #search for a flight
            print("BOOKING A FLIGHT - SIGN IN TO BOOK A FLIGHT\n")
            customer = input(print("Enter customer phone number : "))
            print(
                "BOOKING A FLIGHT - SEARCH A FLIGHT FOR THE REQUIRED DATE\n"
                "Insert you data separated by space in this order : from_destination to_destination start_date :\n"
                "Example : Bengaluru Paris 2023-12-10 \n")
            query_data = tuple(input().split())
            search_flight(cursor, connection, database, query_data)
            records = cursor.fetchall()
            for row in records:
                print(row)
            #book a flight for customer
            print(
                "BOOKING A FLIGHT \n"
                "Choose from the available flights to book: no_of_seats flightschedule_id  :\n"
                "Example : 2   \n")
            insert_data = (input().split())
            insert_data.insert(1 , customer)
            insert_data.insert(2, 'N')
            insert_data1 = tuple(insert_data)
            book_flight(cursor, connection, database, insert_data1)
            bid  = cursor.lastrowid
            #copassenger booking
            if int(insert_data1[0])>1 :
                for cp in range(int(insert_data[0])-1):
                    print(
                        "Enter details of copassenger "
                        "first_name,last_name, emergency_contact\n"
                        "Example : Kumar Aravind 1000000045   \n")
                    insert_data = (input().split())
                    insert_data.insert(3, customer)
                    insert_data1 = tuple(insert_data)

                    insert_copassenger(cursor, connection, database, insert_data1)

                    depid = cursor.lastrowid
                    insert_data = (bid , depid)
                    book_flight_copassenger(cursor, connection, database, insert_data)


        case 4:
            #cancel a flight booking + copassengers

            print(
                "Cancel a Booking - SEARCH A booking FOR THE CUSTOMER\n"
                "Insert your  phone number : \n"
                "Example : 1000000000 \n")
            query_data = tuple(input().split())
            search_booking(cursor, connection, database, query_data)
            records = cursor.fetchall()
            for row in records:
                print(row)
            # Selecting and cancelling a booking
            print(
                "CANCELLING A BOOKING \n"
                "Choose from the available booking to cancel: \n"
                " bid, no_of_seats, customer , boarding_status , flightschedule_id \n"
                "Example : 2   \n")
            delete_data = (input().split())
            delete_booking(cursor, connection , database, delete_data)

            print(
                "Booking with following booking Id cancelled:", delete_data)

        case 5:
            print("two")
        case default:
            print( "Enter from 1 to 5 only")





connection_close(cursor, connection)