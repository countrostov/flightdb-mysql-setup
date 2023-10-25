def insert_flight(cursor, connection , database, insert_data):
    from insert_query import insert_query
    #flight
    query = ("INSERT INTO flight "
             "(flight_id, from_destination, to_destination, seat_capacity, travel_time, cost, emp_id) "
             "VALUES (%s, %s, %s, %s, %s, %s, %s)")
    #insert_data = ('LH104', 'Bengaluru', 'Tokyo', '300', '18', '53000', '5')

    insert_query(cursor, connection , database,query , insert_data)


