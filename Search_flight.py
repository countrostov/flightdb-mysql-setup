def search_flight(cursor, connection , database, query_data):
    import mysql.connector
    from mysql.connector import Error
    from Search_query import search_query


    query = ("SELECT f.flight_id, f.from_destination, f.to_destination , f.travel_time , f.cost  ,"
             "fs.start_date, fs.reaching_date "
             "FROM flight f , flight_schedule fs "
             "WHERE  f.flight_id = fs.flight_id and "
             "f.from_destination=%s and  f.to_destination= %s and fs.start_date=%s "
             )
    #query_data = ['Bengaluru','frankfurt', ' 2023-11-3']

    cursor1 = search_query(cursor, connection , database,query, query_data)
    return cursor1