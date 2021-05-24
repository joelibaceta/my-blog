

from flask import Flask
from flask_restful import Resource, Api
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)
api = Api(app)

from .api.producto_categoria import ProductosCategoriaAPI
from .api.post import PostAPI
from .api.categoria_api import CategoriaAPI
from .api.hello_api import HelloWorld

app.config["MYSQL_USER"]        = "root"
app.config["MYSQL_PASSWORD"]    = "rootcodigo"
app.config["MYSQL_DB"]          = "myblog"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

api.add_resource(HelloWorld, '/hello')
api.add_resource(CategoriaAPI, '/categoria')
api.add_resource(PostAPI, '/post')
api.add_resource(ProductosCategoriaAPI, '/categoria/<id>/posts')