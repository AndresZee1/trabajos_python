
class Cafetera:
    def __init__(self, capacidad_maxima=1000, cantidad_actual=0):
        self.capacidad_maxima = capacidad_maxima
        self.cantidad_actual = min(cantidad_actual, capacidad_maxima)

    def llenar_cafetera(self):
        self.cantidad_actual = self.capacidad_maxima

    def servir_taza(self, cantidad):
        if self.cantidad_actual >= cantidad:
            self.cantidad_actual -= cantidad
            return cantidad
        else:
            servido = self.cantidad_actual
            self.cantidad_actual = 0
            return servido

    def vaciar_cafetera(self):
        self.cantidad_actual = 0

    def agregar_cafe(self, cantidad):
        self.cantidad_actual = min(self.capacidad_maxima, self.cantidad_actual + cantidad)
