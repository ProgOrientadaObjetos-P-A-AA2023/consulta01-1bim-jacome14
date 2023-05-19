"""
Crear dos clases en Python
Usted defina el nombre y los atributos
Puede usar las mismas clases usadas en Java en los ejemplos estudiados
"""

# clase 01
class Trabajador():
    nombre = ""
    apellido = ""
    cedula = ""
    sueldoBasico = 0.0
    def __init__(self, nom, ape, ced, suelBas):
        self.nombre = nom
        self.apellido = ape
        self.cedula = ced
        self.sueldoBasico = suelBas
 
    def __str__(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nCedula: {self.cedula}\nSueldo Basico: {self.sueldoBasico}\n"




# clase 02
class CalcularSueldo():        
    def __init__(self, nom, ape, ed, nac, ced, diasTra, costoDi):
        self.nombre = nom
        self.apellido = ape
        self.edad = ed
        self.nacionalidad = nac
        self.cedula = ced
        self.diasTrabajados = diasTra
        self.costoDia = costoDi

    def calcular(self):
        self.sueldo = self.diasTrabajados * self.costoDia
        
    def __str__(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nEdad: {self.edad}\n\
Nacionalidad: {self.nacionalidad}\nCedula: {self.cedula}\nDias Trabajados: {self.diasTrabajados}\n\
Costo del dia: ${self.costoDia}\nSueldo Total: ${self.sueldo}"
        