from app import app
from model.user_model import user_model
from flask import request, send_file
from datetime import datetime

obj = user_model()

@app.route('/user/getall')
def user_getall_controller():
    return obj.user_getall_model()

@app.route('/user/addone', methods=["POST"])
def user_addone_controller():
    return obj.user_addone_model(request.form) # this request.form, we are getting from POSTMAN "body" section. "Form-Encode" 

@app.route('/user/update', methods=["PUT"])
def user_update_controller():
    return obj.user_update_model(request.form)

@app.route('/user/delete/<id>', methods=["DELETE"])
def user_delete_controller(id):
    return obj.user_delete_model(id)

@app.route('/user/patch/<id>', methods=["PATCH"])
def user_patch_controller(id):
    return obj.user_patch_model(request.form, id)

# Pagination endpoint
@app.route('/user/getall/limit/<limit_rows>/page/<page_no>', methods=["GET"])
def user_pagination_controller(limit_rows, page_no):
    return obj.user_pagination_model(limit_rows, page_no)

# file uploading with unique filename
@app.route('/user/<uid>/upload/avatar/', methods=["PUT"])
def user_avatar_upload_controller(uid):
    file = request.files['avatar']
    unique_file_name = str(datetime.now().timestamp()).replace(".", "")
    file_name_split = file.filename.split(".")
    extension = file_name_split[len(file_name_split) - 1] # get the last item from the list which is extension (i.e. .png, .jpg)
    file_path = f"uploads/{unique_file_name}.{extension}" # save the file on this path with unique name plus extension
    file.save(file_path)
    return obj.user_avatar_upload_model(uid, file_path)

# fetch the file from db
@app.route("/uploads/<filename>")
def user_getavatar_controller(filename):
    return send_file(f"uploads/{filename}")