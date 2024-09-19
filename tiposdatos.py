print("***** Clases V2 Miguel Dominguez ***** \n")
# zona de clases
class datos:
    def __init__(self, estatura, peso):
        self.estatura = estatura
        self.peso = peso

# zona de cracion
    def myfunc(self):
        print("me llamo miguel y mido", self.estatura , " y peso ", self.peso ," kg \n")
        
# LISTAS
    def mi_lista(self):
        albumes = ["lyke mike","ESTRELLA","SAYONARA"]
        print(albumes)
        for y in albumes:
            print(y)
        print("\n")

# TUPLAS
    def mi_tupla(self):
        meses = ("ENERO", "FEBRERO", "MARZO")
        print(meses)
        for a in meses:
            print(a)
        print("\n")

# CONJUNTOS
    def mi_conjunto(self):
        canciones = {
        "PASAJERO": "NOVELA",
        "SATURNO": "ADIVINO",
        "CACHE": 5
        } 
        print(canciones)
        for b in canciones:
            print(b)
        print("\n")

# SETS
    def mi_sets(self):
        mariscos = {"camaron", "pulpo", "mojarra"}
        print(mariscos)
        for c in mariscos:
            print(c)

# utilizacion del objeto
x = datos (1.83, 90)
x.myfunc()
x.mi_lista()
x.mi_tupla()
x.mi_conjunto()
x.mi_sets()