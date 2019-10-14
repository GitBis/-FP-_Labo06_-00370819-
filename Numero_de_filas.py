print("NUMERO DE FILAS")

comprobar = True

while comprobar == True:
     n = int(input("Ingrese un numero entero: "))
     if n > 0:
       for i in range(1,n+1):
           #print(n,end=' ') imprimir en una solo fila
           for j in range(1,i+1):
               print(i,end=' ')
           print("")

       comprobar = False

     else:
       print("No es un numero entero. Vuelva a intetar")


