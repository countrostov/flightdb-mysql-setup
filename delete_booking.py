def delete_booking(cursor, connection , database, delete_data):

    import mysql.connector
    from insert_query import insert_query
    query = ("DELETE FROM booking "
             "WHERE bid = %s "
             )

    insert_query(cursor, connection, database, query, delete_data)


