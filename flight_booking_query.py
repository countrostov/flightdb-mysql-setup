def flight_booking_query(cursor, connection , database,query, insert_data):
    import mysql.connector
    try:
        print("Executing query", query)
        cursor.execute(query, insert_data)
        connection.commit()
    except mysql.connector.Error as err:
        print(err.msg)

    print("Data inserted successfully ")

    return cursor