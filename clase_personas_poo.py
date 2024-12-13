
# Caracteristicas
    # Nombre
    # Apelllidos
    # edad
    # direccion

# funcionalidades
    # hablar
    # comer
    # dormir   
    # trabajar

# _INIT_ se utiliza para inicializar los atributos de la clase. Los métodos hablar, comer, dormir y trabajar
class Persona:
    def __init__(self, nombre, apellidos, edad, direccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.direccion = direccion

    def hablar(self, mensaje):
        print(f"{self.nombre} dice: {mensaje}")

    def comer(self, alimento):
        print(f"{self.nombre} está comiendo {alimento}")

    def dormir(self):
        print(f"{self.nombre} está durmiendo")

    def trabajar(self):
        print(f"{self.nombre} está trabajando")

# Pedir al usuario que ingrese los datos de la persona
nombre = input("Ingresa el nombre de la persona: ")
apellidos = input("Ingresa los apellidos de la persona: ")
edad = int(input("Ingresa la edad de la persona: "))
direccion = input("Ingresa la dirección de la persona: ")

# Crear un objeto de la clase Persona con los datos ingresados por el usuario
persona1 = Persona(nombre, apellidos, edad, direccion)


# Llamar a algunos métodos de la clase Persona
persona1.hablar("Hola, ¿cómo estás?")
persona1.comer("una pizza")
persona1.dormir()
persona1.trabajar()
