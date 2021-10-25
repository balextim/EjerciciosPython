from Electrodomestico import Electrodomestico


class Television(Electrodomestico):

    def __init__(self, precio_base=100, color="Blanco", consumo_energetico="F", peso=5, resolucion=20, fourk=False):
        Electrodomestico.__init__(self, precio_base, color, consumo_energetico, peso,)
        self.__resolucion = resolucion
        self.__fourk = fourk

    def getresolucion(self):
        return self.__resolucion

    def getfourk(self):
        return self.__fourk

    def preciofinal(self):
        precio_final=Electrodomestico.preciofinal(self)
        if float(self.__resolucion) >40:
            precio_final=float(precio_final) + (float(precio_final)*30)/100
        elif float(precio_final) <=40:
            precio_final=precio_final
        if self.__fourk == True:
            precio_final=float(precio_final)+50
        elif self.__fourk == False:
            precio_final=precio_final
        return str(precio_final)
    def toString(self):
        fourk=""
        if self.__fourk == True:
            fourk="Si"
        else:
            fourk="No"
        return "Television: 4k=" +fourk+ " Pulgadas=" +str(self.__resolucion)+ " " +super().toString()