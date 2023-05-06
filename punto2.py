class Producto:
    def __init__(self, IdProducto, Nombre, Precio):
        self.IdProducto= IdProducto
        self.Nombre = Nombre
        self.Precio = Precio

    def calcularSubtotal(self,cantidad):
        vlrSubto= self.Precio *cantidad
        val_cant=[vlrSubto,cantidad]
        return val_cant

    def calcularDescuento(self,vlrSubto,Descuento):
        total =vlrSubto-Descuento
        valores=[total,Descuento]
        return valores

    def imprimirFactura(self,vlrSubto,valores):
        print("----------------------------------------------------")
        print("                 ***FACTURA***                      ")
        print("----------------------------------------------------\n")
        print(f"IdProducto---> {self.IdProducto}")
        print(f"Nombre---> {self.Nombre}")
        print(f"Precio---> {self.Precio}")
        print(f"Cantidad---> {vlrSubto[1]}")
        print(f"Subtotal---> {vlrSubto[0]}")
        print(f"Descuento---> {valores[1]}")
        print(f"Total---> {valores[0]}")

if __name__ == "__main__":
    Producto1 = Producto(111, "Piña", 15000)
    subtotal=Producto1.calcularSubtotal(2)
    total=Producto1.calcularDescuento(subtotal[0],5000)
    Producto1.imprimirFactura(subtotal,total)