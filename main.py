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

        def cambiarRegistro(self, registro):
          self.registro = registro

        def asignarTipo (self, tipo):
          if (tipo == "electrico" or tipo == "gasolina"):
              self.tipo = tipo

class Asiento:
       def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

       def cambiarColor(self, colour):
        listaa = ["rojo", "verde", "amarillo", "negro","blanco"]
        if colour in listaa:
            self.color = colour

