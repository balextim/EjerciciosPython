class Electrodomestico:
    def __init__(self, precio_base=100, color="Blanco", consumo_ener="F", peso=5.0):
        self.__precio_base = precio_base
        self.__color = color
        self.comprobarcolor()
        self.__consumo_ener = consumo_ener
        self.comprobarconsumoenergetico()
        self.__peso = peso

    def getpre_base(self):
        return self.__precio_base

    def getcolor(self):
        return self.__color

    def getconsumo_ener(self):
        return self.__consumo_ener

    def getpeso(self):
        return self.__peso

    def comprobarconsumoenergetico(self):
        listaletras = ["A", "B", "C", "D", "E", "F"]
        i=0
        while str(self.__consumo_ener).lower() != listaletras[i].lower():
            if (i==5):
                i+=1
                break
            else:
                i+=1
        if (i ==6):
            self.__consumo_ener="F"

    def comprobarcolor(self):
        listacolores = ["Blanco", "Negro", "Rojo", "Azul", "Gris"]
        i=0
        while self.__color.lower() != listacolores[i].lower():
            if(i==4):
                i+=1
                break
            else:
                i+=1
        if(i==5):
            self.__color = "Blanco"

    def preciofinal(self):
        precio_final=0.0
        if self.__consumo_ener.lower()=="a":
            precio_final=float(self.__precio_base) + 100
        elif self.__consumo_ener.lower()=="b":
            precio_final=float(self.__precio_base) + 80
        elif self.__consumo_ener.lower()=="c":
            precio_final=float(self.__precio_base) + 60
        elif self.__consumo_ener.lower() == "d":
            precio_final=float(self.__precio_base) + 50
        elif self.__consumo_ener.lower() == "e":
            precio_final=float(self.__precio_base) + 30
        elif self.__consumo_ener.lower() == "f":
            precio_final=float(self.__precio_base) + 10
        if float(self.__peso) >= 0.0 and float(self.__peso) <= 19.0:
            precio_final=precio_final + 10
        elif float(self.__peso) >= 20.0 and float(self.__peso) <= 40.0:
            precio_final=precio_final + 50
        elif float(self.__peso) >= 41.0 and float(self.__peso) <= 79.0:
            precio_final=precio_final + 80
        elif float(self.__peso) > 80.0:
            precio_final=precio_final + 100
        return str(precio_final)
    def toString(self):
        return "Precio base="+str(self.__precio_base)+ " Color=" +self.__color+ " Consumo Energético=" +self.__consumo_ener+\
               " Peso=" +str(self.__peso)+ " Precio final=" +self.preciofinal()
