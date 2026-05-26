import pymysql

def connect_db():
    try:
        connection = pymysql.connect(user = 'root', password = 'Ananya008!',port = 3306, database = 'Ananya', charset = 'utf8', host = 'localhost')
        print("DB connected successfully")
        return connection
    except Exception as e:
        print(f"DB connection failed: {e}")


def disconnect_db(connection):
    try:
        connection.close()
        print("disconnected")
    except :
        print(f"DB disconnection failed")

def create_table():
    query = 'create table IF NOT EXISTS people(id int primary key auto_increment, name varchar(64) not null, gender bool not null, location varchar(32),int age default(0))'
    try:
        connection = connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        if count == 0:
            print ("Table created successfully")
        else:
            print ("Table creation failed")
        cursor.close()
        disconnect_db(connection)
    except :
        print('Error creating table <3')

create_table()
def create_person_demo():
    query = '''
create table IF NOT EXISTS people(
    id int primary key auto_increment,
    name varchar(64) not null,
    gender bool not null,
    age int default 0,
    location varchar(32)
)
'''
    try:
        connection = connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        if count == 1:
            print ("Person created successfully")
        else:
            print ("Person creation failed")
        
        cursor.close()
        disconnect_db(connection)
    except Exception as e:
        print(e.msg)
        print('Error creating person <3')

def read_person():
    name = input("Enter name to search: ")
    age = int(input("Enter age to search: "))
    gender = input("Enter gender to search: ")
    location = input("Enter location to search: ")
    if gender.lower() == 'f':
        gender = True
    else:
        gender = False
    return (name, gender,age, location)

def create_person():
    query = 'insert into people(name, gender, age, location) values(%s, %s, %s, %s);'
    try:
        person = read_person()
        connection = connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query, person)
        
        if count >= 1:
            print ("Person created successfully")
        else:
            print ("Person creation failed")
        
        connection.commit()
        cursor.close()
        disconnect_db(connection)
    except Exception as e:
        print(e)
        print('Person creation failed <3')

create_person()

def search_person():
    id = int(input("Enter id to search: "))
    query = f'select * from people where id = {id};'
    try:
        connection = connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        print(f"Count: {count}")
        if count == 1:
            row = cursor.fetchone()
            print(row)
            print(type(row))
        else:
            print ("No person found")
        connection.commit()
        cursor.close()
        disconnect_db(connection)
    except Exception as d:
        print(d)
        print('Search person failed <3')


def update_person():
    id = int(input("Enter id to update: "))
    new_location = input("Enter new location: ")
    query = 'update people set location = %s where id = %s;'
    
    try:
        connection = connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query, (new_location, id))
        connection.commit()
        cursor.close()
        disconnect_db(connection)
        print(f"Count: {count}")
        if count == 1:
            print (f"Person id {id} updated successfully")
        else:
            print (f"Person {id} update failed")
        
        
    except Exception as f:
        print(f)
        print('Update of person failed <3')


def delete_person():
    id = int(input("Enter id to delete: "))
    query = f'delete from people where id = {id};'
    try:
        connection = connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        connection.commit()
        print(f"Count: {count}")
        if count == 1:
            print (f"Person id {id} deleted successfully")
        else:
            print (f"Person {id} deletion failed")
        
        cursor.close()
        disconnect_db(connection)
    except Exception as f:
        print(f)
        print('Delete of person failed <3')


def list_people():
    query = 'select * from people;'
    try:
        connection = connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        print(f"Count: {count}")
        if count == 1:
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        else:
            print ("No person found")
        connection.commit()
        cursor.close()
        disconnect_db(connection)
    except Exception as d:
        print(d)
        print('Listing people failed <3')


