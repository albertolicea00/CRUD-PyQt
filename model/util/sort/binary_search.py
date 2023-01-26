def busqueda_binaria(dato):
    izq = 0
    der = len(lista)-1
    while izq <= der:
        medio = (izq + der) // 2
        if dato == lista[medio]:
            return medio
        elif dato < lista[medio]:
            der = medio - 1
        else:
            izq = medio + 1
    return None