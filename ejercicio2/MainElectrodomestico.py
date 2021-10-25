from Electrodomestico import Electrodomestico
from Lavadora import Lavadora
from Television import Television

def es4k(fourk):
    if fourk.lower() == "s":
        return True
    elif fourk.lower() == "n":
        return False
def electrodomesticosimple(listaelectrodomesticos):
    precio_base=int(input("Introduzca un precio base"))
    color=input("Introduzca color")
    consumo_ener=input("Introduzca tipo de consumo")
    peso=int(input("Introduzca peso del electrodomestico"))
    electrodomesticosimple = Electrodomestico(precio_base,color,consumo_ener,peso)
    listaelectrodomesticos.append(electrodomesticosimple)

def electrodomesticolavadora(listaelectrodomesticos):
    preciobase=int(input("Introduzca el precio base de la lavadora"))
    color=input("Introduzca color de la lavadora")
    consumo_ener=input("Introduzca consumo energetico de la lavadora")
    peso=int(input("Introduzca peso de la lavadora"))
    carga=int(input("Introduzca carga de la lavadora"))
    electrodomesticolavadora=Lavadora(preciobase,color,consumo_ener,peso,carga)
    listaelectrodomesticos.append(electrodomesticolavadora)

def electrodomesticotelevision(listaelectrodomesticos):
    preciobase=int(input("Introduzca precio base del televisor"))
    color=input("introduzca color del televisor")
    consumo_ener=input("Introduzca consumo energetico del televisor")
    peso=int(input("Introduzca peso del televisor"))
    resolucion=int(input("Introduzca la resolucion del televisor"))
    fourk=input("Introduzca s si es 4k de lo contrario introduzca n")
    fourk=es4k(fourk)
    electrodomesticotelevision=Television(preciobase,color,consumo_ener,peso,resolucion,fourk)
    listaelectrodomesticos.append(electrodomesticotelevision)

def ingresostotales(listaelectrodomesticos):
    beneficiostotales=0.0
    beneficioselectrodomesticos=0.0
    beneficioslavadoras=0.0
    beneficiostelevisiones=0.0

    for x in range(0,len(listaelectrodomesticos)):
        electrodomestico=listaelectrodomesticos[x]
        if type(electrodomestico) is Electrodomestico:
            beneficioselectrodomesticos+=float(electrodomestico.preciofinal())
            beneficiostotales+=float(electrodomestico.preciofinal())
        elif type(electrodomestico) is Lavadora:
            beneficioslavadoras+=float(electrodomestico.preciofinal())
            beneficiostotales += float(electrodomestico.preciofinal())
        elif type(electrodomestico) is Television:
            beneficiostelevisiones+=float(electrodomestico.preciofinal())
            beneficiostotales += float(electrodomestico.preciofinal())
    return "Beneficios totales=" +str(beneficiostotales)+\
           "\nBeneficios electrodomesticos simples=" +str(beneficioselectrodomesticos)+\
           "\nBeneficios lavadoras=" +str(beneficioslavadoras)+\
           "\nBeneficios televisiones=" +str(beneficiostelevisiones)

if __name__ == "__main__":
   listaelectrodomesticos = []

   for i in range(10):
       tipoelectrodomestico = 0
       while tipoelectrodomestico < 1 or tipoelectrodomestico > 3:
           print("Introduce el tipo de electrodomestico que desea")
           tipoelectrodomestico=int(input("1: Electrodomestico simple \n"
                                          "2: Lavadora \n"
                                          "3: Television \n"))
           if tipoelectrodomestico <1 or tipoelectrodomestico >3:
               print("Error introduzca una opcion validad")
       if tipoelectrodomestico == 1:
           electrodomesticosimple(listaelectrodomesticos)
       elif tipoelectrodomestico == 2:
           electrodomesticolavadora(listaelectrodomesticos)
       elif tipoelectrodomestico ==3:
           electrodomesticotelevision(listaelectrodomesticos)
   print("Los electrodomesticos son:")
   for i in range(0,len(listaelectrodomesticos)):
       electrodomestico=listaelectrodomesticos[i]
       print(electrodomestico.toString())

   print(ingresostotales(listaelectrodomesticos))