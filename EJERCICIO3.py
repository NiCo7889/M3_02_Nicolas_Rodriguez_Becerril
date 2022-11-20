"""
Código a evaluar:
paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 
paises["alemania"]
"""

from ast import main 

def error_clave_fuera_diccionario(diccionario, clave):#Creo una función para la resolución del ejercicio
    try:#Pruebo a ver si funciona
        clave = diccionario[clave]
        return clave 
    except KeyError:
        print ("La clave {} no se encuentra en la lista y por tanto no se puede devolver su valor correspondiente".format(clave))     
    return 

error_clave_fuera_diccionario({ "españa":"español", "eeuu":"inglés", "italia":"italiano" } , "alemania")#Ejecuto la función


if __name__ == "__main__":
    main()