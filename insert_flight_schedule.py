def insert_flight_schedule(cursor, connection , database, insert_data1):
    from insert_query import insert_query

    #flight_schedule
    flightschedule_id = cursor.lastrowid
    query = ("INSERT INTO flight_schedule "
             "(flightschedule_id ,start_date, reaching_date,flight_id) "
             "VALUES (%s, %s, %s, %s)")
    insert_data2 = (flightschedule_id,) + insert_data1
    insert_query(cursor, connection , database,query , insert_data2)
