import re
from operaciones_calculadora import (
    sumar, restar, multiplicar, dividir, evaluar, guardar_en_archivo
)

# Convierte "2x4 + 3x2 - 5" a {4: 2, 2: 3, 0: -5}
def parsear_polinomio(texto):
    texto = texto.replace(" -", "+-").replace("-", "+-")
    terminos = texto.split("+")
    pol = {}

    for termino in terminos:
        termino = termino.strip()
        if not termino:
            continue
        if "x" in termino:
            if "x^" in termino:
                coef, exp = termino.split("x^")
            elif "x" in termino:
                coef, exp = termino.split("x")
                exp = "1"
            coef = coef.strip().replace(" ", "")
            exp = int(exp.strip())
            coef = float(coef) if coef not in ["", "+", "-"] else float(coef + "1")
        else:
            coef = float(termino.strip().replace(" ", ""))
            exp = 0
        pol[exp] = pol.get(exp, 0) + coef

    return pol


# Convierte {2: 3, 0: 5} a "3x² + 5"
def polinomio_a_texto(polinomio):
    if not polinomio:
        return "0"

    terminos = []
    for exp in sorted(polinomio.keys(), reverse=True):
        coef = polinomio[exp]
        if coef == 0:
            continue

        # Coeficiente
        if coef == 1 and exp != 0:
            coef_str = ""
        elif coef == -1 and exp != 0:
            coef_str = "-"
        else:
            coef_str = f"{coef:.0f}" if coef == int(coef) else f"{coef}"

        # Término según exponente
        if exp == 0:
            terminos.append(f"{coef_str}")
        elif exp == 1:
            terminos.append(f"{coef_str}x")
        else:
            terminos.append(f"{coef_str}x^{exp}")

    resultado = terminos[0]
    for termino in terminos[1:]:
        if termino.startswith("-"):
            resultado += " - " + termino[1:]
        else:
            resultado += " + " + termino

    return resultado

def mostrar_menu():
    print("\n--- Calculadora Científica de Polinomios ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Evaluar en un número")
    print("6. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-6): ")

        if opcion == "6":
            print("¡Adiós!")
            break

        p1_texto = input("Introduce el primer polinomio (ej: 2x^2 + 1): ")
        p1 = parsear_polinomio(p1_texto)

        if opcion in ["1", "2", "3", "4"]:
            p2_texto = input("Introduce el segundo polinomio: ")
            p2 = parsear_polinomio(p2_texto)

        if opcion == "1":
            resultado = sumar(p1, p2)
            resultado_texto = polinomio_a_texto(resultado)
            print("Resultado:", resultado_texto)
            operacion = "suma"

        elif opcion == "2":
            resultado = restar(p1, p2)
            resultado_texto = polinomio_a_texto(resultado)
            print("Resultado:", resultado_texto)
            operacion = "resta"

        elif opcion == "3":
            resultado = multiplicar(p1, p2)
            resultado_texto = polinomio_a_texto(resultado)
            print("Resultado:", resultado_texto)
            operacion = "multiplicación"


        elif opcion == "4":

            cociente, resto = dividir(p1, p2)

            cociente_texto = polinomio_a_texto(cociente)

            resto_texto = polinomio_a_texto(resto)

            if not cociente and not resto:

                print("No se puede dividir (división entre 0 o polinomio vacío)")

            else:

                print("Cociente:", cociente_texto)

                print("Resto:", resto_texto)

            resultado_texto = f"Cociente: {cociente_texto}, Resto: {resto_texto}"

            operacion = "división"

        elif opcion == "5":
            valor = float(input("Introduce el valor de x: "))
            resultado = evaluar(p1, valor)
            print("Resultado:", resultado)
            resultado_texto = str(resultado)
            operacion = "evaluación"

        else:
            print("Opción no válida.")
            continue

        guardar = input("¿Quieres guardar el resultado en un archivo? (s/n): ").lower()
        if guardar == "s":
            nombre_archivo = input("Nombre del archivo (ej: resultado.txt): ")
            guardar_en_archivo(nombre_archivo, resultado_texto, operacion)

if __name__ == "__main__":
    main()
