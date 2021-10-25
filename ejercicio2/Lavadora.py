from Electrodomestico import Electrodomestico


class Lavadora(Electrodomestico):

    def __init__(self, precio_base=100, color="Blanco", consumo_ener="F", peso=5, carga=5):
        Electrodomestico.__init__(self, precio_base, color, consumo_ener, peso)
        self.__carga = carga

    def getcarga(self):
        return self.__carga

    def preciofinal(self):
        precio_final=Electrodomestico.preciofinal(self)
        if int(self.__carga) > 50.0:
            precio_final=float(precio_final) + 50
            return str(precio_final)
        elif int(self.__carga) <= 50.0:
            return precio_final

    def toString(self):
        return "Lavadora: Carga=" +str(self.__carga) + " " + super().toString()

