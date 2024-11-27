from flask import Blueprint, jsonify,request

from src.services.UsersServices import UsersService
from src.models.UsersModel import Users

main = Blueprint('users_blueprint',__name__)

@main.route('/',methods=['GET'])
def get_users():

    try:
        UsersService.get_user()
        print('Esto se imprime en consola')
        return 'Esto en la página'
    
    except Exception as ex:
     print(ex)

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
        post_user= UsersService.post_user(user)
        print(post_user)

        return jsonify({"message": "Usuario registrado"})
    
    except Exception as ex:
     print(ex)
     response = jsonify({'message': 'Internal Server Error'})
     return response, 500
    
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
        put_user= UsersService.put_user(user)
        print(put_user)

        return jsonify({"message": "Usuario actualizado"})

    except Exception as ex:
        print(ex)
        response = jsonify({'message': 'Internal Server Error'})
        return response, 500

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

        delete_user=UsersService.delete_user(id_user)
        print(delete_user)

        return jsonify({"message": "Usuario eliminado"})

    except Exception as ex:
        print(ex)
        response = jsonify({'message': 'Internal Server Error'})
        return response, 500