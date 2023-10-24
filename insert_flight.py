def insert_flight(cursor, connection , database, insert_data, insert_data1):
    from insert_query import insert_query
    #flight
    query = ("INSERT INTO flight "
             "(flight_id, from_destination, to_destination, seat_capacity, travel_time, cost, emp_id) "
             "VALUES (%s, %s, %s, %s, %s, %s, %s)")
    #insert_data = ('LH104', 'Bengaluru', 'Tokyo', '300', '18', '53000', '5')

    insert_query(cursor, connection , database,query , insert_data)

    #flight_schedule
    flightschedule_id = cursor.lastrowid
    query = ("INSERT INTO flight_schedule "
             "(flightschedule_id ,start_date, reaching_date,flight_id) "
             "VALUES (%s, %s, %s, %s)")
    insert_data2 = (flightschedule_id,) + insert_data1
    insert_query(cursor, connection , database,query , insert_data2)
