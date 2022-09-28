Total = 0
contador = 0
while True:
    input_str = input("ingresar un numero: ")
    try:
        if (input_str == "done"):
            break
        else:
            Total = Total + int(input_str)
            contador = contador + 1
            avarege = Total / contador
    except:
            print("valor no es valido")
            continue
print("Total: ", Total)
print("contador: ", contador)
print("promedio: ", avarege)