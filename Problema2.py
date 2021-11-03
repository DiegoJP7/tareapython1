print("-Programa para calcular la nota final de un estudiante- \n")

nombre = input ("Ingresar el nombre del estudiante: ")
print("Estudiante " + nombre + " registrado" "\n")


#Datos y proceso

print("Ingrese la nota de los trabajos: ")
A = float(input())
if A > 10:
    print("!!La nota es sobre 10 puntos!!")
    print("**Ingrese la nota otra vez**")
    print ("")
nTrabajos = A * 20/100
print("-----------------------------------------------")

print("Ingrese la nota de las lecciones: ")
B = float(input())
if B > 10:
    print("!!La nota es sobre 10 puntos!!")
    print("**Ingrese la nota otra vez**")
    print ("")
nLecciones = B * 30/100
print("-----------------------------------------------")

print("Ingrese la nota de las participaciones: ")
C = float(input())
if C > 10:
    print("!!La nota es sobre 10 puntos!!")
    print("**Ingrese la nota otra vez**")
    print ("")
nParticipaciones = C * 10/100
print("-----------------------------------------------")

print("Ingrese la nota del examen final: ")
D = float(input())
if D > 10:
    print("!!La nota es sobre 10 puntos!!")
    print("**Ingrese la nota otra vez**")
    print ("")
nExmfinal = D * 40/100
print("-----------------------------------------------")


nTotal = nTrabajos + nLecciones + nParticipaciones + nExmfinal


print("La nota final es de: ",nTotal)
if nTotal < 6.99 :
    print("No Aprovado")
    print("")
if nTotal >= 7 and nTotal <= 10:
    print("Aprovado")
    print("")