# Interes Simple V1.2

import time

colors = {"r": "\033[31m", "n": "\033[0m"}


def cnv_str_float_try(string):
    try:
        float(string)
        return True
    except ValueError:
        print(f"{colors['r']}Computo no valido. Solo valores numericos.{colors['n']}")


def cnv_str_int_try(string):
    try:
        int(string)
        return True
    except ValueError:
        print(f"{colors['r']}Computo no valido. Solo numeros enteros.{colors['n']}")


def num_myr_cero(num, indicacion):
    if num <= 0:
        print(
            f"{colors['r']}El valor `{indicacion}` no puede ser cero o negativo.{colors['n']}"
        )
        return False
    return True


def cnv_str_int_cero(string, indicacion):
    if cnv_str_int_try(string):
        num = int(string)
        if num_myr_cero(num, indicacion):
            return True
    return False


def cnv_str_float_cero(string, indicacion):
    if cnv_str_float_try(string):
        num = float(string)
        if num_myr_cero(num, indicacion):
            return True
    return False


def mostrar_resultados(
    acreedor,
    deudor,
    principal,
    porcentaje_interes,
    periodo,
    cantidad_periodo,
    cantidad_caracteres,
):
    tasa_interes = float(porcentaje_interes) / 100
    print("-" * cantidad_caracteres)
    print("\tExtension de Credito - Interes Simple")
    print("-" * cantidad_caracteres)
    print(f"Acreedor: {acreedor}")
    print("-" * cantidad_caracteres)
    print(f"Deudor: {deudor}")
    print("-" * cantidad_caracteres)
    print(f"Fecha: {time.asctime(time.localtime(time.time()))}")
    print("-" * cantidad_caracteres)
    print(f"Tasa de Interes: {porcentaje_interes}%")
    print("-" * cantidad_caracteres)
    print(f"Monto Inicial: ${round(principal, 2):.2f}")
    print("-" * cantidad_caracteres)
    print(f"Periodo: {periodo}")
    print("-" * cantidad_caracteres)
    print(f"Cantidad de Periodos: {cantidad_periodo}")
    print("-" * cantidad_caracteres)
    # print("Interes Simple")
    # print("I = P x r x n")
    # print("P = [P]rincipal - Monto inicial")
    # print("r = Interest [r]ate - Tasa de interes")
    # print("n = [n]umbers of periods - Cantidad de periodos")
    interes_simple = principal * tasa_interes * cantidad_periodo
    print(f"Interes Simple: ${round(interes_simple, 2):.2f}")
    print("-" * cantidad_caracteres)
    monto_total = principal + interes_simple
    print(f"Total: ${round(monto_total, 2):.2f}")
    print("-" * cantidad_caracteres)


def main():
    cantidad_caracteres = 50
    periodos = {
        "1": ("Diario"),
        "2": ("Semanal"),
        "3": ("Mensual"),
        "4": ("Trimestral"),
        "5": ("Cuatrimestral"),
        "6": ("Semestral"),
        "7": ("Anual"),
    }
    periodo = ""
    print("-" * cantidad_caracteres)
    print("\tCALCULADORA INTERES SIMPLE V1.2")
    print("-" * cantidad_caracteres)
    acreedor = input("Acreedor: ")
    print("*" * cantidad_caracteres)
    deudor = input("Deudor: ")
    print("*" * cantidad_caracteres)
    principal = input("Monto Incial: ")
    while not cnv_str_float_cero(principal, "monto incial"):
        principal = input("Monto Incial: ")
    principal = float(principal)
    print("*" * cantidad_caracteres)
    porcentaje_interes = input("Tasa de Interes (%): ")
    while not cnv_str_float_cero(porcentaje_interes, "tasa de interes"):
        porcentaje_interes = input("Tasa de Interes (%): ")
    print("*" * cantidad_caracteres)
    while not periodo:
        print("Periodo")
        for indice, frecuencia in periodos.items():
            print(f"{indice} -> {frecuencia}")
        opcion = input("Numero de opcion -> ")
        if opcion not in periodos:
            print(
                f"{colors['r']}Computo no valido. Solo opciones disponibles.{colors['n']}"
            )
        else:
            periodo = periodos[opcion]
    print("*" * cantidad_caracteres)
    cantidad_periodo = input("Cantidad de Periodos: ")
    while not cnv_str_int_cero(cantidad_periodo, "catidad de periodos"):
        cantidad_periodo = input("Cantidad de Periodos: ")
    cantidad_periodo = int(cantidad_periodo)
    print("\n")
    mostrar_resultados(
        acreedor,
        deudor,
        principal,
        porcentaje_interes,
        periodo,
        cantidad_periodo,
        cantidad_caracteres,
    )


if __name__ == "__main__":
    main()
