class ModelPuc:

    @classmethod
    def insertPuc(cls, db, cuenta, codigo):
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO puc (cuenta, codigo) VALUES (%s, %s)"
            values = (cuenta, codigo)
            cursor.execute(sql, values)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def showPuc(cls, db):
        try:
            cursor = db.connection.cursor()
            sql = 'SELECT * FROM puc'
            cursor.execute(sql)
            data = cursor.fetchall()
            if data != None:
                return data
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def showTablePuc(cls, db, nameTable):
        try:
            cursor = db.connection.cursor()
            sql = f'SELECT * FROM {nameTable}'
            cursor.execute(sql)
            data = cursor.fetchall()
            if data != None:
                return data
            else:
                return None
        except Exception as ex:
            raise Exception(ex)