import pyodbc

driver = "Driver = {SQL Server Native Client 11.0};"
server = "Server =LENOVO-PC;"
database = "Database = Employment;"
trusted_connection = "Trusted_Connection = yes;"

def read(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Test;")

    for row in cursor:
        print("row = {}".format(row))

def create(conn):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Test(name,class, character_level) VALUES('Therkla', 'Ninja', '14');
        ''')
    conn.commit()
    read(conn)

def update(conn):
    cursor = conn.cursor()
    cursor.execute(
            'UPDATE Test SET name=? WHERE class=?;', ('Ninja Girl', 'Ninja')
            )
    conn.commit()
    read(conn)

def delete(conn):
    cursor = conn.cursor()
    cursor.execute('''
            DELETE FROM Test WHERE class = 'Ninja';
            ''')
    conn.commit()
    read(conn)

conn = pyodbc.connect(
"Driver={SQL Server Native Client 11.0};"
"Server=LENOVO-PC;"
"Database=Employment;"
"Trusted_Connection=yes;"
)

read(conn)
create(conn)
update(conn)
delete(conn)


conn.close()