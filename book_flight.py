def book_flight(cursor, connection , database, insert_data):
    import mysql.connector
    from mysql.connector import Error
    from flight_booking_query import flight_booking_query

    bid = cursor.lastrowid
    query = ("INSERT INTO booking "
            "(bid ,no_of_seats, customer, boarding_status,flightschedule_id ) "
            "VALUES (%s, %s, %s, %s, %s)")
    insert_data1 = (bid,) + insert_data
    cursor = flight_booking_query(cursor, connection , database,query, insert_data1)
    cursor.lastrowid
    return cursor

