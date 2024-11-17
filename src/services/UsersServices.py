from src.database.db_mysql import get_connection

class UsersService():

    @classmethod
    def get_user(cls):
        try:
            connection= get_connection()
            print(connection)

            with connection.cursor() as cursor:
                cursor.execute('Select * from person')
                result= cursor.fetchall()
                print(result)

                connection.close()
                return 0
            
        except Exception as ex:
            print(ex)