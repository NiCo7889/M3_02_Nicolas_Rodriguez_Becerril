"""
Código a evaluar:
lista = [4, 7, 30, 23, 5]
lista[10]
"""

from ast import main

def error_elemento_fuera_lista(lista, elemento_lista):
    try:
        elemento = lista[elemento_lista]
        return elemento
    except IndexError:
        print("El elemento {} no pertenece a la lista. ".format(elemento_lista, len(lista)))

error_elemento_fuera_lista([4, 7, 30, 23, 5], 10)

print("\n")

if __name__ == "__main__":
    main()