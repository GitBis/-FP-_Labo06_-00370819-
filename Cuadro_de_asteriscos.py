print("DIBUJA UN CUADRO DE ASTERISCOS")

comprobar = True

while comprobar == True:
    n = int(input("Ingrese un numero entero y dibuje su cuadro: "))
    if n > 0:
      for i in range(n,n+n):
          for j in range(n,n+n):
            print("*",end=' ')
          print("")

      comprobar = False

    else:
      print("El numero ingresado no es correcto. Intentelo de nuevo")
