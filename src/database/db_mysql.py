import pymysql

def get_connection():
    try:
        return pymysql.connect(
            host= 'localhost',
            database= 'image',
            user= 'root',
            passwd= ''
        )
    except Exception as ex:
        print(ex)