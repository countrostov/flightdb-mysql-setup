def search_query(cursor, connection , database,query, query_data):

    import mysql.connector

    # query = ("SELECT first_name, last_name, hire_date FROM employees "
    #          "WHERE hire_date BETWEEN %s AND %s")
    # hire_start = datetime.date(1999, 1, 1)
    # hire_end = datetime.date(1999, 12, 31)

    try:
        print("Executing Search query", query)
        cursor.execute(query, query_data)
    except mysql.connector.Error as err:
        print(err.msg)

    for (first_name, last_name, birth_date) in cursor:
        print((last_name, first_name, birth_date))

    print("Data Read successfully ")

