#          Metodos def 
#  __init__    inicializa 
#  __str__
# __repr__
# __len__
# __getitem__
# __setitem__


# Ejemplo de __str__
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre} tiene {self.edad} años"

persona = Persona("Juan", 25)
print(persona)  # Salida: Juan tiene 25 años

# Ejemplo de __repr__ 
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __repr__(self):
        return f"Persona({self.nombre}, {self.edad})"

persona = Persona("Juan", 25)
print(repr(persona))  # Salida: Persona(Juan, 25)

# Ejemplo de __len__ el puesto cero no cuenta
class Lista:
    def __init__(self, elementos):
        self.elementos = elementos

    def __len__(self):
        return len(self.elementos)
# le entrega funcionalidades a Lista
lista = Lista([1, 2, 3, 4, 5])
print(len(lista))  # Salida: 5

# Ejemplo de __getitem__
# indice directo
class Lista:
    def __init__(self, elementos):
        self.elementos = elementos

    def __getitem__(self, indice):
        return self.elementos[indice]

lista = Lista([1, 2, 3, 4, 5])
print(lista[2])  # Salida: 3

# Ejemplo de __setitem__
# sustitucion de valor 
class Lista:
    def __init__(self, elementos):
        self.elementos = elementos

    def __setitem__(self, indice, valor):
        self.elementos[indice] = valor

lista = Lista([1, 2, 3, 4, 5])
lista[2] = 10
print(lista.elementos)  # Salida: [1, 2, 10, 4, 5]
