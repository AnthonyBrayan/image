from flask import Blueprint, jsonify,request

from src.services.UsersServices import UsersService
from src.models.UsersModel import Users

main = Blueprint('users_blueprint',__name__)

@main.route('/',methods=['GET'])
def get_users():

    try:
        service_response = UsersService.get_user()

        if service_response['status'] == 'success':

            if service_response.get('data'):
                return jsonify({"success": True, "users": service_response['data']}), 200
            else:
                return jsonify({"success": True, "message": service_response.get('message')}), 204
        else:
            return jsonify({"success": False, "message": service_response['message']}), 500
    
    except Exception as ex:
     print(ex)
     return ({"status":"error", "message":"Internal Server Error"}, 500)

@main.route('/',methods=['POST'])
def post_users():
    try:

        required_fields = ['name_usuario', 'password', 'fk_id_type_user', 'fk_dni']
        errors = []

        for field in required_fields:
            if field not in request.json:
                errors.append(f"{field} es obligatorio")

        if errors:
            return jsonify({"errors": errors}), 400

        name_usuario= request.json['name_usuario']
        password = request.json['password']
        fk_id_type_user = request.json['fk_id_type_user']
        fk_dni = request.json['fk_dni']

        user= (Users(None,name_usuario, password, fk_id_type_user, fk_dni))
        service_response= UsersService.post_user(user)
        print(service_response)

        if service_response['status'] == 'success':
            return jsonify(service_response), 201
        else:
            return jsonify(service_response), 400
    
    except Exception as ex:
     print(ex)
     return jsonify({"status":"error", "message":"Internal Server Error"}, 500)
    
@main.route('/',methods=['PUT'])
def put_users():

    try:
        required_fields = ['id_user','name_usuario', 'password', 'fk_id_type_user', 'fk_dni']
        errors = []

        for field in required_fields:
            if field not in request.json:
                errors.append(f"{field} es obligatorio")

        if errors:
            return jsonify({"errors": errors}), 400

        id_user = request.json['id_user']
        name_usuario= request.json['name_usuario']
        password = request.json['password']
        fk_id_type_user = request.json['fk_id_type_user']
        fk_dni = request.json['fk_dni']

        user= (Users(id_user,name_usuario, password, fk_id_type_user, fk_dni))
        service_response= UsersService.put_user(user)

        # Construir respuesta HTTP
        if service_response['status'] == 'success':
            return jsonify(service_response), 200
        else:
            return jsonify(service_response), 404

    except Exception as ex:
        print(ex)
        return jsonify({"status":"error", "message": "Internal Server Error"}), 500

@main.route('/',methods=['DELETE'])
def delete_users():

    try:
        requered_field=['id_user']
        errors=[]

        for field in requered_field:
            if field not in request.json:
                errors.append(f"{field} es obligatorio.")

        if errors:
            return jsonify({"errors": errors}), 400

        id_user = request.json['id_user']

        service_response= UsersService.delete_user(id_user)

        if service_response['status'] == 'success':
            return jsonify(service_response), 200
        elif service_response ['status'] == 'not_found':
            return jsonify(service_response), 404
        else:
            return jsonify({"status":"error", "message":"No se pudo eliminar el usuario"}, 400)

    except Exception as ex:
        print(ex)
        return jsonify({"status": "error", "message": "Internal Server Error"}, 500)