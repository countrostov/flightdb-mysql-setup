def search_booking(cursor, connection , database, query_data):

    import mysql.connector

    query = ("SELECT bid, no_of_seats, customer , boarding_status , flightschedule_id  FROM booking "
             "WHERE customer = %s ")
    # hire_start = datetime.date(1999, 1, 1)
    # hire_end = datetime.date(1999, 12, 31)

    try:
        print("Executing Search query", query)
        cursor.execute(query, query_data)
    except mysql.connector.Error as err:
        print(err.msg)

    #for (flight_id, from_destination, to_destination , travel_time , cost, start_date, reaching_date ) in cursor:
       # print((flight_id, from_destination, to_destination , travel_time , cost, start_date, reaching_date))

    #print("Data Read successfully ")

    return cursor

