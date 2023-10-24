def search_query_bookinglist(cursor, connection , database,query, query_data):

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


    # if len(records) ==0 :
    #     print(" No data for the query available")
    # else:
    # for (last_name,phone_number , bid ) in cursor:
    #      print((last_name,phone_number , bid))

    records  = cursor.fetchall()
    for row in records:
        print (row)

    print("Data Read successfully ")

