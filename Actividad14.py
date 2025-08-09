print("Bienvenidos a la actividad 14")

class Persona:
    def __init__(self, numero_dorsal, nombre, edad, categoria):
        self.numero_dorsal = numero_dorsal
        self.nombre = nombre
        self.edad = edad
        self.categoria = categoria


class Carrera:
    def __init__(self):
        self.inscritos = {}

    def Agregar_Participantes(self):
        try:
            cantidad = int(input("Ingrese la cantidad de participantes que va a inscribir:"))
            for i in range(cantidad):
                print(f"Ingrese los datos del participante {i+1}:")
                dorsal = int(input("Ingrese el dorsal del participante"))
                if dorsal in self.inscritos:
                    print("Dorsal ya existente intente con otro")
                else:
                    break
                nombre = input("Ingrese el nombre del participante")









    def menu(self):
        print("Bienvenidos a la actividad 14")
        print("A continuacion se presenta el siguiente menú ingrese la opción que desea")
        print("1.- Agregar Participantes")
        print("2.- Mostrar participantes ordenados por nombres")

