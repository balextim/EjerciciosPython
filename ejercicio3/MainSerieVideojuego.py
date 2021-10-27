from Serie import Serie
from Videojuego import Videojuego

def entregarSerie(listaSeries):
    posicion = buscarTituloSerie(listaSeries)
    if posicion == -1:
        print("El nombre introducido no se encuentra registrado")
    else:
        listaSeries[posicion].setentregado(True)
        print("El registro ha sido modificado")
def entregarVideojuego(listaVideojuegos):
    posicion=buscarTituloVideojuego(listaVideojuegos)
    if posicion==-1:
        print("El nombre del videojuego introducido no se encuentra registrado")
    else:
        listaVideojuegos[posicion].setentregado(True)
        print("El registro ha sido modificado")
def devolverSerie(listaSeries):
    posicion = buscarTituloSerie(listaSeries)
    if posicion == -1:
        print("El nombre del videojuego no se encuentra registrado")
    else:
        listaSeries[posicion].setentregado(False)
def devolverVideojuego(listaVideojuegos):
    posicion = buscarTituloVideojuego(listaVideojuegos)
    if posicion == -1:
        print("El videojuego no se encuentra registrado")
    else:
        listaVideojuegos[i].setentregado(False)
        print("El registro ha sido modificado")
def buscarTituloSerie(listaSeries):
    nombre = input("Introduzca el nombre de la Serie a entregar o devolver")
    for i in range(0,len(listaSeries)):
        if (listaSeries[i].gettitulo().lower()==nombre.lower()):
            return i
    return -1
def buscarTituloVideojuego(listaVideojuegos):
    nombre=input("Introduzca el nombre del videojuego a entregar o devolver")
    for i in range(0, len(listaVideojuegos)):
        if (listaVideojuegos[i].gettitulo().lower()==nombre.lower()):
            return i
    return -1

def contarSeriesEntregadas(listaseries):
    numSeriesEntregadas = 0
    for i in range(0, len(listaseries)):
        if(listaseries[i].getentregado()==True):
            numSeriesEntregadas+=1
    return numSeriesEntregadas

def contarVideojuegosEntregados(listaVideojuegos):
    numVideojuegosEntregados=0
    for i in range(0, len(listaVideojuegos)):
        if(listaVideojuegos[i].getentregado()==True):
            numVideojuegosEntregados+=1
    return numVideojuegosEntregados

def mayorNumeroTemporadas(listaseries):
    mayorNumeroTemporadas=0
    for i in range(0, len(listaseries)):
        if listaseries[i].getnumerotemporadas() > mayorNumeroTemporadas:
            mayorNumeroTemporadas=listaseries[i].getnumerotemporadas()
    return mayorNumeroTemporadas

def mayorNumeroHoras(listaVideojuegos):
    mayorNumeroHoras=0
    if(listaVideojuegos[i].gethorasestimadas()>mayorNumeroHoras):
        mayorNumeroHoras=listaVideojuegos[i].gethorasestimadas()
    return mayorNumeroHoras

if __name__ == "__main__":
    listaSeries = []
    listaVideojuegos = []

    serie1= Serie("El juego",3,True,"Accion","Nose")
    listaSeries.append(serie1)
    serie2= Serie("LQSA",13,False,"comedia","")
    listaSeries.append(serie2)
    serie3= Serie("Serie3",5,False,"","")
    listaSeries.append(serie3)
    serie4= Serie("Serie4",2,True,"Miedo","Joel")
    listaSeries.append(serie4)
    serie5= Serie("BH",12,True,"Ficcion","Dani")
    listaSeries.append(serie5)
    video1 = Videojuego("Assasins",30,True,"Accion","")
    listaVideojuegos.append(video1)
    video2 = Videojuego("DBZ",20,True,"Ficcion","Sony")
    listaVideojuegos.append(video2)
    video3 = Videojuego("VJ3",12,False,"Belico","Sony")
    listaVideojuegos.append(video3)
    video4 = Videojuego("Crash",20,True,"Accion","Nintendo")
    listaVideojuegos.append(video4)
    video5 = Videojuego("Mario",30,False,"Fantasia","Nintendo")
    listaVideojuegos.append(video5)

    print("Video Series")
    for i in range(0,len(listaSeries)):
        contenido=listaSeries[i]
        print(contenido.toString())

    print("Videojuegos")
    for i in range(0,len(listaVideojuegos)):
        contenido=listaVideojuegos[i]
        print(contenido.toString())

    entregarSerie(listaSeries)
    entregarVideojuego(listaVideojuegos)
    devolverSerie(listaSeries)
    devolverVideojuego(listaVideojuegos)
    print("El numero de series entregadas es:" +str(contarSeriesEntregadas(listaSeries)))
    print("El numero de juegos entregados es:" +str(contarVideojuegosEntregados(listaVideojuegos)))
    print("La serie con mayor temporadas contiene:" +str(mayorNumeroTemporadas(listaSeries))+ " temporadas")
    print("El videojuego con mayor horas de juego contiene:" +str(mayorNumeroHoras(listaVideojuegos))+ " horas de juego")