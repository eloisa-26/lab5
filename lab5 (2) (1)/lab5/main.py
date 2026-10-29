from auth import verificar_pin
from operaciones import consultar_saldo, depositar, retirar


def main():
    saldo = 1000.0
    pin_correcto = "1234"

    print("CAJERO AUTOMÁTICO")

    if verificar_pin(pin_correcto):
        while True:
            print("\n1. Consultar saldo")
            print("\n2. Depositar dinero")
            print("\n3. Retirar dinero")
            print("\n4. Salir")

            opcion = input("Elija una opción: ")

            if opcion == "1":
                print(f"Su saldo actual es: ${consultar_saldo(saldo)}")

            elif opcion == "2":
                monto = float(input("Ingrese monto a depositar: "))
                saldo, ok, mensaje = depositar(saldo, monto)
                print(mensaje)

            elif opcion == "3":
                monto = float(input("Ingrese monto a retirar: "))
                saldo, ok, mensaje = retirar(saldo, monto)
                print(mensaje)

            elif opcion == "4":
                print("Gracias por usar el cajero.")
                break

            else:
                print("Opción inválida.")
    else:
        print("Tarjeta bloqueada por seguridad.")


if __name__ == "__main__":
    main()
