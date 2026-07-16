import validaciones as vld



productos = {
    'M001': ['Alimento Premium', 'comida', 'DogPlus', 10, True, False],
    'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 8, False, False],
    'M003': ['Snack Dental', 'snack', 'BiteJoy', 1, True, True],
    'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False, True],
    'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True, False],
    'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2, False, False]
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
    vld.mostrar_opciones()
    vld.leer_opcion()
    if opcion=="1":
        
        print("Ingrese categoria a consultar")
        vld.unidades_categoria()
        for producto in productos:
            if producto

    elif opcion==2:
        vld.busqueda_precio()
        lista=()
    elif opcion==3:
    elif ocpion==4:
        print("Agregar producto")
        if 
    elif opcion==5:
    elif opcion==6:
       
        print("Programa finalizado.")
        break                




