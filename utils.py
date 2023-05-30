# from django.http import JsonResponse
from flask import jsonify

# Custom Response for Success and Error Messages
def create_response(success: bool, message: str, data: str=None, status_code: int=None, **kwargs):
    return jsonify({"data":data,"message": message, **kwargs, "status_code": status_code}) # Using Flask's jsonify to convert result to JSON response
    # return JsonResponse(data={"data":data,"message": message, **kwargs, "status_code": status_code}, status=status_code)