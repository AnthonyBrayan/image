from src.database.db_mysql import get_connection;

#Model
from src.models.UsersModel import Users


class UsersService():

    @classmethod
    def get_user(cls):
        try:
            connection= get_connection()
            print(connection)

            with connection.cursor() as cursor:
                cursor.execute('Select * from users')
                result= cursor.fetchall()
                print(result)

                connection.close()
                return 'Este es el método get, se ve en consola'
            
        except Exception as ex:
            print(ex)
    
    @classmethod
    def post_user(cls, user:Users):
        try:
            connection= get_connection()
            print(connection)

            with connection.cursor() as cursor:
                id_user = user.id_user
                name_usuario= user.name_usuario
                password = user.password
                fk_id_type_user= user.fk_id_type_user
                fk_dni = user.fk_dni

                cursor.execute("insert into users(id_user, name_usuario, password, fk_id_type_user, fk_dni)" + 
                               "values ('{0}', '{1}', '{2}', '{3}','{4}');".format(id_user, name_usuario, password, fk_id_type_user, fk_dni))
                connection.commit()

                connection.close()
                return 'Este es el método post, se imprime en consola'
            
        except Exception as ex:
            print(ex)

    @classmethod
    def put_user(cls, user:Users):
        try:
            connection= get_connection()

            with connection.cursor() as cursor:
                id_user = user.id_user
                name_usuario= user.name_usuario
                password = user.password
                fk_id_type_user= user.fk_id_type_user
                fk_dni = user.fk_dni

                sql= """
                UPDATE users 
                SET name_usuario = %s, password = %s, fk_id_type_user = %s, fk_dni = %s 
                WHERE id_user = %s;
                """

                values = (name_usuario, password, fk_id_type_user, fk_dni, id_user)

                cursor.execute(sql,values)

                connection.commit()

                connection.close()
                return 'Este es el método put, se imprime en consola'
            
        except Exception as ex:
            print(ex)