from clases import calculadora 
obj = calculadora

print ("bienvenidos a la calculadora")
print ("1.- Suma")
print ("2.- Resta")
print ("3.- Multiplicar")
print ("4.- Division")
opc=input("introduce una opcion")

if opc== "1":
    numero=float(input("introduce un valor"))
    numero2=float(input("introduce otro valor"))
    sum = obj.sumar(numero, numero2)
    print= ("La suma es:",sum)

elif opc=="2":
    numero=float(input("introduce un valor"))
    numero2=float(input("introduce otro valor"))
    res= obj.Resta (numero, numero2)
    print= ("La resta es:", res)
elif opc=="3":
    numero=float(input("introduce un valor"))
    numero2=float(input("introduce otro valor"))
    mul= obj.Multiplicar (numero, numero2)
    print= ("La multiplicacion es:", mul)
elif opc=="4":
    numero=float(input("introduce un valor"))
    numero2=float(input("introduce otro valor"))
    div= obj.Division (numero, numero2)
    print= ("La division es:", div)
else :
    print("opcion no valida, por favor, seleccione una opcion del 1 al 4")