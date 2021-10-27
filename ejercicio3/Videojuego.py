class Videojuego:
    def __init__(self, titulo="Desconocido", horasestimadas=10.0, entregado=False, genero="Desconocido", compania="Desconocida"):
        self.__titulo=titulo
        self.__horasestimadas=horasestimadas
        self.__entregado=entregado
        self.__genero=genero
        self.__compania=compania

    def gettitulo(self):
        return self.__titulo

    def gethorasestimadas(self):
        return self.__horasestimadas

    def getentregado(self):
        return self.__entregado

    def getgenero(self):
        return self.__genero

    def getcompania(self):
        return self.__compania

    def settitulo(self, titulo):
        self.__titulo=titulo

    def sethorasestimadas(self, horasestimadas):
        self.__horasestimadas=horasestimadas

    def setentregado(self, entregado):
        self.__entregado=entregado

    def setgenero(self, genero):
        self.__genero=genero

    def setcompania(self, compania):
        self.__compania=compania

    def toString(self):
        return "Titulo:" +self.__titulo+ " Horas estimadas:" +str(self.__horasestimadas)+\
               "Entregado:" +str(self.__entregado)+ " Genero:" +self.__genero+ " Compañia:" +self.__compania
