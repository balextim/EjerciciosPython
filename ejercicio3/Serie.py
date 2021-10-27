
class Serie:
    def __init__(self, titulo="Desconocido", numtemporadas=3, entregado=False, genero="Desconocido", creador="Desconocido"):
        self.__titulo=titulo
        self.__numtemporadas=numtemporadas
        self.__entregado=entregado
        self.__genero=genero
        self.__creador=creador

    def gettitulo(self):
        return self.__titulo

    def getnumerotemporadas(self):
        return self.__numtemporadas

    def getentregado(self):
        return self.__entregado

    def getgenero(self):
        return self.__genero

    def getcreador(self):
        return self.__creador

    def settitulo(self, titulo):
        self.__titulo=titulo

    def setnumertemporadas(self, numerotemporadas):
        self.__numtemporadas=numerotemporadas

    def setentregado(self,entregado):
        self.__entregado=entregado

    def setgenero(self, genero):
        self.__genero=genero

    def setcreador(self, creador):
        self.__creador=creador

    def toString(self):
        return "Titulo:" +self.__titulo+ " Numero temporadas:" +str(self.__numtemporadas)+ " Entregado:" +str(self.__entregado)+\
               " Genero:" +self.__genero+ " Creador:" +self.__creador