def search_flightschedule(cursor, connection , database, query_data):

    import mysql.connector

    query = ("SELECT fs.flightschedule_id, f.flight_id , fs.start_date, fs.reaching_date, "
             "f.from_destination , f.to_destination "
             "from flight_schedule fs , flight f "
             "WHERE fs.flight_id  = f.flight_id and f.emp_id = %s")
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

