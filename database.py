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



