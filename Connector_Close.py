
def connection_close(cursor, connection):
    cursor.close()
    connection.close()
    print("MySQL connection is closed in separate fn")