class Repartidor:
    def __init__(self, cantidad, zona):
        self.cantidad = cantidad
        self.zona = zona
    def __str__(self):
        return f"Cantidad: {self.cantidad} Zona: {self.zona}"

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x[1]["cantidad"] < pivote[1]["cantidad"]]
        iguales = [x for x in lista if x[1]["cantidad"] == pivote[1]["cantidad"]]
        mayores = [x for x in lista[1:] if x[1]["cantidad"] > pivote[1]["cantidad"]]
        return quick_sort(mayores) + iguales + quick_sort(menores)

repartidores = {}
def menu():
    print("\n===== Control de Entregas =====\n1. Ingreso de repartidores\n2. Ordenamiento por paquetes\n3. Busqueda de repartidor\n4. Estadisticas\n5. Salir")

def ingreso():
    while True:
        try:
            NoRepartidores = int(input("Ingrese cuántos repartidores participaron: "))
            for i in range(NoRepartidores):
                print(f"\nRepartidor {i+1}: ")
                while True:
                    nombre = input("Ingrese nombre: ")
                    if nombre in repartidores:
                        print(f"El nombre ({nombre}) ya existe, reintente")
                    else:
                        if nombre or nombre.isspace():
                            break
                        else:
                            print("El nombre no es válido")
                while True:
                    try:
                        cantidad = int(input("Ingrese cantidad de paquetes entregados: "))
                        if cantidad > 0:
                            break
                        else:
                            print("No se permiten cantidades negativas, reintente")
                    except Exception as ex:
                        print(f"Ha ocurrido un error: {ex}")
                while True:
                    zona = input("Ingrese la zona (Norte, Sur, Este, Oeste): ").upper()
                    if ((zona == "NORTE") or (zona == "SUR")) or ((zona == "ESTE") or (zona == "OESTE")):
                        break
                    else:
                        print("La zona ingresada no es válida")
                repartidores[nombre] = Repartidor(cantidad, zona)
                print("\nRepartidor guardado con exito")
            break
        except Exception as ex:
            print(f"Ha ocurrido un error: {ex}")

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x[1].cantidad < pivote[1].cantidad]
        iguales = [x for x in lista if x[1].cantidad == pivote[1].cantidad]
        mayores = [x for x in lista[1:] if x[1].cantidad > pivote[1].cantidad]
        return quick_sort(mayores) + iguales + quick_sort(menores)

def mostrarRepartidores():
    if repartidores:
        print("\n= = = = = Registro Original = = = = =")
        for clave, obj in repartidores.items():
            print(f"Nombre: {clave} {obj}")
        print("\n= = = = = Ranking = = = = =")
        lista = list(repartidores.items())
        ordenado = quick_sort(lista)
        ordenadoD = dict(ordenado)
        for clave2, obj2 in ordenadoD.items():
            print(f"Nombre: {clave2} {obj2}")
    else:
        print("No hay repartidores registrados")

def busqueda_secuencial(lista, busqueda):
    for j in range(len(lista)):
        if lista[j] == busqueda:
            return j
    return -1

def buscarRepartidor():
    if repartidores:
        buscar = input("Ingrese el nombre de un repartidor: ")
        b = busqueda_secuencial(list(repartidores.keys()), buscar)
        if b != -1:
            print(f"{buscar} entregó {repartidores[buscar]['repartidos']} paquetes")
        else:
            print("No existe ese repartidor")
    else:
        print("No hay repartidores registrados")

def estadisticas():
    if repartidores:
        may = 0
        b = 0
        total = 0
        min = 100
        mayor = []
        menor = []
        print("\n= = = = = ESTADISTICAS = = = = =")
        for datos in repartidores.values():
            total = total + datos["repartidos"]
        for clave, dato in repartidores.items():
            if dato["repartidos"] > may:
                may = dato["repartidos"]
                mayor = (clave, dato["repartidos"])
                if b == 0:
                    min = dato["repartidos"]
                    menor = (clave, dato["repartidos"])
                    b = b + 1
            elif dato["repartidos"] < min:
                min = dato["repartidos"]
                menor = (clave, dato["repartidos"])

        promedio = total / len(repartidores)
        print(f"El total de paquetes entregados es: {total}")
        print(f"El promedio de entrega es de: {promedio}")
        print(f"Mayor número de entregas: {mayor[0]} ({mayor[1]})")
        if menor:
            print(f"Menor número de entregas: {menor[0]} ({menor[1]})")
    else:
        print("No hay repartidores registrados")

def main():
    while True:
        try:
            menu()
            op = int(input("Selecciona una opcion: "))
            match op:
                case 1:
                    ingreso()
                case 2:
                    mostrarRepartidores()
                case 3:
                    buscarRepartidor()
                case 4:
                    estadisticas()
                case 5:
                    print("Saliendo. . .")
                    break
                case _:
                    print("Opcion invalida, reintente")
        except Exception as ex:
            print(f"Ha ocurrido un error: {ex}")
main()



