print("Bienvenidos a la actividad 14")

class Persona:
    def __init__(self, numero_dorsal, nombre, edad, categoria):
        self.numero_dorsal = numero_dorsal
        self.nombre = nombre
        self.edad = edad
        self.categoria = categoria

    def __str__(self):
        return (f"Corsal: {self.numero_dorsal} "
                f"Nombre del Competidor: {self.nombre}"
                f"Edad del Competidor {self.edad} "
                f"Inscrito en la categoria{self.categoria}")



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
                edad = int(input("Ingrese la edad del participante"))
                categoria = input("Ingrese la categoria: (juvenil, adulto, máster")
                self.inscrito[dorsal] = Persona(dorsal, nombre, nombre, edad, categoria)
        except ValueError:
            print("No se puede ingresar los datos")

    def quick_sort(self, resultado):
        if len(resultado) <= 1:
            return resultado

        pivote = resultado[0]
        menor = [x for x in resultado if x.nombre < pivote.nombre]
        igual = [x for x in resultado if x.nombre == pivote.nombre]
        mayor = [x for x in resultado if x.nombre > pivote.nombre]

        return self.quick_sort(menor) + igual + self.quick_sort(mayor)











    def menu(self):
        print("Bienvenidos a la actividad 14")
        print("A continuacion se presenta el siguiente menú ingrese la opción que desea")
        print("1.- Agregar Participantes")
        print("2.- Mostrar participantes ordenados por nombres")

