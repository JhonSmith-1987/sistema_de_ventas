class ModelTable:

    # @classmethod
    # def modelo(cls, db, table_name):
    #     cursor = db.connection.cursor()
    #     sql = f"""CREATE TABLE `{table_name}`(
    #                         id int(10) AUTO_INCREMENT PRIMARY KEY,
    #                         debe VARCHAR(50),
    #                         haber VARCHAR(50)
    #                     )"""
    #     cursor.execute(sql)
    #     db.connection.commit()

    @classmethod
    def tablePuc(cls, db, table_name):
        cursor = db.connection.cursor()
        sql = f"""CREATE TABLE `{table_name}`(
                        id int(10) AUTO_INCREMENT PRIMARY KEY,
                        fecha VARCHAR(50),
                        detalle VARCHAR(50),
                        debe VARCHAR(50),
                        haber VARCHAR(50)
                    )"""
        cursor.execute(sql)
        db.connection.commit()
