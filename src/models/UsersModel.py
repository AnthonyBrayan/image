class Users():
    def __init__(self, id_user, name_usuario, password, fk_id_type_user, fk_dni) -> None:
        self.id_user= id_user
        self.name_usuario = name_usuario
        self.password = password
        self.fk_id_type_user = fk_id_type_user
        self.fk_dni = fk_dni