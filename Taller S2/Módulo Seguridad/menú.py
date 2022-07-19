from submenu import SubMenu
import re
from usuario import Usuario
from validar import Validar
import time
import os


sub = SubMenu()
lista = ["1).Usuario ","2).Administrador","3).Salir"]
alternativa = ""  
while alternativa != "3":
    os.system("cls")
    alternativa = sub.menuprincipal(lista,"Módulo de Seguridad") 
    if alternativa == "1":
        alternativa1 = ""
        while alternativa1 != "2":
            os.system("cls")
            alternativa1 = sub.menu(["1) Verificación de Usuario","2) Salir"],"Opciones de Usuario")
            os.system("cls")
            print("*"*15,"Identifíquese","*"*15)
            if alternativa1 == "1":
                while True:
                    correo = input("Ingrese un correo: ")
                    cor = Validar.Validarcorreo(correo)
                    if cor == True:
                        print("Correo válido")
                        os.system("cls")
                        break
                    else:
                        print("Correo no válido")
                        os.system("cls")
                    
                
                while True:
                    cédula = input("Ingresar número de cédula: ")
                    ced = Validar.Validarced(cédula)
                    if  ced == True:
                        if len(cédula) == 10:
                            print("-"*2,"Cédula Correcta","-"*2)  
                            time.sleep(0.6) 
                            os.system("cls")
                            break

                while alternativa1 != "5":
                
                    alternativa1 = sub.menu(["1).Ingresar datos", "2).Mostrar datos", "3).Actualizar datos","4).Salir"],"Opciones de Usuario")
                            
                    if alternativa1 == "1": 
                            os.system("cls")
                            nombre = input("Ingrese su nombre: ")
                            apellido = input("Ingrese su primer apellido: ")
                            dirección = input("Ingrese su dirección: ")
                                
                            metod = Usuario(nombre, apellido, cédula, dirección)
                            usuario = metod.registro1()
                            Usuario.usuario.append(usuario)
                            os.system("cls")

                            input("Presione una tecla para continuar...")
                            time.sleep(0.5)
                            os.system("cls")
        
                        

                    elif alternativa1 == "2": 
                        os.system("cls")
                        print("*"*70)
                        print(" "*5,"Nombre"," "*8,"Apellido"," "*7,"Cédula"," "*9,"Dirección")
                        for metod in Usuario.usuario:
                            nom = metod["Nombre"]
                            ape = metod ["Apellido"]
                            ced = metod ["Cédula"]
                            dir = metod["Dirección"]

                            print(" "*6,nom," "*10,ape," "*(11-len(nom)),ced," "*(19-len(ced)),dir)
                        
                        print("*"*70)
                        input("Presione una tecla para continuar...")
                        os.system("cls")
        
                       

                    elif alternativa1 == "3": 
                        os.system("cls")
                        for metod in Usuario.usuario:
                            metod["Nombre"] = "Alejandro"
                            print(metod)

                         
                    
                    elif alternativa1 == "4":
                        pass
                    
                        

    if alternativa == "2":
        alternativa1 = ""
        while alternativa1 != "2":
            os.system("cls")
            alternativa1 = sub.menu(["1) Verificación de Administrador","2) Salir"],"Opciones de Administración")
            os.system("cls")
            print("*"*15,"Identifíquese","*"*15)
            if alternativa1 == "1":
                while True:
                    correo = input("Ingrese un correo: ")
                    cor = Validar.Validarcorreo(correo)
                    if cor == True:
                        print("Correo válido")
                        os.system("cls")
                        break
                    else:
                        print("Correo no válido")
                        os.system("cls")
                    
                
                
                while True:
                    cédula = input("Ingresar clave: ")
                    ced = Validar.Validarced(cédula)
                    if  ced == True:
                        if len(cédula) == 10:
                            print("-"*2,"Clave Correcta","-"*2)  
                            time.sleep(0.6) 
                            os.system("cls")
                            break


                while alternativa1 != "5":
                
                    alternativa1 = sub.menu(["1).Ingresar datos", "2).Mostrar datos", "3).Actualizar datos", "4).Eliminar datos","5).Salir"],"Opciones de Administrador")
                            
                    if alternativa1 == "1":
                            os.system("cls")
                            nombre = input("Ingrese su nombre: ")
                            apellido = input("Ingrese su primer apellido: ")
                            dirección = input("Ingrese su dirección: ")
                                
                            metod = Usuario(nombre,apellido, cédula, dirección)
                            usuario = metod.registro1()
                            Usuario.usuario.append(usuario)
                            os.system("cls")

                            input("Presione una tecla para continuar...")
                            time.sleep(0.5)
                            os.system("cls")
        


                    elif alternativa1 == "2":
                        os.system("cls")
                        print("*"*70)
                        print(" "*5,"Nombre"," "*8,"Apellido"," "*7,"Cédula"," "*9,"Dirección")
                        for metod in Usuario.usuario:
                            nom = metod["Nombre"]
                            ape = metod ["Apellido"]
                            ced = metod ["Cédula"]
                            dir = metod["Dirección"]

                            print(" "*6,nom," "*8,ape," "*(11-len(nom)),ced," "*(19-len(ced)),dir)
                        
                        
                        print("*"*70)
                        input("Presione una tecla para continuar...")
        
                       

                    elif alternativa1 == "3":
                        pass
                        


                    elif alternativa1 == "4":
                        pass
                    elif alternativa1 == "5":
                        print("Salir del ")





    if alternativa == "3":
        os.system("cls")
        print("Saliendo del módulo...")
        time.sleep(1)        
        os.system("cls")           
                        


