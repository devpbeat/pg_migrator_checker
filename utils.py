def get_table_names(connection):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
        """)
        tables = cursor.fetchall()
        # just add tables that has 'core_' in the name
        #return [table[0] for table in tables]
        tables_names = []
        for table in tables:
            if 'core_' in table[0]:
                tables_names.append(table[0])
        return tables_names

def get_count_table(connection, table_name):
    with connection.cursor() as cursor:
        if '_user' in table_name:
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        else:
            cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE status = 1")
        result = cursor.fetchone()
        return result[0]