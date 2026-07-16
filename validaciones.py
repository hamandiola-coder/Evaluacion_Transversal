def mostrar_opciones():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por categoría")
    print("2. Búsqueda de productos por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")

#opcion 1
def unidades_categoria(categoria):
    categoria=input("Ingrese la categoria: ").strip().lower()
    return categoria







def leer_opcion():
    try:
        opcion=input("Ingrese una opcion: ")
        return opcion

    except ValueError:
        print("Ingrese una opcion valida para continuar")    



def busqueda_precio(p_min, p_max):
    try:
       precio_minimo=int(input("Ingrese el precio minimo: "))
       precio_maximo=int(input("Ingrese el precio maximo: "))
    except ValueError:
        print("Debe ingresar valores enteros")    
def buscar_codigo(codigo):
    codigo=input("Ingrese el codigo del producto: ")
    if codigo in stock:

        True
    else:
        False    
def actualizar_precio(codigo,nuevo_precio):
    buscar_codigo()



def agregar_producto(producto):
    print("Agregando productos")
    codigo=input("Ingrese el  codigo del producto: ")
    nombre=input("Ingrese el nombre del producto: ")
    categoria=input("Ingrese la categoria del producto").strip().lower()
    marca=input("Ingrese la marca del producto: ").strip().lower()
    peso_kg=float(input("Ingrese el peso del producto: "))
    es_importado=input("El producto es importado s/n")
    es_para_cachorro=input("El producto es para cachorro s/n")
    precio=int(input("Ingrese el precio del producto"))>0
    unidades=int(input("Ingrese las unidades del producto"))>0
    if not buscar_codigo(codigo):
    if not
#opcion 5      
def eliminar_producto(codigo):
    buscar_codigo()
    if codigo in stock:
        codigo.pop(productos)
        