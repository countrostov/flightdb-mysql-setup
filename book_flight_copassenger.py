def book_flight_copassenger(cursor, connection , database, insert_data):
    from insert_query import insert_query

    #bid = cursor.lastrowid
    query = ("INSERT INTO copassenger_list "
            "(bid ,dep_id ) "
            "VALUES (%s, %s)")
    #insert_data = ('6', '1' )

    insert_query(cursor, connection , database,query, insert_data)

