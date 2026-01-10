class Cliente():

    def __init__(self, nombre, valor_compra):
        self.nombre = nombre
        self.valor_compra = valor_compra
    
    def calcular_descuento(self):
        descuento_total = 0
        if self.valor_compra >= 200000:
            return self.valor_compra * 0.20
        elif self.valor_compra < 200000:
            return self.valor_compra * 0.05
        else:
            print("Valor ingresado incorrecto")

    def calcular_total_pagar(self):
        descuento = self.calcular_descuento()
        return self.valor_compra - descuento
    
def menu():
    menu_usuario = int(input("Que opcion deseas usar\n1. Crear Cliente\n2. Ver Clientes\n3. Calcular total a pagar de un cliente\n4. Salir"))
    for i in menu_usuario:
        if i > 4:
            break
        if i == 1:
            crear_cliente()
        if i == 2:
            # opcion para ver clientes creados
        if i == 3:
            Cliente.calcular_total_pagar()

def crear_cliente():
    nombre_nuevo_usuario = str(input("Ingresa tu nombre\n>>> "))
    valor_compras = validar_valor_compra()
    cliente_nuevo = Cliente(nombre_nuevo_usuario, valor_compras)
    return cliente_nuevo

def validar_valor_compra():
    while True:
        try:
            valor = float(input("Ingresa el valor de las compras\n>>> "))
            if valor < 0:
                print("Error: el valor no puede ser negativo.")
            else:
                return valor
        except ValueError:
            print("Error: debes ingresar un número válido.")

def main():
    cliente = crear_cliente()

    descuento = cliente.calcular_descuento()
    total = cliente.calcular_total_pagar()

    print(f"Bienvenido !{cliente.nombre}¡")
    print(f"Descuento aplicado: {descuento}")
    print(f"Total a pagar: {total}")

main()