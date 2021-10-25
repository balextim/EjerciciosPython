from clasepersona import Persona


def estadofisico(x):
    if x==2:
        return "Error no se puede dividir por cero"
    if x == -1:
        return persona1.getnombre() + " Usted padece delgadez"
    elif x == 0:
        return persona1.getnombre() + " Usted está en su peso ideal"
    elif x == 1:
        return persona1.getnombre() + " Usted padece sobrepeso"
def comprobaredad(edad):
    if edad ==1:
        return "es mayor de edad"
    else:
        return "es menor de edad"

if __name__ == "__main__":
    nombre=input("Introduzca nombre")
    edad=input("introduzca la edad")
    dni=Persona.generadni(0)
    dniaux=Persona.calcularletradni("",dni)
    sexo=input("Introduzca H si eres hombre o M si eres mujer")
    peso=(input("Introduzca su peso en kilogramos"))
    altura=(input("Introduzca su altura en metros"))
    persona1=Persona(nombre,edad,str(dniaux),sexo,peso,altura)
    persona2=Persona(nombre,edad,str(dniaux),sexo)
    persona3=Persona()
    edad=persona1.esmayor()
    print(comprobaredad(edad))
    imc, x = persona1.calcularimc()
    print(estadofisico(x))
    print("Su índice de masa corporal es " + str(imc))
    edad=persona2.esmayor()
    print(comprobaredad(edad))
    imc, x = persona2.calcularimc()
    print(estadofisico(x))
    print("Su índice de masa corporal es " +str(imc))
    edad=persona3.esmayor()
    print(comprobaredad(edad))
    imc, x = persona3.calcularimc()
    print(estadofisico(x))
    print("Su índice de masa corporal es " +str(imc))
    print(persona1.tostring())
    print(persona2.tostring())
    print(persona3.tostring())



