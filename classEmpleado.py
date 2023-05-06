class Empleado:
    def __init__(self, IdEmpleado, apellidos, nombres, area, salario ):
        self.IdEmpleado= IdEmpleado
        self.apellidos = apellidos
        self.nombres = nombres
        self.area = area
        self.salario = salario
        
    def imprimirDatos(self):
        print("----------------------------------------------------")
        print("            DATOS DEL EMPLEADO                      ")
        print("----------------------------------------------------")
        print(f"cedula---> {self.IdEmpleado}")
        print(f"apellido---> {self.apellidos}")
        print(f"nombre---> {self.nombres}")
        print(f"area---> {self.area}")
        print(f"salario---> {self.salario}")
    
    def calcularSalario(self,nroHoras):
        vlrDia = self.salario / 30
        vlrHora = vlrDia / 8
        vlrSalario = nroHoras * vlrHora
        datos=[vlrDia,vlrHora,vlrSalario]
        return datos #retorna una lista
        
    def imprimirColilla(self, datos):
        print("----------------------------------------------------")
        print("             ***COLILLA DE PAGO***                  ")
        print("----------------------------------------------------\n")
        print(f"cedula---> {self.IdEmpleado}")
        print(f"apellido---> {self.apellidos}")
        print(f"nombre---> {self.nombres}")
        print(f"area---> {self.area}")
        print(f"salario---> {self.salario}")
        print(f"valor Dia---> {datos[0]}")
        print(f"valor Hora---> {datos[1]}")
        print(f"valor Pagar---> {datos[2]}")
    
    
       
        
if __name__ == "__main__":
    #crear un objeto empleado a partir de la clase Empleado
    # instanciar el objeto, crearlo
    empleado1 = Empleado(123,"agudelo","cesar","ti",2000000)
    empleado1.imprimirDatos()
    datos = empleado1.calcularSalario(280)
    empleado1.imprimirColilla(datos)
    
    
    
    #empleado2 = Empleado(456,"mejia","augusto","ti",3000000)
    #empleado2.imprimirDatos()
    
    
    
    