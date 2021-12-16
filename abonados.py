class Abonado:
    
    def __init__(self, numero, nombre, estado):
        self.numero = numero
        self.nombre = nombre
        self.estado = estado

    def mostrarDatos(self):
        print(self.nombre + ', Telefono: ' + str(self.numero) + ', Estado: ' + self.estado)