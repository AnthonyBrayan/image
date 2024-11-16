from src.database.db_mysql import get_connection

class UsersService():

    @classmethod
    def get_user(cls):
        try:
            connection= get_connection
            print(connection)
            
        except Exception as ex:
            print(ex)