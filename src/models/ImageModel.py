class Image():
    def __init__(self, id_image, title_image, url_image, fk_id_user) -> None:
        self.id_image = id_image
        self.title_image = title_image
        self.url_image = url_image
        self.fk_id_user = fk_id_user