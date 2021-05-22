from flask_mysqldb import MySQL
from flask_restful import Resource
from flask import current_app

class CategoriaAPI(Resource):
    def get(self):
        mysql = MySQL(current_app)
        cur = mysql.connection.cursor()

        return "categoria"