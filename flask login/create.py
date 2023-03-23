import sqlite3

connection = sqlite3.connect("user_data.db")
cursor = connection.cursor()

# command = """CREATE TABLE IF NOT EXISTS users(name TEXT,password TEXT)"""

# cursor.execute(command)

cursor.execute("INSERT INTO users VALUES('AKASH','AKASH@123')")
cursor.execute("INSERT INTO users VALUES('NAVANG','ADMIN@123')")

connection.commit()

