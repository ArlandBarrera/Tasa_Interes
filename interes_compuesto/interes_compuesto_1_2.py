# Interes Compuesto V1.2

import time

colors = {"r": "\033[31m", "n": "\033[0m"}


def cnv_str_float_try(string):
    try:
        float(string)
        return True
    except ValueError:
        print(f"{colors['r']}Computo no valido. Solo valores numericos.{colors['n']}")


def num_myr_cero(num, indicacion):
    if num <= 0:
        print(
            f"{colors['r']}El valor `{indicacion}` no puede ser cero o negativo.{colors['n']}"
        )
        return False
    return True


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
    tiempo,
    cantidad_caracteres,
):
    tasa_interes = float(porcentaje_interes) / 100
    print("-" * cantidad_caracteres)
    print("\tExtension de Credito - Interes Compuesto")
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
    print(f"Tiempo de acumulacion: {tiempo}")
    print("-" * cantidad_caracteres)
    # print("Interes Compuesto")
    # print("T = P x [ (1 + (r / n) ) ^ (n x t) ]")
    # print("P = [P]rincipal - Monto inicial")
    # print("r = Interest [r]ate - Tasa de interes")
    # print("n = [n]umbers of periods per year - Cantidad de periodos anuales")
    # print("t = [t]ime in years - tiempo anual")
    monto_total = principal * (
        (1 + (tasa_interes / cantidad_periodo)) ** (cantidad_periodo * tiempo)
    )
    interes_compuesto = monto_total - principal
    print(f"Interes Compuesto: ${round(interes_compuesto, 2):.2f}")
    print("-" * cantidad_caracteres)
    print(f"Total: ${round(monto_total, 2):.2f}")
    print("-" * cantidad_caracteres)


def main():
    cantidad_caracteres = 50
    periodos = {
        "1": ("Diario", 365),
        "2": ("Semanal", 48),
        "3": ("Mensual", 12),
        "4": ("Trimestral", 4),
        "5": ("Cuatrimestral", 3),
        "6": ("Semestral", 2),
        "7": ("Anual", 1),
    }
    periodo = ""
    cantidad_periodo = 0
    print("-" * cantidad_caracteres)
    print("\tCALCULADORA INTERES COMPUESTO V1.2")
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
    while not cantidad_periodo:
        print("Periodo")
        for indice, valor in periodos.items():
            print(f"{indice} -> {valor[0]}")
        opcion = input("Indice de opcion -> ")
        if opcion not in periodos:
            print(
                f"{colors['r']}Computo no valido. Solo opciones disponibles.{colors['n']}"
            )
        else:
            periodo, cantidad_periodo = periodos[opcion]
    print("*" * cantidad_caracteres)
    tiempo_years = input("Tiempo de acumulacion (years): ")
    while not cnv_str_float_cero(tiempo_years, "tiempo de acumulacion"):
        tiempo_years = input("Tiempo de acumulacion (years): ")
    tiempo_years = float(tiempo_years)
    print("\n")
    mostrar_resultados(
        acreedor,
        deudor,
        principal,
        porcentaje_interes,
        periodo,
        cantidad_periodo,
        tiempo_years,
        cantidad_caracteres,
    )


if __name__ == "__main__":
    main()