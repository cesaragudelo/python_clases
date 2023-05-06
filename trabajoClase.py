class CuentaAhorro:
    def __init__(self, NroCuenta, Nombres, Sucursal, Saldo ):
        self.NroCuenta= NroCuenta
        self.Nombres = Nombres
        self.Sucursal = Sucursal
        self.Saldo = Saldo
        
    def imprimirDatos(self):
        print("----------------------------------------------------")
        print("            DATOS DE CUENTA                      ")
        print("----------------------------------------------------")
        print(f"Ncuenta---> {self.NroCuenta}")
        print(f"nombre---> {self.Nombres}")
        print(f"sucursal---> {self.Sucursal}")
        print(f"saldo---> {self.Saldo}")
        
    def ConsignarMonto(self,monto):
        cantSaldo= self.Saldo
        sumSaldo=cantSaldo+monto
        cuentaHorros=[sumSaldo]
        return cuentaHorros
    
    def RetirarMonto(self,monto,saldo):
        sumSaldo=saldo[0]-monto
        cuentaHorros=[sumSaldo]
        return cuentaHorros
    
    def Consultar(self, saldoActual):
        print("----------------------------------------------------")
        print("            DATOS DE CUENTA                      ")
        print("----------------------------------------------------")
        print(f"Ncuenta---> {self.NroCuenta}")
        print(f"nombre---> {self.Nombres}")
        print(f"sucursal---> {self.Sucursal}")
        print(f"saldo comienzo---> {self.Saldo}")
        print(f"saldo actual--->{saldoActual[0]}")
        
        
if __name__ == "__main__":
    persona1= CuentaAhorro(123,"cesar","itagui",50000)
    persona1.imprimirDatos()
    saldoArray= persona1.ConsignarMonto(500000)
    saldoArray=persona1.RetirarMonto(10000,saldoArray)
    persona1.Consultar(saldoArray)