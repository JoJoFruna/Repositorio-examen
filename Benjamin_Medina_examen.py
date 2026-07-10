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

def unidades_categoria(categoria, productos, stock):
    total_unidades = 0
    cat_buscar = categoria.strip().lower()
    
    for codigo, datos in productos.items():
        if datos[1].lower() == cat_buscar:
            if codigo in stock:
                total_unidades += stock[codigo][1]
                
    print(f"El total de unidades disponibles es: {total_unidades}")

def busqueda_precio(p_min, p_max, productos, stock):
    resultados = []

    for codigo, datos_stock in stock.items():
        precio = datos_stock[0]
        unidades = datos_stock[1]
    
        if p_min <= precio <= p_max and unidades > 0:
            if codigo in productos:
                nombre = productos[codigo][0]
                resultados.append(f"{nombre}--{codigo}")
    
    if resultados:
        resultados.sort()  
        print(f"Los productos encontrados son: {resultados}")
    else:
        print("No hay productos en ese rango de precios.")

def actualizar_precio(codigo, nuevo_precio, stock):
    clave_real = None
    for k in stock.keys():
        if k.upper() == codigo.upper():
            clave_real = k 
            break
    
    if clave_real is not None:
        stock[clave_real][0] = nuevo_precio
        return True
    return False

def
