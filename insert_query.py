def insert_query(cursor, connection , database,data):
    #from __future__ import print_function
    import mysql.connector
    from datetime import date, datetime, timedelta

    add_flight_manager = ("INSERT INTO flight_manager "
                  "(emp_id, first_name, last_name, airline , designation, phone_number) "
                  "VALUES (%s, %s, %s, %s, %s, %s)")

    # Insert salary information
    emp_id = cursor.lastrowid
    #data_flight_manager = (emp_id, 'Matt', 'Healy', 'British Air', 'flight_manager', '1000000002')
    data_flight_manager = data

    try:
        print("Executing query", add_flight_manager)
        cursor.execute(add_flight_manager, data_flight_manager)
        connection.commit()
    except mysql.connector.Error as err:
        print(err.msg)

    print("Data inserted successfully ")

