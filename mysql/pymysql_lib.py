import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='Bank_Application',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def create_table():

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "CREATE TABLE users (id INT(3) PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(50), password VARCHAR(30), account_no VARCHAR(12), age INT(3), balance int(20));"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
        

    finally:
        print("Successfully created Database..!!")
        # connection.close()

    return True


def add_user(name, age, password, acct_no):
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = f"INSERT INTO users (name, age, password, account_no, balance) VALUES('{name}', {age}, '{password}', '{acct_no}', 0);"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

    finally:
        print("Successfully Added User..!!")

def fetch_user_details(name):

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = f"SELECT name, password, balance FROM users WHERE name = '{name}';"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        data = cursor.fetchall()

        return data

    finally:
        print("Successfully fetched.!!")
        # connection.close()

def GenerateStatement(name):

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = f"SELECT Trans_Date,destination,(select transaction_name from transaction_type tt where tt.id = t.type) as Trans_Type from transaction as t where account_Name = '{name}';"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        data = cursor.fetchall()

        return data

    finally:
        print("Successfully fetched.!!")
        # connection.close()

def get_balance(name):

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = f"SELECT balance FROM users WHERE name = '{name}';"
            cursor.execute(sql)
        data = cursor.fetchall()
        return data

    finally:
        print("Successfully fetched.!!")


def alter_balance(name, balance):

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = f"UPDATE users SET balance = {balance} where name = '{name}'"
            
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

    finally:
        print("Successfully updated User balance..!!")
        # connection.close()
        
def transaction_log(name,amount,destination,types):
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = f"INSERT into transaction(account_Name,type,destination,amount) VALUES ('{name}',{types},'{destination}',{amount});"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

    finally:
        #print("Successfully updated User balance..!!")
        # connection.close()

# alter_balance("bolanle", 24000)
# add_user('x',22, '112','owe2093')