def passenger_list(cursor, connection , database, query_data):
    from Search_query_bookinglist import search_query_bookinglist

    query = ("SELECT c.last_name,c.first_name, c.phone_number , b.bid , b.boarding_status , f.from_destination, "
             "f.to_destination , fs.flightschedule_id , fs.flight_id , b.no_of_seats, "
             "fs.start_date , fs.reaching_date "
             "FROM customer c , booking b , flight_schedule fs , flight f "
             "WHERE  fs.flightschedule_id = %s and b.customer = c.phone_number and "
             "b.flightschedule_id = fs.flightschedule_id  "
             "and fs.flight_id = f.flight_id  "
             )
    #query_data = ['32']
    cursor = search_query_bookinglist (cursor, connection , database,query, query_data)
    records  = cursor.fetchall()
    print("Passenger List for flight schedule ", query_data)
    for row in records:
         print (row)


    query = ("SELECT c.last_name,c.first_name, c.cust , cp.bid "
             "FROM copassenger c , copassenger_list cp, flight_schedule fs, booking b "
             "WHERE  b.flightschedule_id = fs.flightschedule_id and fs.flightschedule_id = %s and b.bid = cp.bid "
             "and cp.dep_id = c.dep_id  "
             )
    #query_data = ['32']

    search_query_bookinglist(cursor, connection, database, query, query_data)
    records = cursor.fetchall()
    print("\n Co-Passenger List for flight schedule ", query_data)
    for row in records:
        print(row)