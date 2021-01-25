import sqlite3

connection = sqlite3.connect('project_hotel.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS" \
               " hoteis" \
               " (id int PRIMARY KEY," \
               " name text," \
               " stars real," \
               " hotel_night real," \
               " city text )"
cursor.execute(create_table)

connection.commit()
connection.close()
