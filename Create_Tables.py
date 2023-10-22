def create_tables(cursor, database):

    import mysql.connector
    from mysql.connector import errorcode



    TABLES = {}
    TABLES['customer'] = (
        "CREATE TABLE `customer` ("
        "  `phone_number` INT(255) NOT NULL,"
        "  `first_name` varchar(14) NOT NULL,"
        "  `last_name` varchar(16) NOT NULL,"
        "  `birth_date` date NOT NULL,"
        "  `gender` enum('M','F') NOT NULL,"
        "  `house_number` SMALLINT(255) NOT NULL,"
        "  `street` varchar(14) NOT NULL,"
        "  `city` varchar(14) NOT NULL,"
        "  `emergency_contact` INT(255) NOT NULL,"
        "  PRIMARY KEY (`phone_number`)"
        ") ")

    TABLES['copassenger'] = (
        "CREATE TABLE `copassenger` ("
        "  `dep_id` INT(255) NOT NULL AUTO_INCREMENT,"
        "  `first_name` varchar(14) NOT NULL,"
        "  `last_name` varchar(16) NOT NULL,"
        "  `emergency_contact` INT(255) NOT NULL,"
        "  PRIMARY KEY (`dep_id`),"
        "  `cust` INT(255),"
        "  FOREIGN KEY (`cust`) REFERENCES `customer`(`phone_number`)"
        ") ")

    TABLES['flight_manager'] = (
        "CREATE TABLE `flight_manager` ("
        "  `emp_id` INT(255) NOT NULL AUTO_INCREMENT,"
        "  `first_name` varchar(16) NOT NULL,"
        "  `last_name` varchar(16) NOT NULL,"
        "  `airline` varchar(16) NOT NULL,"
        "  `designation` varchar(16) NOT NULL,"
        "  `phone_number` INT(255) NOT NULL,"
        "  PRIMARY KEY (`emp_id`)"
        ") ")

    TABLES['flight'] = (
        "CREATE TABLE `flight` ("
        "  `flight_id` INT(255) NOT NULL,"
        "  `from` varchar(16) NOT NULL,"
        "  `to` varchar(16) NOT NULL,"
        "  `seat_capacity` INT(255) NOT NULL,"
        "  `travel_time` INT(255) NOT NULL,"
        "  `cost` INT(255) NOT NULL,"        
        "  PRIMARY KEY (`flight_id`),"
        "  `emp_id` INT(255),"
        "  FOREIGN KEY (`emp_id`) REFERENCES `flight_manager`(`emp_id`)"
        ") ")

    TABLES['flight_schedule'] = (
        "CREATE TABLE `flight_schedule` ("
        "  `flight_id` INT(255) NOT NULL,"
        "  `start_date` date NOT NULL,"
        "  `reaching_date` date NOT NULL,"
        "  CONSTRAINT `PK_flight_schedule` PRIMARY KEY (`start_date`,`reaching_date` ),"
        "  FOREIGN KEY (`flight_id`) REFERENCES `flight`(`flight_id`)"
        ") ")


    TABLES['booking'] = (
        "CREATE TABLE `booking` ("
        "  `bid` INT(255) NOT NULL AUTO_INCREMENT,"
        "  `no_of_seats` INT(255) NOT NULL,"
        "  `customer` INT(255) NOT NULL,"
        "  `flight_id` INT(255) NOT NULL,"
        "  `boarding_status` enum('y','n') NOT NULL,"
        "  `start_date` date NOT NULL,"
        "  `reaching_date` date NOT NULL,"
        "  PRIMARY KEY (`bid`),"
        "  FOREIGN KEY (`flight_id`) REFERENCES `flight`(`flight_id`),"
        "  FOREIGN KEY (`customer`) REFERENCES `customer`(`phone_number`),"
        "  FOREIGN KEY (`start_date`, `reaching_date`) REFERENCES `flight_schedule`(`start_date`, `reaching_date`)"
        ") ")

    TABLES['copassenger_list'] = (
        "CREATE TABLE `copassenger_list` ("
        "  `bid` INT(255) ,"
        "  `dep_id` INT(255) NOT NULL,"
        "  FOREIGN KEY (`bid`) REFERENCES `booking`(`bid`),"
        "  FOREIGN KEY (`dep_id`) REFERENCES `copassenger`(`dep_id`)"
        ") ")

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

    print("Tables created successfully")
