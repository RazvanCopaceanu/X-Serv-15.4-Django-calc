from django.shortcuts import render
from django.http import HttpResponse

def barra(request):
    return HttpResponse("Bienvenido a la calculadora" + "<br>" + "Las operaciones disponibles son: suma, resta, multi o div")

#localhost:8000/op1/operacion/op2
def calcular(request, op1, operacion, op2):
    if operacion == "suma":
        return HttpResponse("Se suman los numeros: " + op1 + ' y ' + op2 + " .Con resultado = " + str(int(op1) + int(op2)))
    elif operacion == "resta":
        return HttpResponse("Se restan los numeros: " + op1 + ' y ' + op2 + " .Con resultado = " + str(int(op1) - int(op2)))
    elif operacion == "multi":
        return HttpResponse("Se multiplican los numeros: " + op1 + ' y ' + op2 + " .Con resultado = " + str(int(op1) * int(op2)))
    elif operacion == "div" and op2 == "0":
        return HttpResponse("La calculadora no divide entre 0. Prueba con otro numero")
    elif operacion == "div":
        return HttpResponse("Se dividen los numeros: " + op1 + ' y ' + op2 + " .Con resultado = " + str(int(op1) / int(op2)))
    else:
        return HttpResponse("Error. Introduce suma, resta, multi o div")

