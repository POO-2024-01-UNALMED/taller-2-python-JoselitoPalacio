class Auto:
    cantidadcreados =0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
         self.modelo = modelo
         self.precio= precio
         self.asientos = asientos
         self.marca = marca
         self.motor = motor
         self.registro = registro

class Motor:
        def __init__(self, numeroCilindros, tipo, registro):
          self.numeroCilindros = numeroCilindros
          self.tipo = tipo
          self.registro = registro

class Asiento:
       def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

