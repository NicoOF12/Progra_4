from inspect import _void


class CuentaJoven:

    def __init__(self, nombre, cuenta):
        self._nombre = nombre
        self._cuenta = cuenta

    def ingresarCantidad(self, valor):
        if(valor):
            return

    def retirarCantidad(self, valor):
        if(valor):
            return

class CuentaBancaria:

    def __init__(self, numeroCuenta, nombreTitular, saldo, numeroOperaciones, MAXIMOREINTEGRO, cuentasCreadas):
        self._numeroCuenta = numeroCuenta
        self._nombreTitular = nombreTitular
        self._saldo = saldo
        self._numeroOperaciones = numeroOperaciones
        self._MAXIMOREINTEGRO = MAXIMOREINTEGRO
        self._cuentasCreadas = cuentasCreadas

    def getNumeroCuenta(self):
        return self._numeroCuenta

    def getNombreTitular(self):
        return self._nombreTitular

    def getSaldo(self):
        return self._saldo

    def getNumeroOperaciones(self):
        return self._numeroOperaciones

    def setSaldo(self, saldo):
        self._saldo = saldo

    def ingresarCantidad(self, cantidad):
        if(cantidad):
            return True
        else:
            return False

    def retirarCantidad(self, cantidad):
        if(cantidad):
            return True
        else:
            return False

    def getCuentasCreadas(self):
        return self._cuentasCreadas

    def setCuentasCreadasNull(self):
        return _void