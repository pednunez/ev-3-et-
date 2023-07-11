import numpy as np

# Declaracion de elementos del programa.
lista=[['A4','B4','C4','D4'],
        ['A3','B3','C3','D3'],
        ['A2','B2','C2','D2'],
        ['A1','B1','C1','D1']]

lista_compradores=[]
lista_totales=[]
matriz=np.array(lista)

def comprarDepartamento():
    print("\nCOMPRAR DEPARTAMENTO\n")
    print(matriz)
    existe = True
    flag_reserva=True
    datos_ingresados=False
    try:
        while flag_reserva==True:
            flag1=True
            while flag1==True:
                piso=input("Seleccione un piso entre 1 y 4: ")
                if not piso:
                    print("Piso incorrecto")
                else:
                    try:
                        int(piso)
                        it_is = True
                    except ValueError:
                        it_is = False

                    if  it_is==True:
                        if int(piso) > 0 and int(piso) < 11:
                            flag1=False
                        else:
                            print('Piso incorrecto')
                    else:
                        print('Piso incorrecto')
            flag2=True
            while flag2==True:
                tipo=input("Seleccione un tipo de departameto A-B-C-D: ")
                tipo=tipo.upper()
                if not tipo:
                    print("Tipo incorrecto")
                else:
                    if tipo == 'A':
                        flag2=False
                    elif tipo == 'B':
                        flag2=False
                    elif tipo == 'C':
                        flag2=False
                    elif tipo == 'D':
                        flag2=False
                    else:
                        print("Tipo incorrecto")

            flag3=True
            while flag3==True:
                rut=input("Ingrese rut sin guion, ni puntos y sin digito verificador: ")
                if not rut:
                    print("rut incorrecto")
                else:
                    if len(rut) == 8:
                        if rut.isdigit():
                            flag3=False
                        else:
                            print("Rut incorrecto")
                    else:
                        print("Rut incorrecto")

            a_comprar=tipo+piso
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    if matriz[i][j] == a_comprar:
                        matriz[i][j] = 'X'

                        if tipo == 'A':
                            valor=3800
                        elif tipo == 'B':
                            valor=3000
                        elif tipo == 'C':
                            valor=2800
                        elif tipo == 'D':
                            valor= 3500

                        lista_compradores.append([rut,a_comprar,valor])
                        lista_totales.append([tipo,valor])
                        flag_reserva=False
                        existe = False
                        print("\nDepartamentos vendido de forma exitosa.\n")
                        break

            if existe==True:
                print("\nDepartamento no disponible, ingrese datos nuevamente.\n")
    except:
        print("\nIngreso Invalido.\n")

def verDepartamentoDisponibles():
    print("\nDEPARTAMENTOS DISPONIBLES\n")
    print(matriz)

def verListadoCompradores():
    print("\nLISTADO DE COMPRADORES\n")
    ordenados = sorted(lista_compradores)
    for x in ordenados:
        print(f"RUT :{x[0]} | DEPARTAMENTO VENDIDO :{x[1]} | VALOR UF:{x[2]}")

def mostrarGanancias():
    print("\nGANANCIAS\n")
    cantidad1=0
    totaluf1=0
    for x in lista_totales:
        if x[0] =='A':
            cantidad1 += 1
            totaluf1=totaluf1+x[1]

    cantidad2=0
    totaluf2=0
    for x in lista_totales:
        if x[0] =='B':
            cantidad2 += 1
            totaluf2=totaluf2+x[1]

    cantidad3=0
    totaluf3=0
    for x in lista_totales:
        if x[0] =='C':
            cantidad3 += 1
            totaluf3=totaluf3+x[1]

    cantidad4=0
    totaluf4=0
    for x in lista_totales:
        if x[0] =='D':
            cantidad4 += 1
            totaluf4=totaluf4+x[1]

    cantidadT=cantidad1+cantidad2+cantidad3+cantidad4
    sumaTotal=totaluf1+totaluf2+totaluf3+totaluf4

    print("TIPO DEPARTAMENTO | CANTIDAD    | TOTAL")
    print("____________________________________________")
    print(f"TIPO A 3800 UF   | {cantidad1} | {totaluf1}")
    print(f"TIPO B 3000 UF   | {cantidad2} | {totaluf2}")
    print(f"TIPO C 2800 UF   | {cantidad3} | {totaluf3}")
    print(f"TIPO D 3500 UF   | {cantidad4} | {totaluf4}")
    print("____________________________________________")
    print(f"TOTAL            | {cantidadT} | {sumaTotal}")

# MENU PRINTCIPAL
principal=True
try:
    while principal==True:
        menu=int(input('''
            MENU VENTA DEPARTAMENTO
        [1] COMPRAR DEPARTAMENTO
        [2] MOSTRAR DEPARTAMENTOS DISPONIBLES
        [3] VER LISTADO DE COMPRADORES
        [4] MOSTRAR GANANCIAS TOTALES
        [5] SALIR
        Seleccione opcion: '''))

        if menu ==5:
            principal=False
            print("\nGRACIAS POR COMPRAR DEPARTAMENTOS.")
        elif menu==1:
            comprarDepartamento()
        elif menu==2:
            verDepartamentoDisponibles()
        elif menu==3:
            verListadoCompradores()
        elif menu==4:
            mostrarGanancias()
except:
    print("\nIngreso Invalido.")
