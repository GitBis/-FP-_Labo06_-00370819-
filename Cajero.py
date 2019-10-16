
#  ' ' - Espacio
#   '\ t' - Pestaña horizontal
#  '\ n' - Nueva línea
#  '\ v' - Pestaña vertical
#  '\ f' - Feed
#  '\ r' - retorno de carro 

import os #libreria para limpiar pantalla


saldo = 1000

def menu():

 os.system('cls')
 print('\n\t '"CAJERO AUTOMATICO")
 print('\n\t 'f"Saldo actual: {saldo}" )
 print('\n'"Elija una opcion")
 print('\n'"1 - Deposito")
 print('\n'"2 - Retiro")
 print('\n'"3 - Salir")



while True:

     menu()
     
     opcion = input('\n'"Opcion: ")


     
     if opcion == "1":
         print('\n\t '"DEPOSITAR A SU CUENTA")  

         comprobar = True

         while comprobar == True:

             dep= float(input('\n'"Ingrese la cantidad a depositar: "))
        
             if dep > 0:

                   saldo = saldo+dep
                   print("La acción se realizó correctamente")
                   input('\n'"pulsa una tecla para continuar...")

                   comprobar = False
             else:
                   print("La cantidad es erronea, intente de nuevo")
 
     elif opcion == "2":
          print('\n\t '"RETIRAR")

          comprobar = True
          while comprobar == True:

              ret= float(input('\n'"Ingrese la cantidad a retirar: "))

              if ret > 0:
             
                   saldo = saldo-ret
                   print("La acción se realizó correctamente")
                   input('\n'"pulsa una tecla para continuar...")

                   comprobar = False
              else:
                   print("La cantidad es erronea, intente de nuevo")

     elif opcion == "3":
          break

     else:
         print("No eligio ninguna opcion, vuelva a escoger")
         input('\n'"pulsa una tecla para continuar...")


