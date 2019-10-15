print("MULTIPLOS DE UN RANGO DE NUMEROS")

comprobar = True

while comprobar == True:
    n = int(input("Numero a encontrar multiplo: "))
    if n > 0:
      while comprobar == True:
         n2 = int(input("Rango de numero a mostrar: "))
         if n2 > 0:
            print(f"Los multiplos de {n} son:")
            for i in range(1,n2+1):
                print(n*i," , ", end='')

            comprobar = False
         else:
            print("Numero incorrecto, intente de nuevo")

    else:
        print("Numero incorrecto, intentelo de nuevo")
