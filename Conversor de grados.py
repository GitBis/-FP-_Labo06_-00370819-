import os #libreria para limpiar pantalla


def menu():

 os.system('cls')
 print('\n\t '"CONVERSOR DE TEMPERATURA")
 print('\n'"Elija una opcion")
 print('\n'"1 -Convertir Fahrenheit a Celsius")
 print('\n'"2 -Convertir Celsius a Fahrenheit")
 print('\n'"3 -Convertir Kelvin a Celsius ")
 print('\n'"4 -Salir")



while True:

     menu()
     
     opcion = input('\n'"Opcion: ")


     
     if opcion == "1":
         print('\n\t '"Fahrenheit a Celsius")  
         faren= float(input('\n'"Ingrese los grados Fahrenheit: "))
         celsf = (faren-32)*5/9
         print(f"{celsf}, Celsius")
         input('\n'"pulsa una tecla para continuar...")

  
 
     elif opcion == "2":
          print('\n\t '"Celsius a Fahrenheit")

          cels= float(input('\n'"Ingrese los grados Celsius: "))
          
          farenf = (cels*9/5)+32 
          print(f"{farenf}, Fahrenheit")
          input('\n'"pulsa una tecla para continuar...")


     elif opcion == "3":
          print('\n\t '"Kelvin a Celsius")

          kel= float(input('\n'"Ingrese los grados Kelvin: "))
           
          kelf = kel-273.15
          print(f"{kelf}, Kelvin")
          input('\n'"pulsa una tecla para continuar...")


     elif opcion == "4":
          break

     else:
         print("No eligio ninguna opcion, vuelva a escoger")
         input('\n'"pulsa una tecla para continuar...")


