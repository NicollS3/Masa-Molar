"""Masa molar
Calcule la masa molar del ácido sulfúrico H2SO4,(H = 1)
(S = 32)y(O = 16)
Donde:
Ac = Ácido sulfúrico
H = Hidrogeno
S = Azufre
O = Oxigeno"""

#Crear la clase
class MasaMolar:
    #Ingresar los atributos
    def __init__(self):
        self.Hidrogeno =int(input("Ingrese el valor del Hidrogeno:"))
        self.Azufre =int(input("Ingrese el valor del Azufre:"))
        self.Oxigeno =int(input("Ingrese el valor del Oxigeno:"))
        
    #Metodos
    def masa_molar(self):
        self.H =(self.Hidrogeno * 2)
        self.A=(self.Azufre * 1)
        self.O=( self.Oxigeno * 4)
        self.molar =(self.H)+(self.A)+(self.O)
      
    def mostrar_datos(self):
        print("La masa molar es:",self.molar,'g/mol')
    def imprimir(self):
        return print("Fin del programa")

    #Crear el objeto
mm = MasaMolar()
#Instanciar la clase
print()
print("Los datos son:")
mm.masa_molar()
mm.mostrar_datos()
mm.imprimir()
