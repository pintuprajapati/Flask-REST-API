import mysql.connector
import json
from flask import jsonify
class user_model():

    # Initializing constructor and establishing connection first.
    def __init__(self):
        # mysql database connection establishment between python and mysql
        try:
            self.conn = mysql.connector.connect(host="localhost", user="flask_user", password="Admin@123", database="flask_db") # change the details as per your db config.
            print('Connection Established Successfully')
            self.conn.autocommit=True # Automatically commit() to the database once POST, PUT, DELETE queries are executed.
            self.cur = self.conn.cursor(dictionary=True) # Cursor will help in query execution and interaction with database
        except Exception as e:
            print('Some error occured. Connect not established', e)

    # User GET Query
    def user_getall_model(self):
        try:
            self.cur.execute("SELECT * FROM users")
            result = self.cur.fetchall()
            return jsonify(result)  # Using Flask's jsonify to convert result to JSON response
            # return json.dumps(result) # converting to string
        except Exception as e:
            print("➡ e :", e)

    # User POST Query
    def user_addone_model(self, data):
        try:
            self.cur.execute(f"INSERT INTO flask_db.users (name, id, email, password, phone, role)\
                             VALUES ('{data['name']}','{data['id']}','{data['email']}','{data['password']}','{data['phone']}','{data['role']}');")
            return "User created successfully"
        except Exception as e:
            print("➡ e :", e)

    # User UPDATE Query
    def user_update_model(self, data):
        try:
            self.cur.execute(f"UPDATE users SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}', password='{data['password']}', role='{data['role']}' WHERE id={data['id']};")
            if self.cur.rowcount > 0:
                return "User Updated successfully"
            return "Nothing to update"
        except Exception as e:
            print("➡ e :", e)

    # User DELETE Query
    def user_delete_model(self, id):
        try:
            self.cur.execute(f"DELETE FROM users WHERE id={id}")
            if self.cur.rowcount > 0:
                return "User Deleted successfully"
            return "Nothing to Delete"
        except Exception as e:
            print("➡ e :", e)