def calculo_salario(horas, tarifas):
    MAXH = 40
    if (horas > MAXH):
        horas_extra = int(horas)- MAXH
    else:
        horas_extra = 0
    calculo = (int(horas)* int(tarifas)) + (horas_extra *(int(tarifas)/2))
    return calculo

horas = float(input("ingrese horas trabajadas: "))
tarifas = float(input("ingrese tarifa "))
Pago = calculo_salario(horas, tarifas)
print(Pago)