# Interes Simple V 1.3

# Interes Simple
# I = P x r x n
# P = [P]rincipal - Monto inicial
# r = Interest [r]ate - Tasa de interes
# n = [n]umbers of periods - Cantidad de periodos

import time

# rojo, nulo
colors: dict[str, str] = {"r": "\033[31m", "n": "\033[0m"}


def parseStringToFloat(string: str):
    try:
        float(string)
        return True
    except ValueError:
        print(f"{colors['r']}Computo no valido. Solo valores numericos.{colors['n']}")


def parseStringToInt(string: str):
    try:
        int(string)
        return True
    except ValueError:
        print(f"{colors['r']}Computo no valido. Solo numeros enteros.{colors['n']}")


def numEquGtrThanCero(num: float, indicacion: str) -> bool:
    if num < 0:
        print(
            f"{colors['r']}El valor `{indicacion}` no puede negativo.{colors['n']}"
        )
        return False
    return True


def parseStrToIntLessCero(string: str, indicacion: str) -> bool:
    if parseStringToInt(string):
        num = int(string)
        if numEquGtrThanCero(num, indicacion):
            return True
    return False


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
    cantidad_caracteres: int,
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
    interes_simple = principal * tasa_interes * cantidad_periodo
    print(f"Interes Simple: ${round(interes_simple, 2):.2f}")
    print("-" * cantidad_caracteres)
    monto_total = principal + interes_simple
    print(f"Total: ${round(monto_total, 2):.2f}")
    print("-" * cantidad_caracteres)


def main():
    cantidad_caracteres = 50
    periodos: dict[str, str] = {
        "1": ("Diario"),
        "2": ("Semanal"),
        "3": ("Mensual"),
        "4": ("Bimestral"),
        "5": ("Trimestral"),
        "6": ("Cuatrimestral"),
        "7": ("Semestral"),
        "8": ("Anual"),
    }
    periodo = ""
    print("-" * cantidad_caracteres)
    print("\tCALCULADORA INTERES SIMPLE V 1.3")
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
    while not parseStrToIntLessCero(cantidad_periodo, "catidad de periodos"):
        cantidad_periodo = input("Cantidad de Periodos: ")
    cantidad_periodo = int(cantidad_periodo)
    print("\n")
    mostrarResultados(
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
