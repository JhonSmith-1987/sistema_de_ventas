class Products:

    def __init__(self, nombre, valor, cantidad):
        self.nombre = nombre
        self.valor = valor
        self.cantidad = cantidad

    def __str__(self):
        return f"""
                nombre: {self.nombre}
                valor: {self.valor}
                cantidad: {self.cantidad}
            """