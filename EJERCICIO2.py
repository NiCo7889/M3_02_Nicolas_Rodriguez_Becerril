"""
Código a evaluar:
lista = [4, 7, 30, 23, 5]
lista[10]
"""

from ast import main

def error_elemento_fuera_lista(lista, elemento_lista): #Creo una función para la resolución del ejercicio
    try: #Pruebo a ver si funciona
        elemento = lista[elemento_lista]#Busco un elemento no pertenece a la lista
        return elemento
    except IndexError:#Capturo el error
        print("El elemento {} no pertenece a la lista. ".format(elemento_lista, len(lista)))

error_elemento_fuera_lista([4, 7, 30, 23, 5], 10)#Ejecuto la función

if __name__ == "__main__":
    main()