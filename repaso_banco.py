def validador(usuario):
    intentos = 0
    max_intentos = 3
    
    while intentos < max_intentos:
        contraseña = input("Ingresa tu contraseña\n>>> ")
        
        if contraseña in usuario:
            datos = usuario[contraseña]
            print(f"Hola bienvenido {datos['tipo']} {datos['nombre']}")
            break
        else:
            intentos += 1
            if intentos > max_intentos:
                print("Numero de intentos maximos alcanzados")
            else:
                print("Contraseña incorrecta")

def main():

    usuarios = {
    'user123': {'nombre': 'sebastian', 'tipo': 'usuario', 'cedula': '12345'},
    'admin123': {'nombre': 'oscar', 'tipo': 'admin', 'cedula': '09876'}
    }

    validador(usuarios)

main()