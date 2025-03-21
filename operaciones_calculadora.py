def sumar(p1, p2):
    resultado = p1.copy()
    for exp, coef in p2.items():
        resultado[exp] = resultado.get(exp, 0) + coef
    return resultado

def restar(p1, p2):
    resultado = p1.copy()
    for exp, coef in p2.items():
        resultado[exp] = resultado.get(exp, 0) - coef
    return resultado

def multiplicar(p1, p2):
    resultado = {}
    for exp1, coef1 in p1.items():
        for exp2, coef2 in p2.items():
            exp = exp1 + exp2
            coef = coef1 * coef2
            resultado[exp] = resultado.get(exp, 0) + coef
    return resultado

def dividir(dividendo, divisor):
    cociente = {}
    resto = dividendo.copy()
    # Si el grado del divisor es mayor, se devuelve cociente vacío y resto igual al dividendo
    while resto and max(resto) >= max(divisor):
        exp_diff = max(resto) - max(divisor)
        coef_div = resto[max(resto)] / divisor[max(divisor)]
        cociente[exp_diff] = coef_div

        subtrahend = {}
        for exp, coef in divisor.items():
            nuevo_exp = exp + exp_diff
            nuevo_coef = coef * coef_div
            subtrahend[nuevo_exp] = nuevo_coef

        resto = restar(resto, subtrahend)

    return cociente, resto

def evaluar(pol, valor):
    resultado = 0
    for exp, coef in pol.items():
        resultado += coef * (valor ** exp)
    return resultado

def leer_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as f:
        lineas = f.readlines()

    p1_texto = ""
    p2_texto = ""
    operacion = ""

    for linea in lineas:
        if linea.startswith("POLINOMIO 1:"):
            p1_texto = linea.replace("POLINOMIO 1:", "").strip()
        elif linea.startswith("POLINOMIO 2:"):
            p2_texto = linea.replace("POLINOMIO 2:", "").strip()
        elif linea.startswith("OPERACIÓN:"):
            operacion = linea.replace("OPERACIÓN:", "").strip().upper()

    return p1_texto, p2_texto, operacion

def guardar_en_archivo(nombre_archivo, resultado, operacion="OPERACIÓN"):
    with open(nombre_archivo, 'w') as f:
        f.write(f"RESULTADO DE LA {operacion.upper()} DE POLINOMIOS:\n")
        f.write(resultado + '\n')
