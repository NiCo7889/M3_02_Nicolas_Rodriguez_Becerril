"""
Código a evaluar:
paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 
paises["alemania"]
"""

from ast import main 
paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } #Creamos un diccionario

def non_dict_key():     #Creamos una función para coger el error
    try:
        paises["alemania"]  #Buscamos la clave alemania en el diccionario
    except KeyError:    #Si la excepción es del tipo KeyError
        return "La clave buscada no existe"     #Decimos que la clave no existe en caso de que salte el error

def main():     #Creamos la función main
    print(non_dict_key())

if __name__ == "__main__":  #Ejecutamos el código
    main()