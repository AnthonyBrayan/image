from src.database.db_mysql import get_connection;

#Model
from src.models.PersonModel import Person


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
    
    @classmethod
    def post_user(cls, person:Person):
        try:
            connection= get_connection()
            print(connection)

            with connection.cursor() as cursor:
                dni = person.dni
                name_person= person.name_person
                phone = person.phone

                cursor.execute("insert into person(dni, name_person, phone) values ('{0}', '{1}', '{2}');".format(dni, name_person, phone))
                connection.commit()

                connection.close()
                return 'Este es el método post, se imprime en consola'
            
        except Exception as ex:
            print(ex)