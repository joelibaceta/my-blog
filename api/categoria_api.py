from flask_mysqldb import MySQL
from flask_restful import Resource
from ..app import mysql

class CategoriaAPI(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM categoria")
        result = cur.fetchall()
        return str(result)
