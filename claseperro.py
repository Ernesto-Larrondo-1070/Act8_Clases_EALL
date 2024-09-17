print("Clases version 2 el contructor")

class Perro:
    def __init__(self, color, edad):
        self.color=color
        self.edad=edad
    # funciones creadas por el usuario
    def muerde(self):
            print("Chale el perro me mordio")
    def chatperro(self,mensaje):
            print(f"Chat perro: {mensaje} ")
    def Chatperra(self,mensajep):
            print(f"Chat perro: {mensajep} ")
    def datos(self):
            print(f"Color {self.color} edad {self.edad}")
# Crear objeto
Labrador=Perro("Negro",2)
#llamada a funciones
Labrador.datos()
Labrador.muerde()
Labrador.chatperro("Hola soy Dominc")
Labrador.Chatperra("Hola soy Emi")
Labrador.chatperro("Quieres hacerme gogo")
Labrador.Chatperra("Grrrrru......")



