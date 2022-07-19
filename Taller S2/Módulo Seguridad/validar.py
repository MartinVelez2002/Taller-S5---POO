import re


class Validar:

    def Validarced():
        pass

    def Validarcorreo():
        pass


    def Validarced(ced):
        ced2 = ced.isdigit()
        if ced2 == True:
            return True
        else:
            return False

    def Validarcorreo(correo):
        if re.match('^[(a-z0-9\_\-\.)]+@[gmail,hotmail,outlook,unemi]+\.[(a-z)]',correo.lower()):
            return True
            
        else:
            return False

    def Validarclave(clave):
        key2 = clave.isdigit()
        
        if key2 == True:
            return True
        else:
            return False