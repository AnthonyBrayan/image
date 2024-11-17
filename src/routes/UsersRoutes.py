from flask import Blueprint, request

from src.services.UsersServices import UsersService
from src.models.PersonModel import Person

main = Blueprint('users_blueprint',__name__)

@main.route('/',methods=['GET'])
def get_users():
    UsersService.get_user()
    print('Esto se imprime en consola')
    return 'Esto en la página'

@main.route('/',methods=['POST'])
def post_users():
    print(request)
    dni = request.json['dni']
    name_person= request.json['name_person']
    phone = request.json['phone']

    user= (Person(dni, name_person, phone))
    post_person= UsersService.post_user(user)
    print(post_person)

    # print(put_person)
    return 'Esto en la página'