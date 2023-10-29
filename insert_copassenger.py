def insert_copassenger(cursor, connection , database, insert_data):
    from insert_query import insert_query



    # #copassenger
    dep_id = cursor.lastrowid
    query = ("INSERT INTO copassenger "
             "(dep_id ,first_name,last_name, emergency_contact, cust) "
             "VALUES (%s, %s, %s, %s, %s)")
    insert_data1 = (dep_id,)+ insert_data
    #insert_data = (dep_id, 'san', 'tha', '1100000011', '1000000001')


    cursor = insert_query(cursor, connection , database,query , insert_data1)
    return cursor
