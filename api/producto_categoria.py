from flask_restful import Resource
from ..app import mysql


class ProductosCategoriaAPI(Resource):
    def get(self, id):
        cur = mysql.connection.cursor()
        cur.execute('''
        SELECT p.titulo, c.nombre as categoria
            FROM  myblog.post as p
            LEFT JOIN myblog.categoria  as c
            ON p.idcategoria = c.idcategoria
            WHERE p.idcategoria = ''' + id )
        result = cur.fetchall()
        return str(result)