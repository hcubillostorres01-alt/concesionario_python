from vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, precio_base, puertas):
        super().__init__(marca, modelo, precio_base)
        self.__puertas = max(puertas, 1)  # Validación: mínimo 1 puerta

    # método abstracto
    def calcular_impuesto(self):
        # 8% del precio base
        impuesto = self.get_precio_base() * 0.08
        # Si tiene 5 puertas, se resta el 1% del precio base
        descuento = self.get_precio_base() * 0.01 if self.__puertas == 5 else 0
        return impuesto - descuento

    # Sobrescribimos el método ficha()
    def ficha(self):
        return f"Automóvil - {super().ficha()} | Puertas: {self.__puertas}"

    # Sobrescribimos __str__()
    def __str__(self):
        return f"{self.ficha()} | Precio final: ${self.calcular_precio_final():,.2f}"
