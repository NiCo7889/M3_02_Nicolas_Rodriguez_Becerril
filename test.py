from ast import main

print("Ejercicio 3:\n")

def error_clave_0(diccionario, clave):
    try:
        clave = diccionario[clave]
        return clave
    except KeyError:
        print("La clave {} no está presente en este diccionario".format(clave)) 

error_clave_0({ "españa":"español", "eeuu":"inglés", "italia":"italiano" }, "alemania")

print("\n")

if __name__ == "__main__":
    main()