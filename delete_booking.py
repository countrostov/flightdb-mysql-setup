def insert_query(cursor, connection , database,insert_query, insert_data):
    import mysql.connector
    try:
        print("Executing query", insert_query)
        cursor.execute(insert_query, insert_data)
        connection.commit()
    except mysql.connector.Error as err:
        print(err.msg)

    print("Data deleted successfully ")

