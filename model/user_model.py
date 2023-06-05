import mysql.connector
import json
from flask import jsonify
from utils import create_response
from flask import make_response
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
            getall_query = "SELECT * FROM users"
            self.cur.execute(getall_query)
            result = self.cur.fetchall()
            if len(result) > 0:
                res = create_response(success=True, message="User Data fetched", status_code=200, data=result)
                res.headers['Access-Control-Allow-Origin'] = "*"
                return res
                # return create_response(success=True, message="User Data fetched", status_code=200, data=result)
            else:
                return create_response(success=True, message="NO User Data to be fetched", status_code=204, data=result)
            # return jsonify(result)  # Using Flask's jsonify to convert result to JSON response
            # return json.dumps(result) # converting to string
        except Exception as e:
            return create_response(success=False, message="Some error occured while fetching the data", status_code=400)

    # User POST Query
    def user_addone_model(self, data):
        try:
            self.cur.execute(f"INSERT INTO flask_db.users (name, id, email, password, phone, role)\
                             VALUES ('{data['name']}','{data['id']}','{data['email']}','{data['password']}','{data['phone']}','{data['role']}');")
            return create_response(success=True, message="User created successfully", status_code=201)
        except Exception as e:
            return create_response(success=False, message="Some error occured while adding the data", status_code=400)

    # User UPDATE Query
    def user_update_model(self, data):
        try:
            # query: UPDATE TABLE_NAME SET col=val, col=val WHERE id={id}}
            self.cur.execute(f"UPDATE users SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}', password='{data['password']}', role='{data['role']}' WHERE id={data['id']};")
            if self.cur.rowcount > 0:
                return create_response(success=True, message="User Updated successfully", status_code=200)
            return create_response(success=True, message="Nothing to update", status_code=204)
        except Exception as e:
            return create_response(success=False, message="Some error occured while updating the data", status_code=400)
    
    # User PATCH Query
    def user_patch_model(self, data, id):
        try:
            # query: UPDATE TABLE_NAME SET col=val, col=val WHERE id={id}}
            query = "UPDATE users SET "
            for key in data:
                query += f"{key}='{data[key]}', "
            query = query[:-2] + f" WHERE id={id};"

            self.cur.execute(query)
            if self.cur.rowcount > 0:
                return create_response(success=True, message="User Updated successfully", status_code=200)
            return create_response(success=True, message="Nothing to update", status_code=204)
        except Exception as e:
            return create_response(success=False, message="Some error occured while updating the data", status_code=400)

    # User DELETE Query
    def user_delete_model(self, id):
        try:
            self.cur.execute(f"DELETE FROM users WHERE id={id}")
            if self.cur.rowcount > 0:
                return create_response(success=True, message="User Deleted successfully", status_code=200)
            return create_response(success=True, message="Nothing to delete", status_code=204)
        except Exception as e:
            return create_response(success=False, message="Some error occured while deleting the data", status_code=400)

    # Pagination Query
    def user_pagination_model(self, limit_rows, page_no):
        start = (int(page_no) * int(limit_rows)) - int(limit_rows)

        query = f"SELECT * from users LIMIT {start}, {limit_rows}"
        try:
            self.cur.execute(query)
            result = self.cur.fetchall()
            if len(result) > 0:
                res = make_response({
                        "message":"User Data fetched",
                        "data": {
                            "user": result,
                            "page_no": page_no,
                            "limit_rows": limit_rows
                        },
                        "status_code": 200,
                    }, 200)
                # res = create_response(success=True, message="User Data fetched", status_code=200, data=result)
                res.headers['Access-Control-Allow-Origin'] = "*"
                return res
            else:
                return create_response(success=True, message="NO User Data to be fetched", status_code=204, data=result)
        except Exception as e:
            return create_response(success=False, message="Some error occured while fetching the data", status_code=400)

    # Upload user's avatar
    def user_avatar_upload_model(self, uid, filepath):
        try:
            update_query = f"UPDATE users SET avatar='{filepath}' WHERE id={uid}"
            self.cur.execute(update_query)
            if self.cur.rowcount > 0:
                    return create_response(success=True, message="File Uploaded successfully", status_code=200)
            return create_response(success=True, message="Nothing to upload", status_code=204)
        except Exception as e:
            return create_response(success=False, message="Some error occured while uploading the file", status_code=400)

