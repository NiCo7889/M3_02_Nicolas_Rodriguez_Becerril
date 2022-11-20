"""
Código a evaluar:
numero = 7/0
"""

from ast import main 

def error_division_0(numerador,denominador):
    try: 
        numero = numerador/denominador
        return numero 
    except ZeroDivisionError:
        print("No se puede dividir por 0")
    return

error_division_0(7,0)

if __name__ == "__main__":
    main()