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
    except:
        print('Error creating table <3')

create_table()

#copy paste and replace the connection with your name
