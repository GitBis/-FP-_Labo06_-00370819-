print("TABLA DE MULTIPLICAR")


comprobar = True

while comprobar == True:
      n = int(input("Ingrese un numero entero: "))
      if n > 0:
          for i in range(1,11):
             print(n, " x  ", i, " = ", n*i)
          comprobar = False
      else:
          print("El numero ingresado no es entero. Intentelo nuevamente")
      