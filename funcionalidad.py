

class CifradoCesar(object):
    
    alfabeto_minuscula = list("abcdefghijklmnopqrstuvwxyz")
    alfabeto_mayuscula = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    digitos = list("0123456789")
    texto_original = ""
    mensaje_encriptado = ""
    mensaje_desencriptado = ""
    mensaje_estado_archivo = ""
    desplazamiento = 0
    
    def __init__(self, nombre_archivo, desplazamiento):
        
        self.nombre_archivo = nombre_archivo
        CifradoCesar.desplazamiento = desplazamiento
        
        try:
            CifradoCesar.mensaje_estado_archivo = ""
            with open(self.nombre_archivo, 'r') as archivo:
                CifradoCesar.texto_original = archivo.read()
        
        except FileNotFoundError:
            CifradoCesar.mensaje_estado_archivo = "No se ha encontrado el archivo..."

    @classmethod
    def proceso_encriptado_minusculas(cls, caracter):
        if CifradoCesar.desplazamiento == 0:
            CifradoCesar.mensaje_encriptado = CifradoCesar.texto_original
        else:
            indice = CifradoCesar.alfabeto_minuscula.index(caracter)
            modulo = CifradoCesar.desplazamiento % 26
            nuevo_indice = indice + modulo
        
            if nuevo_indice >= 26:
                rango_de_indice_alcanzado = len(list(range(indice, len(CifradoCesar.alfabeto_minuscula))))
                modulo -= rango_de_indice_alcanzado
            
                for numero in range(modulo + 1):
                    if numero + 1 == modulo + 1:
                        CifradoCesar.mensaje_encriptado += CifradoCesar.alfabeto_minuscula[numero]
            else:
                CifradoCesar.mensaje_encriptado += CifradoCesar.alfabeto_minuscula[nuevo_indice]
            
    @classmethod
    def proceso_encriptado_mayuscula(cls, caracter):
        if CifradoCesar.desplazamiento == 0:
            CifradoCesar.mensaje_encriptado = CifradoCesar.texto_original
        
        else:
            indice = CifradoCesar.alfabeto_mayuscula.index(caracter)
            modulo = CifradoCesar.desplazamiento % 26
            nuevo_indice = indice + modulo

            if nuevo_indice >= 26:
                rango_de_indice_alcanzado = len(list(range(indice, len(CifradoCesar.alfabeto_mayuscula))))
                modulo -= rango_de_indice_alcanzado
            
                for numero in range(modulo + 1):
                    if numero + 1 == modulo + 1:
                        CifradoCesar.mensaje_encriptado += CifradoCesar.alfabeto_mayuscula[numero]
            else:
                CifradoCesar.mensaje_encriptado += CifradoCesar.alfabeto_mayuscula[nuevo_indice]
    
    @classmethod
    def proceso_encriptado_digitos(cls, caracter):
        if CifradoCesar.desplazamiento == 0:
            CifradoCesar.mensaje_encriptado = CifradoCesar.texto_original
        else:    
            indice = CifradoCesar.digitos.index(caracter)
            modulo = CifradoCesar.desplazamiento % 10
            nuevo_indice = indice + modulo
        
            if nuevo_indice >= 9:
                rango_de_indice_alcanzado = len(list(range(indice, len(CifradoCesar.digitos))))
                modulo -= rango_de_indice_alcanzado
            
                for numero in range(modulo + 1):
                    if numero + 1 == modulo + 1:
                        CifradoCesar.mensaje_encriptado += CifradoCesar.digitos[numero]
            else:
                CifradoCesar.mensaje_encriptado += CifradoCesar.digitos[nuevo_indice]
    
    @classmethod
    def proceso_desencriptado_minusculas(cls, caracter):
        indice = CifradoCesar.alfabeto_minuscula.index(caracter)
        modulo = CifradoCesar.desplazamiento % 26
        nuevo_indice = indice - modulo
        CifradoCesar.mensaje_desencriptado += CifradoCesar.alfabeto_minuscula[nuevo_indice]
    
    @classmethod
    def proceso_desencriptado_mayuscula(cls, caracter):
        indice = CifradoCesar.alfabeto_mayuscula.index(caracter)
        modulo = CifradoCesar.desplazamiento % 26
        nuevo_indice = indice - modulo
        CifradoCesar.mensaje_desencriptado += CifradoCesar.alfabeto_mayuscula[nuevo_indice]        
    
    @classmethod
    def proceso_desencriptado_digitos(cls, caracter):
        indice = CifradoCesar.digitos.index(caracter)
        modulo = CifradoCesar.desplazamiento % 10
        nuevo_indice = indice - modulo
        CifradoCesar.mensaje_desencriptado += CifradoCesar.digitos[nuevo_indice]        
    
     #metodo para encriptar mensaje no encriptado
    def encriptado(self):
        
        mensaje_letras = list(CifradoCesar.texto_original)
        CifradoCesar.mensaje_encriptado = ""
        
        for letra in mensaje_letras:
            
            if letra in CifradoCesar.alfabeto_minuscula:
                CifradoCesar.proceso_encriptado_minusculas(letra)
            
            elif letra in CifradoCesar.digitos:
                CifradoCesar.proceso_encriptado_digitos(letra)
            
            elif letra in CifradoCesar.alfabeto_mayuscula:
                CifradoCesar.proceso_encriptado_mayuscula(letra)                
            
            else:
                if CifradoCesar.desplazamiento != 0:
                    CifradoCesar.mensaje_encriptado += letra
                
        return CifradoCesar.mensaje_encriptado
        
    #metodo para desencriptar el mensaje encriptado
    def desencriptado(self): 
        
        if CifradoCesar.mensaje_encriptado:
            
            CifradoCesar.mensaje_desencriptado = ""
            
            for letra in list(CifradoCesar.mensaje_encriptado):
            
                if letra in CifradoCesar.alfabeto_minuscula:
                    CifradoCesar.proceso_desencriptado_minusculas(letra)
                
                elif letra in CifradoCesar.digitos:
                    CifradoCesar.proceso_desencriptado_digitos(letra)
                
                elif letra in CifradoCesar.alfabeto_mayuscula:
                    CifradoCesar.proceso_desencriptado_mayuscula(letra)
                
                else:

                    CifradoCesar.mensaje_desencriptado += letra
       
        return CifradoCesar.mensaje_desencriptado

        