"""
Código a evaluar:
numero = 7/0
"""

from ast import main 

def error_division_0(numerador,denominador): #Creo una función para la resolución del ejercicio
    try: #Pruebo a ver si funciona
        numero = numerador/denominador
        return numero 
    except ZeroDivisionError: #Como divido por zero me da error 
        print("No se puede dividir por 0")
    return 

error_division_0(7,0)

if __name__ == "__main__":
    main()