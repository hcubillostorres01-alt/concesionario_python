from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca, modelo, precio_base):
        # Encapsulamiento
        self.__marca = marca
        self.__modelo = modelo
        # Validación: precio base debe ser mayor que  0 segun indicaciones dadas
        self.__precio_base = max(precio_base, 1.0)

    # Métodos GET no se permiten SET según la instrucción del profesor
    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_precio_base(self):
        return self.__precio_base

    # Método abstracto para calcular el impuesto (solo las hijas lo implementan segun lo solicitado)
    @abstractmethod
    def calcular_impuesto(self):
        pass

    # Método público para calcular el precio final
    def calcular_precio_final(self):
        return self.__precio_base + self.calcular_impuesto()

    # Método para mostrar la ficha del vehículo
    def ficha(self):
        return f"Marca: {self.__marca} | Modelo: {self.__modelo} | Precio base: ${self.__precio_base:,.2f}"

    # Método __str__ para representar el objeto como texto
    def __str__(self):
        return f"{self.ficha()} | Precio final: ${self.calcular_precio_final():,.2f}"
