"""
Localiza el error en el siguiente bloque de código. 
Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
resultado = "2" + 10
"""

from ast import main 

def error_suma_string(*args): #Creo una función para la resolución del ejercicio
    suma = 0
    for args in args:
        try: #Pruebo a ver si funciona
            suma += args 
        except TypeError: #Capturo el error
            print ("No se puede sumar un string a un int.")     
    return 

error_suma_string("2", 10) #Ejecuto la función

if __name__ == "__main__":
    main()