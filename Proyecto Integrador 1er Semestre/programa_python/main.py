import csv

provincias = {
    "01": "Azuay",
    "02": "Bolívar",
    "03": "Cañar",
    "04": "Carchi",
    "05": "Cotopaxi",
    "06": "Chimborazo",
    "07": "El Oro",
    "08": "Esmeraldas",
    "09": "Guayas",
    "10": "Imbabura",
    "11": "Loja",
    "12": "Los Ríos",
    "13": "Manabí",
    "14": "Morona Santiago",
    "15": "Napo",
    "16": "Pastaza",
    "17": "Pichincha",
    "18": "Tungurahua",
    "19": "Zamora Chinchipe",
    "20": "Galápagos",
    "21": "Sucumbíos",
    "22": "Orellana",
    "23": "Santo Domingo de los Tsáchilas",
    "24": "Santa Elena"

}


def validar_cedula(cedula):

    valida = False

    if len(cedula) == 10:

        try:

            int(cedula)

            valida = True

        except ValueError:

            valida = False

    return valida


def obtener_provincia(cedula):

    codigo = cedula[0:2]

    if codigo in provincias:

        provincia = provincias[codigo]

    else:

        provincia = "Código provincial no válido"

    return provincia


def guardar_cedula(cedula, codigo, provincia):

    with open("cedulas.csv", 'a', newline="") as archivo:

        escritor = csv.writer(archivo)

        escritor.writerow([cedula, codigo, provincia])


def mostrar_registros():

    try:

        with open('cedulas.csv', 'r') as archivo:

            lector = csv.reader(archivo)

            print("==================================")
            print(" REGISTROS GUARDADOS")
            print("==================================")

            contador = 1

            for fila in lector:
                
                if len(fila) > 0:

                    print('CÉDULA:', contador)
                    print('Cédula:', fila[0])
                    print('Código:', fila[1])
                    print('Provincia:', fila[2])
                    print()

                    contador = contador + 1

    except FileNotFoundError:

        print('No existen registros guardados')


def buscar_cedula():

    cedula_buscar = input('Ingrese la cédula que desea buscar: ')

    encontrada = False
    
    if validar_cedula(cedula_buscar):

        try:

            with open('cedulas.csv', 'r') as archivo:

                lector = csv.reader(archivo)

                for fila in lector:
                    
                    if len(fila) > 0:

                        if fila [0] == cedula_buscar:

                            print()
                            print('CÉDULA ENCONTRADA')
                            print('Cédula:', fila[0])
                            print('Código:', fila[1])
                            print('Provincia:', fila[2])
                            print()

                            encontrada = True

        except FileNotFoundError:

            print('No existen registros guardados')

        if encontrada == False:

            print('Cédula no encontrada')
    
    else:
        print('Cédula no válida')
        
        
def eliminar_cedula():

    cedula_eliminar = input("Ingrese la cédula que desea eliminar: ")

    registros = []
    
    encontrada = False
    
    if validar_cedula(cedula_eliminar):
        
        try:

            with open("cedulas.csv", "r") as archivo:

                lector = csv.reader(archivo)

                for fila in lector:
                    
                    if len(fila) > 0:

                        if fila[0] == cedula_eliminar:
                            
                            encontrada = True
                            
                        else:

                            registros.append(fila)

        except FileNotFoundError:
            
            print('No existen registros guardados')
            
            
        if encontrada == True:
            
            with open("cedulas.csv", "w", newline="") as archivo:

                escritor = csv.writer(archivo)

                escritor.writerows(registros)
                
            print("Cédula eliminada correctamente")
            
        else:
            
            print('Cédula no encontrada')
            
    else:
        
        print('Cédula no válida')    
            


def cedula_repetida(cedula):
    
    repetida = False
    
    try:
        
        with open ('cedulas.csv', 'r') as archivo:
            
            lector = csv.reader(archivo)
            
            for fila in lector:
                
                if len(fila) > 0:
                
                    if fila[0] == cedula:
                        
                        repetida = True
    
    except FileNotFoundError:
        
        repetida = False
        
    return repetida
            

print("==================================")
print(" SISTEMA DE REGISTRO DE CÉDULAS")
print("==================================")

opcion = 0

while opcion != 5:

    print()
    print("1. Registrar cédula")
    print("2. Mostrar registros")
    print("3. Buscar cédula")
    print("4. Eliminar cédula")
    print("5. Salir")

    print()

    try:
        
        opcion = int(input("Seleccione una opción: "))
        
    except ValueError:
        
        opcion = 0

    if opcion == 1:

        cedula = input("Ingrese el número de cédula: ")

        if validar_cedula(cedula):

            codigo = cedula[0:2]

            provincia = obtener_provincia(cedula)

            if provincia != 'Código provincial no válido':
                
                if cedula_repetida(cedula):
                    
                    print('La cédula ya está registrada')
                
                else:

                    guardar_cedula(cedula, codigo, provincia)

                    print('Provincia:', provincia)

                    print('Cédula guardada correctamente')

            else:
                print('Código provincial no válido')

        else:

            print("Cédula no válida")


    elif opcion == 2:

        mostrar_registros()

    elif opcion == 3:

        buscar_cedula()

    elif opcion == 4:

        eliminar_cedula()

    elif opcion == 5:

        print('Programa finalizado')

    else:
        print('Opción incorrecta')
