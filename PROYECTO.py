import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "No es posible dividir entre cero."

def raiz_cuadrada(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "No es posible sacar la raíz cuadrada de un número negativo."

def potencia(a, b):
    return a ** b

def tangente(angulo_grados):
    return math.tan(math.radians(angulo_grados))

def coseno(angulo_grados):
    return math.cos(math.radians(angulo_grados))

def seno(angulo_grados):
    return math.sin(math.radians(angulo_grados))

def logaritmo(base, x):
    if base > 0 and base != 1 and x > 0:
        return math.log(x, base)
    else:
        return "Base no válida para el logaritmo."

def formula_general(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante >= 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return x1, x2
    else:
        return "Hay Discriminante negativo, no hay soluciones reales."

resultado_anterior = None

while True:
    print("\nSeleccione una operacion:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Raíz Cuadrada")
    print("6. Potencia")
    print("7. Tangente")
    print("8. Coseno")
    print("9. Seno")
    print("10. Logaritmo")
    print("11. Formula General (Ecuación Cuadrática)")
    print("12. Salir")

    opcion = input("Ingrese el numero de la operacion que desea realizar:")

    if opcion == '12':
        print("APAGADO")
        break

    if opcion in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'):
            
            if opcion <= '9' and opcion !='11':
                if resultado_anterior is None:
                    num1 = float(input("Ingrese el primer digito: "))
                else:
                    num1 = resultado_anterior


            if opcion == '11':
                a = float(input("Ingrese el valor para a: "))
                b = float(input("Ingrese el valor para b: "))
                c = float(input("Ingrese el valor para c: "))
                resultado = formula_general(a, b, c)
                print("Las soluciones de X, Y son:", resultado)
            else:
                if opcion <= '4'  and opcion != '10':
                    num2 = float(input("Ingrese el segundo digito: "))

                if opcion == '1':
                    resultado = suma(num1, num2)
                elif opcion == '2':
                    resultado = resta(num1, num2)
                elif opcion == '3':
                    resultado = multiplicacion(num1, num2)
                elif opcion == '4':
                    resultado = division(num1, num2)
                elif opcion == '5':
                    resultado = raiz_cuadrada(num1)
                elif opcion == '6':
                    exponente = float(input("Ingrese el exponente: "))
                    resultado = potencia(num1, exponente)
                elif opcion == '7':
                    resultado = tangente(num1)
                elif opcion == '8':
                    resultado = coseno(num1)
                elif opcion == '9':
                    resultado = seno(num1)
                elif opcion == '10':
                    base = float(input("Ingrese la base: "))
                    resultado = logaritmo(base, num1)


                print("El resultado es:", resultado)
                resultado_anterior = resultado
                continuar = input("¿Desea realizar otra operación con este resultado? (Sí/No): ")
                if continuar.lower() != 'si':
                    print("HEMOS ACABADO, HORA DE APAGARSE")
                    break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida (1-12).")
