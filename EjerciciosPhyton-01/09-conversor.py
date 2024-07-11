temperatura = float(input("Ingrese la temperatura:"))
escala = input("Su escala ¿es Fahrenheit(F) o Celsius?(C):").lower()

if escala == "f":
    Celsius = (temperatura - 32) * 5/9
    print(Celsius)
elif escala == "c":
    Fahrenheit = temperatura * 1.8 + 32
    print(Fahrenheit) 
else:
    print("Coloco una escala no validad")
    print("Por favor ingrese la letra F si su escala es Fahrenheit")
    print("o la letra C si es Celsius")