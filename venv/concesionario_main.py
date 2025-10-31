from automovil import Automovil
from moto import Moto

def main():
    # Creamos la lista de vehículos (polimorfismo)
    inventario = [
        Automovil("Toyota", "Yaris", 40000, 5),
        Moto("Honda", "CB190R", 20000, 190),
        Automovil("Mazda", "Mazda 3", 25000, 4),
        Moto("BMW", "G310R", 34000, 350),
        Moto("PULSAR", "NS400", 4200, 400),
    ]

    total_inventario = 0.0

    print("\n===== INVENTARIO DEL CONCESIONARIO =====\n")
    for vehiculo in inventario:
        print(vehiculo)
        total_inventario += vehiculo.calcular_precio_final()

    print("\n========================================")
    print(f"Valor total del inventario: ${total_inventario:,.2f}")
    print("========================================\n")

if __name__ == "__main__":
    main()
