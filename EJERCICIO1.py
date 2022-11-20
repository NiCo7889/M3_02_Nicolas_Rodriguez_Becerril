"""
Código a evaluar:
numero = 7/0
"""

def division_por_cero():    
    try:                    
       numero = 7/0
    except ZeroDivisionError:   
        return "No se puede dividir entre 0"    
    return numero
    
def main():
    print(division_por_cero())

if __name__ == "__main__":
    main()