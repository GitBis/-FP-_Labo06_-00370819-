import random

print("ADIVINA EL NUMERO")
comprobar = True
contador = 1
while comprobar == True:
    n = int(input("Ingrese un numero del 1 al 10: "))
    if n > 0 and n < 11:
        all = random.randrange(1,10)
        if n == all:
          print(all)
          print(f"numero de intentos: {contador}")
        else:
            while n != all:
                if n > all:
                   n =  int(input("¡Te pasastes! vuelve a intentar: "))
                   contador += 1
         
                elif n < all:
                     n =  int(input("¡Prueba un numero mayor! : "))
                     contador += 1
        print(f"El numero aleatorio era: {all}")
        print(f"numero de intentos: {contador}")   
             
        comprobar = False
    else:
     print("Ese no es un numero del 1 al 10 vuelve a intentar")

