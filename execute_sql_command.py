def execute_sql_command(cursor, connection , database, query):

    import mysql.connector


    TABLES = query
    # TABLES['customer'] = (
    #     "CREATE TABLE `customer` ("
    #     "  `phone_number` INT(255) NOT NULL,"
    #     "  `first_name` varchar(14) NOT NULL,"
    #     "  `last_name` varchar(16) NOT NULL,"
    #     "  `birth_date` date NOT NULL,"
    #     "  `gender` enum('M','F') NOT NULL,"
    #     "  `house_number` SMALLINT(255) NOT NULL,"
    #     "  `street` varchar(14) NOT NULL,"
    #     "  `city` varchar(14) NOT NULL,"
    #     "  `emergency_contact` INT(255) NOT NULL,"
    #     "  PRIMARY KEY (`phone_number`)"
    #     ") ")

    #for table_name in TABLES:
        #table_description = TABLES[table_name]
    try:
        print("Executing query",query)
        cursor.execute(query)
    except mysql.connector.Error as err:
        print(err.msg)

    print("SQL query executed successfully")

    return cursor