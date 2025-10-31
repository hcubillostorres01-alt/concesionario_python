from vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self, marca, modelo, precio_base, cilindraje):
        super().__init__(marca, modelo, precio_base)
        self.__cilindraje = max(cilindraje, 1)  # Validación: cilindraje > 0

    # Implementación del método abstracto
    def calcular_impuesto(self):
        # Si el cilindraje es menor o igual a 250 → 5%
        # Si es mayor a 250 → 9%
        tasa = 0.05 if self.__cilindraje <= 250 else 0.09
        return self.get_precio_base() * tasa

    # Sobrescribimos el método ficha
    def ficha(self):
        return f"Moto - {super().ficha()} | Cilindraje: {self.__cilindraje}cc"

    # Sobrescribimos __str__()
    def __str__(self):
        return f"{self.ficha()} | Precio final: ${self.calcular_precio_final():,.2f}"
