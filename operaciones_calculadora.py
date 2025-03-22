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
    dividendo = dividendo.copy()
    divisor = divisor.copy()
    cociente = {}

    if not divisor:
        return {}, dividendo  # No se puede dividir entre 0

    while dividendo and max(dividendo) >= max(divisor):
        exp_dividendo = max(dividendo)
        exp_divisor = max(divisor)
        coef_dividendo = dividendo[exp_dividendo]
        coef_divisor = divisor[exp_divisor]

        nuevo_exp = exp_dividendo - exp_divisor
        nuevo_coef = coef_dividendo / coef_divisor
        cociente[nuevo_exp] = nuevo_coef

        # Generar el polinomio a restar
        a_restar = {}
        for exp, coef in divisor.items():
            a_restar[exp + nuevo_exp] = coef * nuevo_coef

        # Restar el término del dividendo
        for exp, coef in a_restar.items():
            dividendo[exp] = dividendo.get(exp, 0) - coef
            if abs(dividendo[exp]) < 1e-10:
                del dividendo[exp]

    return cociente, dividendo


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
