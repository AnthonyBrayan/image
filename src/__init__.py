from flask import Flask;

#Routers
from .routes import UsersRoutes

app=Flask(__name__)

def init_app(config):
 app.config.from_object(config)

 app.register_blueprint(UsersRoutes.main, url_prefix='/Users')

 return app

