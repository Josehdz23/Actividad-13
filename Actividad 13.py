class Repartidor:
    def __init__(self, nombre, cantidad, zona):
        self.cantidad = cantidad
        self.zona = zona
        self.nombre = nombre
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
for i in range(3):
    nombre = input("Ingrese el nombre: ")
    cantidad = int(input("Ingrese el cantidad: "))
    zona = input("Ingrese el zona: ")
    repartidor = Repartidor(nombre, cantidad, zona)
    repartidores[repartidor.nombre] = {
        "cantidad": repartidor.cantidad,
        "zona": repartidor.zona
    }
    for clave, dato in repartidores.items():
        print(clave, dato["cantidad"], dato["zona"])



lista = list(repartidores.items())
ordenada = quick_sort(lista)
ordenadoD = dict(ordenada)

for clave2, dato2 in ordenadoD.items():
    print(clave2, dato2["cantidad"], dato2["zona"])



