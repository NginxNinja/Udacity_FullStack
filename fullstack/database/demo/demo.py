import psycopg2

connection = psycopg2.connect('dbname=example')

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table2;')

cursor.execute('''
    CREATE TABLE table2 (
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')

# Sample 1
cursor.execute('INSERT INTO table2 (id, completed) VALUES (1, true);')

# Sample 2
cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (2, True))

#S Sample 3
cursor.execute('INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);', {'id': 3, 'completed': False})

# Sample 4
SQL = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'
data = {'id': 4, 'completed': False}
cursor.execute(SQL, data)

# Query the results
cursor.execute('SELECT * FROM table2;')

# Printing the results of everything.
result_fetchall = cursor.fetchall()
print('fetchall: ', result_fetchall)

# Printing the first 2 results from the query.
result_fetchmany = cursor.fetchmany(2)
print('fetchmany(2): ', result_fetchmany)

# Printing the first result from the query.
result_fetchone = cursor.fetchone()
print('fetchone: ', result_fetchone)



connection.commit()

cursor.close()
connection.close()