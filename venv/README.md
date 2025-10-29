# Proyecto Concesionario - Actividad 8  
**Curso:** Lenguaje de Programación II  
**Estudiante:** Humberto Cubillos Torres  
**Programa:** Ingeniería de Software (Modalidad Virtual)  
**Institución:** Universidad de La Salle - Colombia  
**Fecha:** Octubre 2025  

---

Descripción del Proyecto
Este proyecto implementa un sistema de **concesionario de vehículos** aplicando los cuatro pilares de la **Programación Orientada a Objetos (POO)**:  
- **Encapsulamiento**: Los atributos de cada clase son privados y se accede a ellos mediante métodos `get`.  
- **Herencia**: Las clases `Automovil` y `Moto` heredan de la clase abstracta `Vehiculo`.  
- **Abstracción**: La clase `Vehiculo` define un método abstracto `calcular_impuesto()` que es implementado por sus clases hijas.  
- **Polimorfismo**: Se crea una lista de vehículos que mezcla automóviles y motos, demostrando cómo cada objeto puede comportarse según su tipo.

---

Clases Principales
- **vehiculo.py** → Clase abstracta base con atributos comunes (marca, modelo, precio base).  
- **automovil.py** → Hereda de `Vehiculo` y añade el atributo `puertas`.  
- **moto.py** → Hereda de `Vehiculo` y añade el atributo `cilindraje`.  
- **concesionario_main.py** → Clase principal que crea la lista de vehículos, muestra la información y calcula el total del inventario.  

---

## ⚙️ Requisitos
- Python 3.10 o superior  
- Editor recomendado: Visual Studio Code  

---

## ▶️ Cómo Ejecutar el Programa
1. Abre el proyecto en **Visual Studio Code**.  
2. Asegúrate de tener Python instalado y configurado.  
3. Abre una terminal en la carpeta del proyecto.  
4. Ejecuta el archivo principal con el siguiente comando:

```bash
python concesionario_main.py
