class Products:

    def __init__(self, nombre, valor, cantidad, imagen):
        self.nombre = nombre
        self.valor = valor
        self.cantidad = cantidad
        self.imagen = imagen

    def __str__(self):
        return f"""
                nombre: {self.nombre}
                valor: {self.valor}
                cantidad: {self.cantidad}
                imagen: {self.imagen}
            """