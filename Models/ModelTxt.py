class ModelTxt:

    @classmethod
    def createConsignment(cls, fecha, detalle, valor):
        file = open(f'static/consignment/{detalle}.txt', 'a')
        file.write('Consignacion')
        file.write('\n')
        file.write(f'   Fecha: {fecha}')
        file.write('\n')
        file.write(f'   Detalle: {detalle}')
        file.write('\n')
        file.write(f'   Valor: {valor}')
        file.close()

    @classmethod
    def showConsignment(cls, db):
        try:
            cursor = db.connection.cursor()
            sql = f'SELECT * FROM consignaciones'
            cursor.execute(sql)
            data = cursor.fetchall()
            if data != None:
                return data
            else:
                return None
        except Exception as ex:
            raise Exception(ex)








