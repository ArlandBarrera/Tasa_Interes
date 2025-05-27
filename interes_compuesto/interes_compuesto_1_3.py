# Interes Compuesto V 1.3

# Interes Compuesto
# T = P x [ (1 + (r / n) ) ^ (n x t) ]
# P = [P]rincipal - Monto inicial
# r = Interest [r]ate - Tasa de interes
# n = [n]umbers of periods per year - Cantidad de periodos anuales
# t = [t]ime in years - tiempo anual

import time

# rojo, nulo
colors: dict[str, str] = {"r": "\033[31m", "n": "\033[0m"}


def parseStringToFloat(string: str):
    try:
        float(string)
        return True
    except ValueError:
        print(f"{colors['r']}Computo no valido. Solo valores numericos.{colors['n']}")


def numEquGtrThanCero(num: float, indicacion: str) -> bool:
    if num < 0:
        print(
            f"{colors['r']}El valor `{indicacion}` no puede ser negativo.{colors['n']}"
        )
        return False
    return True


def parseStrToFloatLessCero(string: str, indicacion: str) -> bool:
    if parseStringToFloat(string):
        num = float(string)
        if numEquGtrThanCero(num, indicacion):
            return True
    return False


def mostrarResultados(
    acreedor: str,
    deudor: str,
    principal: float,
    porcentaje_interes: str,
    periodo: str,
    cantidad_periodo: int,
    tiempo: float,
    cantidad_caracteres: int,
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
    periodos: dict[str, tuple[str, int]] = {
        "1": ("Diario", 365),
        "2": ("Semanal", 48),
        "3": ("Mensual", 12),
        "4": ("Bimestral", 6),
        "5": ("Trimestral", 4),
        "6": ("Cuatrimestral", 3),
        "7": ("Semestral", 2),
        "8": ("Anual", 1),
    }
    periodo = ""
    cantidad_periodo = 0
    print("-" * cantidad_caracteres)
    print("\tCALCULADORA INTERES COMPUESTO V 1.3")
    print("-" * cantidad_caracteres)
    acreedor = input("Acreedor: ")
    print("*" * cantidad_caracteres)
    deudor = input("Deudor: ")
    print("*" * cantidad_caracteres)
    principal = input("Monto Incial: ")
    while not parseStrToFloatLessCero(principal, "monto incial"):
        principal = input("Monto Incial: ")
    principal = float(principal)
    print("*" * cantidad_caracteres)
    porcentaje_interes = input("Tasa de Interes (%): ")
    while not parseStrToFloatLessCero(porcentaje_interes, "tasa de interes"):
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
    while not parseStrToFloatLessCero(tiempo_years, "tiempo de acumulacion"):
        tiempo_years = input("Tiempo de acumulacion (years): ")
    tiempo_years = float(tiempo_years)
    print("\n")
    mostrarResultados(
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
