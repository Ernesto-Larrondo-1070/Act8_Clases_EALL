class informacion:

    
    def mi_lista(self):
        lista_Nomperros=["boby","julian","molly"]
        for x in lista_Nomperros:
            print(x)

    def mi_tupla(self):
        tuplaamigos=["Edgar","Emi","justhin"]
        for x in tuplaamigos:
            print(x)

    def mi_set(self):
        misetfam=["pablo","zullyban","paty"]
        for x in misetfam:
            print(x)       

    def thisdict(self):
        thisdic =	{
    "cherry --": "cereza",
    "Watermelon --": "sandia",
    "apple --": "manzana"
}
        for x,y in thisdic.items():
            print(x,y)

#Creando el objeto}

datos= informacion()
print("---------Listado de nombre de perros---------")
datos.mi_lista()
print("---------Listado de mis amigos---------------")
datos.mi_tupla()
print("---------Listado de familias-----------------")
datos.mi_set()
print("---------Listado de nombres en ingles--------")
datos.thisdict()


