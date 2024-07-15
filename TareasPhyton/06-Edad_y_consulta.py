print("")

Edad = int(input("Ingrese la edad de la persona: "))
print("")
Art = int(input("Ingrese la cantidad de articulos comprados: "))
print("")

if (Edad > 18):
    if Art > 1:
        print("La persona es mayor a 18 y ha comprado más de un articulo (True)")
        print("")
    else:
        print("La persona es mayor de 18 pero no ha comprado más de un articulo (False)")
        print("")
else:
    print("La persona no es mayor de 18 (False)") 
    print("")