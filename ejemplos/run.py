# Crear dos objetos de la clase 01

from mis_clases import Trabajador

# Crear objeto 01
print("\nDATOS DEL 1er OBJETO")
profesor1 = Trabajador("Juan", "Jácome", "0705936874", 450.00) 
# Presentar objeto; usar el método __st__
print(profesor1)


# Objeto 02
# Crear ingresando valores por teclado
print("\nINGRESE LOS DATOS DEL 2do OBJETO")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
cedula = input("Ingrese su identificación: ")
sueldo_basico =  float(input("Ingrese su sueldo: "))

profesor2 = Trabajador(nombre, apellido, cedula, sueldo_basico)  

# Presentar objeto; usar el método __st__
print("\nDATOS DEL 2do OBJETO")
print(profesor2)
