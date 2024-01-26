import mysql.connector

database = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="linus123",
    database="E-handel"
)

cursor = database.cursor(dictionary=True)

def login_query(username, password):
    cursor.execute(f"SELECT * FROM users where username = '{username}' and password = '{password}' LIMIT 1")
    result = cursor.fetchall()
    return result

def check_if_user_exist(username):
    cursor.execute(f"SELECT * FROM users where username = '{username}'")
    result = cursor.fetchall()
    return result

def create_user(username, password):
    cursor.execute("INSERT INTO users (username, password, role) "
                   f"VALUES ('{username}', '{password}', 'USER')")
    database.commit()

def get_all_products():
    cursor.execute(f"SELECT * FROM products")
    result = cursor.fetchall()
    return result