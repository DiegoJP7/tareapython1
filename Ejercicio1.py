
print("--Programa para calcular el costo total de una llamada-- \n")
nombre = input ("Ingresar el nombre del usuario: ")
print("¡Hola " + nombre + "!")

#Ingreso de datos
print("Ingresar el tiempo de llamada en minutos: ")
duraLlam = float(input())
print("Ingresar el valor de la llamada por minutos: ")
costMinuto = float(input())

#Proceso
cosTotal = duraLlam * costMinuto

print("La duracion de la llamada es: ",duraLlam)
print("El costo por minuto de la llamada es:  ",costMinuto)
print("El costo total de la llamada es:    ",cosTotal)

