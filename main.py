lista_vendedores = []

def mostrar_liquidacion(nombre_vendedor, cantidad_ventas, monto_total, sueldo_comision):
    return f"""
Recibo de sueldo del vendedor {nombre_vendedor}
Cantidad de ventas realizadas: {cantidad_ventas}
Monto total de las ventas: ${monto_total:.2f}
Sueldo por comision: ${sueldo_comision:.2f}
"""

def calcular_comision(monto_total):
    if monto_total <= 100000:
        sueldo_comision = monto_total * 0.05
    if monto_total > 100000 and monto_total <= 300000:
        sueldo_comision = monto_total * 0.10
    if monto_total > 300000:
        sueldo_comision = monto_total * 0.15
    return sueldo_comision
 
# HACER QUE FUNCIONE EN EL PROGRAMA (OWEN)
def agregar_vendedor(Nombre, Ventas, Comisiones, Bonos):
    vendedor = {
        "Nombre": Nombre,
        "Ventas": Ventas,
        "Comisiones": Comisiones,
        "Bonos": Bonos
    }
    lista_vendedores.append(vendedor)

while True:
    try:
        # Mostrar menu
        print("Selecciona la opcion que deseas realizar")
        print("1- Calcular comision")
        print("2- Ver recibos de sueldo")
        print("3- Informe de vendedores")
        print("4- Salir")
        opc = int(input("Opcion: "))
 
        # Realizar accion del menu
        match opc:
 
            case 1:
                print("|------------------|")
                print("calcular comision")
                print("|------------------|")
 
                # NOMBRE DEL VENDEDOR
                while True:
                    nombre_vendedor = input("Ingrese su nombre:")
                    if nombre_vendedor.isalpha():
                        break
                    else:
                        print("Error: Debes ingresar un nombre alfanumerico.")
 
                # CANTIDAD DE VENTAS
                while True:
                    try:
                        cantidad_ventas = int(input("Ingrese la cantidad de ventas realizadas:"))
                        if cantidad_ventas > 0 and cantidad_ventas <= 10000:
                            break
                        else:
                            print("Error: Debes ingresar un número entre 1 y 10000.")
                    except ValueError:
                        print("Error: Debes ingresar un número entero.")
 
                # MONTO TOTAL DE LAS VENTAS
                while True:
                    try:
                        monto_total = int(input("Ingrese el monto total de las ventas:"))
                        if monto_total > 0:
                            break
                        else:
                            print("Error: Debes ingresar un monto mayor a 1.")
                    except ValueError:
                        print("Error: Debes ingresar un número entero.")
 
                # Llamar a funcion para calcular comision
                sueldo_comision = calcular_comision(monto_total)
                print("|---------------------------------------------------------------------------------|")
                print(f"El vendedor {nombre_vendedor} ha realizado {cantidad_ventas} ventas por un sueldo total de ${sueldo_comision:.2f}.")
                print("|---------------------------------------------------------------------------------|")
                
                agregar_vendedor(nombre_vendedor, cantidad_ventas, sueldo_comision, 0)

            case 2:
                print("|------------------|")
                print("Recibo de sueldo")
                print("|------------------|")
                while True:
                    nombre = input("Ingrese su nombre: ")
                    if nombre.isalpha():
                        break
                    else:
                        print("Error: Debes ingresar un nombre en texto.")
                
                for vendedor in lista_vendedores:
                    try:
                        if nombre == vendedor["Nombre"]:
                            print("|---------------------------------------------------|")
                            print(mostrar_liquidacion(nombre, vendedor["Ventas"], vendedor["Comisiones"], vendedor["Bonos"]))
                            print("|---------------------------------------------------|")
                            break
                    except KeyError:
                        print("Error: No existe ese vendedor.")
                        
            case 3:
                pass
                    
 
            case 4:
                print("|------------------|")
                print("Saliendo...")
                print("|------------------|")
                exit()
                break
 
            case _:
                print("Error: Debes de ingresar una opcion valida.")
 
    except ValueError:
        print("Error: Debes ingresar un número entero.")

