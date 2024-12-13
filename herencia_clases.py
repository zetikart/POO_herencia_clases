class persona():
    def __init__(self, apePat, apeMat, nom):
        self.apellidoPaterno = apePat
        self.apellidoMaterno = apeMat
        self.nombres = nom

    def mostrarNombreCompleto(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)
# Reutilizar codigo 
# al incluir la clase funcion en la clase estudiante
# estudiante tiene esos atributos y caracteristica de 'class persona()'

# persona le hereda a Estudiante 
# clase hija ' class Estudiante(persona):'
# profesion va incluido dentro de esta funcion las personas que no tienen profesion se usa la 'persona'
class Estudiante(persona):
    def __init__(self,apePat,apeMat,nom,pro):
        # funcion super() heredar el constructor de la clase padre
        super().__init__(apePat, apeMat, nom)
        self.profesion = pro 

#estudiante hereda de persona apePat apeMat nom
estu1=Estudiante("torres","lopez","Juan", "ciberseguridad")

print(estu1.mostrarNombreCompleto())
print(estu1.profesion)
