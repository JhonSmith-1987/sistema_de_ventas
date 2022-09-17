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








