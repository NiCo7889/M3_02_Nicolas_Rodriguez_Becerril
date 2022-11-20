"""
Código a evaluar:
paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 
paises["alemania"]
"""

from ast import main 

def error_elemento_fuera_lista(lista, elemento_lista):
    try:
        elemento = lista[elemento_lista]
        return elemento 
    except IndexError:
        print ("El elemento {} no se encuentra en la lista, ya que la lista solo contiene {} elementos".format(elemento_lista, len(lista)))     
    return 

error_elemento_fuera_lista([4, 7, 30, 23, 5], 10)

if __name__ == "__main__":
    main()