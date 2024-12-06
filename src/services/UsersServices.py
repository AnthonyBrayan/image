from src.database.db_mysql import get_connection;
from flask import jsonify

import traceback

#Logger
from src.utils.Logger import Logger

#Model
from src.models.UsersModel import Users

#Werkzeug
from werkzeug.security import generate_password_hash

class UsersService():

    @classmethod
    def get_user(cls):
        try:
            connection= get_connection()
            print(connection)
            
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute('CALL sp_list_user()')
                    result= cursor.fetchall()

            if result:
                return {"status": "success", "data": result}
            else:
                return {"status": "success", "data": [], "message": "No hay usuarios disponibles"}
            
        except Exception as ex:
            Logger.add_to_log('error', str(ex))
            Logger.add_to_log('error',traceback.format_exc())
            return {"status": "error", "message": "Error al mostrar usuarios"}
    
    @classmethod
    def post_user(cls, user:Users):
        try:
            connection= get_connection()
            print(connection)

            with connection:
                with connection.cursor() as cursor:
                    id_user = user.id_user
                    name_usuario= user.name_usuario
                    password = user.password
                    fk_id_type_user= user.fk_id_type_user
                    fk_dni = user.fk_dni

                    encripted_password= generate_password_hash(password, 'pbkdf2:sha256',30)

                    sql="""
                        CAll sp_add_user(%s, %s, %s, %s,%s);
                        """
                    values= (id_user, name_usuario, encripted_password, fk_id_type_user, fk_dni)
                    
                    cursor.execute(sql, values)
                    connection.commit()

                    if cursor.rowcount > 0:
                        return {"status": "success", "message": "Usuario registrado exitosamente"}
                    else:
                        return {"status": "error", "message": "No se pudo registrar el usuario"}
            
        except Exception as ex:
            Logger.add_to_log('error', str(ex))
            Logger.add_to_log('error', traceback.format_exc())
            return {"status": "error", "message": "Error al registrar el usuario"}

    @classmethod
    def put_user(cls, user:Users):
        try:
            connection= get_connection()
            
            with connection:
                with connection.cursor() as cursor:
                    id_user = user.id_user
                    name_usuario= user.name_usuario
                    password = user.password
                    fk_id_type_user= user.fk_id_type_user
                    fk_dni = user.fk_dni

                    encripted_password= generate_password_hash(password, 'pbkdf2:sha256',30)

                    # Placeholders parametrizados: Create for sql query.
                    sql= """
                    CALL sp_put_user(%s,%s,%s,%s,%s)
                    """

                    values = (name_usuario, encripted_password, fk_id_type_user, fk_dni, id_user)

                    cursor.execute(sql,values)

                    connection.commit()

                    if cursor.rowcount > 0:
                        return {"status": "success", "message": "Usuario actualizado exitosamente"}
                    else:
                        return {"status": "error", "message": "No se encontró el usuario para actualizar"}
            
        except Exception as ex:
            Logger.add_to_log('error', str(ex))
            Logger.add_to_log('error', traceback.format_exc())
            return {"status": "error", "message": "Error al actualizar el usuario"}

    @classmethod
    def delete_user(cls, id_user: int):
            try:
                connection= get_connection()

                with connection:
                    with connection.cursor() as cursor:

                        sql = """
                            CALL sp_delete_user(%s)

                            """
                        values=(id_user)

                        cursor.execute(sql,values)
                        connection.commit()

                if cursor.rowcount > 0:
                    return {"status" : "success", "message" : "Usuario eliminado exitosamente"}
                else:
                    return {"status" : "not_found", "message" : "No se encontró el usuario para eliminar"}

            except Exception as ex:
                Logger.add_to_log('error', str(ex))
                Logger.add_to_log('error', traceback.format_exc())
                return {"status":"error", "message":"Error al eliminar usuario"}