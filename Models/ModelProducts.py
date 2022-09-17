from werkzeug.utils import secure_filename
import os


class ModelProducts:

    @classmethod
    def insertProduct(cls, db, producto):
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO productos (nombre, valor, cantidad, imagen) VALUES (%s, %s, %s, %s)"
            values = (producto.nombre, producto.valor, producto.cantidad, producto.imagen)
            cursor.execute(sql, values)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def insertImage(cls, file, nombre):
        basepath = os.path.dirname(__file__)
        filename = secure_filename(file.filename)
        extension = os.path.splitext(filename)[1]
        nuevo_nombre_file = nombre + extension
        upload_path = os.path.join(basepath, 'static/img_products', nuevo_nombre_file)
        file.save(upload_path)
