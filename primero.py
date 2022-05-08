import constantes

print("PRIMERA APP EN Python")
vector=[]
PI= 3.141516
numero1=43
numero2=20
radio= 5
cadena1="Cadena de texto para pruebas"
cadenaUpper="ESTO ES UNA CADENA EN UPPERCASE"
cadenaLower="esto es una cadena de lowercase"
cadenaMezclada="EsTo Es Una CAdenA tOtAlmEnTE MezcLaDA. upp3RCS53"
#arrancamos a programar
#primero vamos a mostrar todas las variables
print("Variables numericas")
cPI= str(PI)
n1= str(numero1)
n2= str(numero2)
print("Constante PI= " + cPI)
print("Variable numero1= " + n1)
print("Variable numero2= " + n2)
suma= numero1+numero2
suma= str(suma)
print("El resultado de sumar " + n1 + " + " + n2 + " = " + suma)
resta= numero1-numero2
resta= str(resta)
print("El resultado de restar " + n1 + " - " + n2 + " = " + resta )
producto= numero1*numero2;
producto=str(producto)
print("El producto " + n1 + " * " + n2 + " = " + producto)
cociente= numero1/numero2
cociente= str(cociente)
print("El cociente entre " + n1 + "/" + n2 +" = " + cociente)
cociente= numero1//numero2
cociente= str(cociente)
print("El cociente entero entre " + n1 + "/" + n2 +" = " + cociente)
area= constantes.PI* (radio**2)
print("==========================")
print("|Radio= " + str(radio))
print("|Area= " + str(area))
