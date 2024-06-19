import os, time
from funciones import *

while True:
    os.system("cls")
    print("menú contactos")
    print("1. agregar contacto\n2. ver contacos\n3. exportar archivo csv\n4. salir")
    opc = int(input("ingrese opción: "))

    os.system("cls")
    if opc==1:
        opcion_1()
    elif opc==2:
        opcion_2()
    elif opc==3:
        opcion_3()
    else:
        opcion_4()
    time.sleep(3)
