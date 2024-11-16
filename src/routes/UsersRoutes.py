from flask import Blueprint

from src.services.UsersServices import UsersService

main = Blueprint('users_blueprint',__name__)

@main.route('/')
def get_users():
    UsersService.get_user()
    print('Esto se imprime en consola')
    return 'Esto en la página'