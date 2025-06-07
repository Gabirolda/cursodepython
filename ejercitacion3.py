#dados tres numero determinar cual es mayor

numero1 = int(input("Ingrese un numero:"))
numero2 = int(input("Ingrese un numero:"))
numero3 = int(input("Ingrese un numero:"))

if numero1 > numero2 and numero1 > numero3:
    print("El numero mayor es: " ,numero1, )
elif numero2 > numero1 and numero2 >numero3:
    print("El numero mayor es: " ,numero2,)
else: print("El numero mayor es: " ,numero3,)