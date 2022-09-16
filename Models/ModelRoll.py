from werkzeug.security import generate_password_hash


class ModelRoll:

    @classmethod
    def insertRoll(cls, db, roll, password):
        try:
            password_hash = generate_password_hash(password)
            cursor = db.connection.cursor()
            sql = "INSERT INTO rolls (roll, password) VALUES (%s, %s)"
            values = (roll, password_hash)
            cursor.execute(sql, values)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def showRolls(cls, db):
        try:
            cursor = db.connection.cursor()
            sql = 'SELECT * FROM rolls'
            cursor.execute(sql)
            data = cursor.fetchall()
            if data != None:
                return data
            else:
                return None
        except Exception as ex:
            raise Exception(ex)