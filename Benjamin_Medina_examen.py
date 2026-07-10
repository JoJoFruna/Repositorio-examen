def validar_no_vacio(texto):
    return texto.strip() != ""

def validar_codigo_nuevo(codigo, productos):
    if not validar_no_vacio(codigo):
        return False
    # Corregido .key() a .keys() y el uso del diccionario correcto
    return codigo.upper() not in [k.upper() for k in productos.keys()]

def validar_peso(peso_str):
    try:
        # Corregido: antes usaba la variable 'precio' por error
        peso = float(peso_str) 
        return peso > 0
    except ValueError:
        return False # Corregido: faltaba el return

def validar_sn(respuesta):
    """Valida que la respuesta sea 's' o 'n'."""
    return respuesta.strip().lower() in ['s', 'n']

def validar_precio(precio_str):
    """Valida que el precio sea un entero mayor que cero."""
    try:
        precio = int(precio_str)
        return precio > 0
    except ValueError:
        return False

def validar_unidades(unidades_str):
    try:
        unidades = int(unidades_str)
        return unidades >= 0
    except ValueError:
        return False

# parte 2

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

def agregar_producto(codigo, nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro, precio, unidades, productos, stock):
    codigo = codigo.upper() # Corregido asignación de método .upper()
    if buscar_codigo(codigo, productos):
        return False
    
    productos[codigo] = [nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro]
    stock[codigo] = [precio, unidades]
    return True

def eliminar_producto(codigo, productos, stock):
    clave_real = None
    for k in productos.keys(): # Corregido .key() a .keys()
        if k.upper() == codigo.upper():
            clave_real = k
            break
    
    if clave_real is not None:
        del productos[clave_real]
        if clave_real in stock:
            del stock[clave_real]
        return True
    return False

def main():
    productos = {
        'M001': ['Alimento Premium', 'comida', 'DogPlus', 10.0, True, False],
        'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 8.0, False, False],
        'M003': ['Snack Dental', 'snack', 'BiteJoy', 1.0, True, True],
        'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False, True],
        'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True, False],
        'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2.0, False, False]
    } 

    stock = {
        'M001': [32990, 12],
        'M002': [9990, 0],
        'M003': [5490, 25],
        'M004': [7990, 5],
        'M005': [11990, 7],
        'M006': [24990, 3]
    }

    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Unidades por categoría")
        print("2. Búsqueda de productos por rango de precio")
        print("3. Actualizar precio de producto")
        print("4. Agregar producto")
        print("5. Eliminar producto")
        print("6. Salir")
        print("=====================================")

        opcion = leer_opcion()  
        
        if opcion == 1:
            cat = input("ingrese categoria a consultar: ")
            unidades_categoria(cat, productos, stock)
        
        elif opcion == 2:
            while True:
                try:
                    p_min = int(input("ingrese precio minimo: "))
                    p_max = int(input("ingrese precio maximo: "))
                    if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                        break
                    else:
                        print("debe ingresar valores validos (mayores a 0 y minimo menor que le maximo).")
                except ValueError:
                    print("Debe ingresar valores enteros")
            
            busqueda_precio(p_min, p_max, productos, stock)
        
        elif opcion == 3:
            otra_vez = 's'
            while otra_vez == 's':
                cod = input("ingrese codigo del producto: ")
                precio_str = input("ingrese nuevo precio: ")

                if validar_precio(precio_str):
                    nuevo_p = int(precio_str)
                    if actualizar_precio(cod, nuevo_p, stock):
                        print("precio actualizado")
                    else:
                        print("el codigo no existe")
                else:
                    print("precio no valido. debe ser entero positivo.")
                
                otra_vez = input("¿desea actualizar otro precio? (s/n) ").strip().lower()

        elif opcion == 4:
            cod = input("Ingrese código del producto: ")
            nom = input("Ingrese nombre: ")
            cat = input("Ingrese categoría: ")
            mar = input("Ingrese marca: ")
            peso = input("Ingrese peso (kg): ")
            imp = input("¿Es importado? (s/n): ")
            cach = input("¿Es para cachorro? (s/n): ")
            prec = input("Ingrese precio: ")
            unid = input("Ingrese unidades: ")
            
            # Corregido: pasamos 'productos' en lugar del inexistente 'producto'
            if not validar_codigo_nuevo(cod, productos): 
                print("Error: Código inválido o ya existente.")
            elif not validar_no_vacio(nom):
                print("Error: Nombre no puede estar vacío.")
            elif not validar_no_vacio(cat):
                print("Error: Categoría no puede estar vacía.")
            elif not validar_no_vacio(mar):
                print("Error: Marca no puede estar vacía.")
            elif not validar_peso(peso):
                print("Error: Peso inválido.")
            elif not validar_sn(imp):
                print("Error: Respuesta de importación debe ser 's' o 'n'.")
            elif not validar_sn(cach):
                print("Error: Respuesta de cachorro debe ser 's' o 'n'.")
            elif not validar_precio(prec):
                print("Error: Precio inválido.")
            elif not validar_unidades(unid):
                print("Error: Unidades inválidas.")
            else:
                peso_val = float(peso)
                imp_val = True if imp.lower() == 's' else False
                cach_val = True if cach.lower() == 's' else False
                prec_val = int(prec)
                unid_val = int(unid)
                
                if agregar_producto(cod, nom, cat, mar, peso_val, imp_val, cach_val, prec_val, unid_val, productos, stock):
                    print("Producto agregado")
                else:
                    print("El código ya existe")
                    
        elif opcion == 5:
            cod = input("Ingrese código del producto: ")
            if eliminar_producto(cod, productos, stock):
                print("Producto eliminado")
            else:
                print("El código no existe")
                
        elif opcion == 6:
            print("Programa finalizado.")
            break

if __name__ == "__main__":
    main()
                



            