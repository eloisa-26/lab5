def consultar_saldo(saldo):
    return saldo


def depositar(saldo, monto):
    if monto <= 0:
        return saldo, False, "Monto inválido."

    nuevo_saldo = saldo + monto
    return nuevo_saldo, True, f"Depósito exitoso. Nuevo saldo: ${nuevo_saldo}"


def retirar(saldo, monto):
    if monto <= 0:
        return saldo, False, "Monto inválido."

    if monto > saldo:
        return saldo, False, "Fondos insuficientes."

    nuevo_saldo = saldo - monto
    return nuevo_saldo, True, f"Retiro exitoso. Nuevo saldo: ${nuevo_saldo}"
