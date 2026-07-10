def validar_no_vacio(texto):
    return texto.strip() != ""

def validar_codigo_nuevo(codigo, producto):
    if not validar_no_vacio(codigo):
        return False
    return codigo.upper() not in [k.upper() for k in productos.key()]

def validar_peso(peso_str):
    try:
        precio = int(precio_str)
        return precio > 0
    except ValueError:
        False

def validar_unidades(unidades_str):
    try:
        unidades = int(unidades_str)
        return unidades >= 0
    except ValueError:
        return False

#parte 2

def leer_opcion():
    while True:
        try:
            opcion = int(input("ingrese opcion: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("debe seleccionar una opcion valida")
        except ValueError:
            print("Debe seleccionar una opción válida")

def buscar_codigo(codigo, diccionario):
    for clave in diccionario.keys():
        if clave.upper() == codigo.upper():
            return True
    return False