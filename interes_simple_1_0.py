# Interes Simple V 1.0

import time


def main():
    cantidad_caracteres = 50
    principal = 0
    tasa_interes = 0
    periodo = ""
    cantidad_periodo = 0
    print("\tCALCULADORA INTERES SIMPLE V 1.0")
    print("-" * cantidad_caracteres)
    principal = input("Monto Incial: ")
    principal = float(principal)
    print("*" * cantidad_caracteres)
    porcentaje_interes = input("Tasa de Interes (%): ")
    tasa_interes = float(porcentaje_interes) / 100
    print("*" * cantidad_caracteres)
    while not periodo:
        print("Periodo")
        print("1 -> Semanal")
        print("2 -> Mensual")
        print("3 -> 3 Meses")
        print("4 -> 4 Meses")
        print("5 -> 6 Meses")
        print("6 -> Anual")
        periodo = input("Numero de opcion -> ")
        if periodo not in ["1", "2", "3", "4", "5", "6"]:
            print("\nComputo no valido.")
        else:
            if periodo == "1":
                periodo = "Semanal"
            elif periodo == "2":
                periodo = "Mensual"
            elif periodo == "3":
                periodo = "3 Meses"
            elif periodo == "4":
                periodo = "4 Meses"
            elif periodo == "5":
                periodo = "6 Meses"
            elif periodo == "6":
                periodo = "Anual"
    print("*" * cantidad_caracteres)
    cantidad_periodo = input("Cantidad de Periodos: ")
    cantidad_periodo = int(cantidad_periodo)
    print("\n")
    print("-" * cantidad_caracteres)
    print("\tExtension de Credito - Interes Simple")
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


if __name__ == "__main__":
    main()
