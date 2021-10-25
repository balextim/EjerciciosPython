from random import randint
class Persona:
    def __init__(self, nombre="", edad=0, dni="", sexo="M", peso=0.0, altura=0.0):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura

    def setnombre(self, nombre):
        self.__nombre = nombre

    def setedad(self, edad):
        self.__edad = edad

    def setsexo(self, sexo):
        self.__sexo = sexo

    def setpeso(self, peso):
        self.__peso = peso

    def setaltura(self, altura):
        self.__altura = altura

    def getnombre(self):
        return self.__nombre

    def getedad(self):
        return self.__edad

    def getsexo(self):
        return self.__sexo

    def getpeso(self):
        return self.__peso

    def getaltura(self):
        return self.__altura

    def getdni(self):
        return self.__dni

    # método para calcular el IMC
    def calcularimc(self):
        x = 2
        if float(self.__peso) ==0 or float(self.__altura) ==0:
            return 0,x
        imc = float(self.__peso) / (float(self.__altura) * float(self.__altura))
        if imc >= 0 and imc <= 18.50:
            x = -1
        elif imc > 18.50 and imc <= 25:
            x = 0
        elif imc > 25:
            x = 1
        return imc, x

    # método para saber si es mayor de edad
    def esmayor(self):
        if int(self.__edad) > 18:
            return 1
        else:
            return -1

    # metodo para comprobar si el sexo es corrrecto
    def comprobarsexo(self):
        if self.__sexo != 'H' or self.__sexo != 'M':
            self.setsexo("M")

    # metodo para visualizar la  informacion del objeto
    def tostring(self):
        return "Nombre:" + self.__nombre + " Edad:" + str(self.__edad) + " Dni:" + str(self.__dni) + " Sexo:" + self.__sexo +\
               " Peso:" + str(self.__peso) + " Altura:" + str(self.__altura)

    # metodo para generar el dni del objeto
    def generadni(self):
        listanumeros = []
        for i in range(8):
            cifradni = randint(0, 9)
            listanumeros.append(str(cifradni))
        dni = ''
        for i in range(8):
            dni = dni + listanumeros[i]
        return dni

    def calcularletradni(self, dniaux):
        lista = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q',
                 'V', 'H', 'L', 'C', 'K', 'E']
        dnin=int(dniaux)
        letra=lista[dnin%23]
        dnil = str(dnin) + letra
        return str(dnil)

