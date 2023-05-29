from dotenv import load_dotenv
load_dotenv('.env') 

from flask import Flask
app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome"

@app.route("/hello")
def hello():
    return "hello"

if __name__ == "__main__":
    app.run(debug=True)

# we are importing it here (Because 'app' instance is initialized above, so we have to import afterwards)
# import controller.user_controller as user_controller
# from controller import user_controller, product_controller
from controller import *

