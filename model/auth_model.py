from functools import wraps
import mysql.connector
import json
from flask import make_response, request
import jwt
import re
from config.config import dbconfig

class auth_model():

    # Initializing constructor and establishing connection first.
    def __init__(self):
        # mysql database connection establishment between python and mysql
        try:
            # change the details as per your db config.
            self.conn = mysql.connector.connect(
                host=dbconfig['hostname'],
                user=dbconfig['username'],
                password=dbconfig['password'],
                database=dbconfig['datbase']
            )
            print('Connection Established Successfully')
            self.conn.autocommit=True # Automatically commit() to the database once POST, PUT, DELETE queries are executed.
            self.cur = self.conn.cursor(dictionary=True) # Cursor will help in query execution and interaction with database
        except Exception as e:
            print('Some error occured. Connect not established', e)

    # Creating a JWT auth decorator
    def token_auth(self, endpoint=""):
        def inner1(func):
            # To solve this error:
            # AssertionError: View function mapping is overwriting an existing endpoint function: inner2
            @wraps(func)
            def inner2(*args):
                endpoint = request.url_rule # it's getting endpoint from request (dynamic)
                authorization = request.headers.get("Authorization")
                print("➡ authorization :", authorization)
                if re.match("Bearer *([^ ]+) *$", authorization, flags=0):
                    token = authorization.split(" ")[1]

                    try:
                        jwt_decoded = jwt.decode(token, "test1", algorithms="HS256")
                    except jwt.ExpiredSignatureError:
                        return make_response({"ERROR": "TOKEN EXPIRED"}, 401)
                    
                    role_id = jwt_decoded['payload']['role_id']
                    print("➡ role_id :", role_id)
                    get_role_query = f"SELECT roles FROM acceessibility_view WHERE endpoint='{endpoint}'"
                    print("➡ get_role_query :", get_role_query)
                    self.cur.execute(get_role_query)
                    result = self.cur.fetchall()

                    if len(result) > 0:
                        allowed_roles = json.loads(result[0]['roles'])
                        if role_id in allowed_roles:
                            return func(*args)
                        else: return make_response({"ERROR": "INVALID_ROLE"}, 404)

                    else: return make_response({"ERROR": "UNKNOWN_ENDPOINT"}, 404)
                else: return make_response({"message": "INVALID_TOKEN"}, 401)
            return inner2
        return inner1
    