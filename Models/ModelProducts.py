class ModelProducts:

    @classmethod
    def insertProduct(cls, db, producto):
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO puc (nombre, valor, cantidad) VALUES (%s, %s, %s)"
            values = (producto.nombre, producto.valor, producto.cantidad)
            cursor.execute(sql, values)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)