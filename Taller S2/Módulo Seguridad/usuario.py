import os
os.system("cls")

class Usuario: 
    
    usuario =[{"Nombre":"Dan","Apellido":"Hernan","Cédula":"123131243","Dirección":"Milagro"}]

    def __init__(self,nombre,apellido,cédula, direccion):
        self.nombre = nombre
        self.cédula = cédula 
        self.apellido = apellido  
        self.direccion = direccion
      
    
    def registro1(self):
       return ({"Nombre":self.nombre,"Apellido":self.apellido,"Cédula":self.cédula,"Dirección":self.direccion})


    



class Usuario_comun(Usuario):
    def __init__(self, nombre, apellido, dirección, cédula, clave, estado="True"):
        super().__init__(nombre, apellido, dirección, cédula)
        self.clave = clave
        self.estado = estado
        

    def registro3(self):
        super().registro3()


class Admin(Usuario):
    def __init__(self, nombre, apellido, dirección, cédula, clave, estado="False"):
        super().__init__(nombre, apellido, dirección, cédula)
        self.clave = clave
        self.estado = estado

