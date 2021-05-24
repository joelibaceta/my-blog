from flask_restful import Resource
from ..app import mysql

class PostAPI(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM post")
        result = cur.fetchall()
        return str(result)