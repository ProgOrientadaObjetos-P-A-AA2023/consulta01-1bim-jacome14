# Crear dos objetos de la clase 02

from mis_clases import CalcularSueldo

# Crear objeto 01
print("\nDATOS DEL 1er OBJETO")
usuario1 = CalcularSueldo("Alexander", "López", 20, "Ecuatoriana","1478545202" ,\
                           25, 20.00) 
usuario1.calcular()
# Presentar objeto; usar el método __st__
print(usuario1)


# Objeto 02
# Crear ingresando valores por teclado
print("\nINGRESE LOS DATOS DEL 2do OBJETO")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad =  int(input("Ingrese su edad: "))
cedula = input("Ingrese su identificación: ")
nacionalidad = input("Ingrese su nacionalidad: ")
dias_trabajados =  int(input("Ingrese los dias trabajados: "))
costo_dia =  float(input("Ingrese el costo del día de trabajo: "))

usuario2 = CalcularSueldo(nombre, apellido, edad, nacionalidad, cedula,\
                           dias_trabajados, costo_dia) # Segundo objeto
usuario2.calcular()

# Presentar objeto; usar el método __st__
print("\nDATOS DEL 2do OBJETO")
print(usuario2)
