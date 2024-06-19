contactos = []

def opcion_1():
    print("AGREGAR CONTACTO")
    nombre = validar_nombre()
    telefono = validar_telefono()
    correo = validar_correo()
    contacto ={"nombre":nombre, "telefono":telefono, "correo":correo}
    contactos.append(contacto)
    print("contacto agregado!")



def opcion_2():
    if len(contactos)==0:
        print("no existen contactos")
    else:
        print("\tlista de contactos")
        for c in contactos:
            print(f"nombre: {c["nombre"]}")
            print(f"telefono: {c["nombre"]}")
            print(f"correo: {c["nombre"]}\n")

def opcion_3():
    if not contactos==0:
        print("no existen contactos")
    else:
        nombre_archivo = input("ingrese nombre del archivo: ")+".csv"
        try:
            import csv
            with open(nombre_archivo, "w", newline="") as archivo:
                escritor = csv.DictWriter(archivo, ["nombre","telefono","correo"])
                escritor.writerows(contactos)
        except:
            print("error el archivo ya existe!")

def opcion_4():
    print("gracias, a dios!")
    exit()



def validar_nombre():
    while True:
        nom = input("ingrese nombvre: ")
        if len(nom.strip())>=3 and nom.isalpha():
            return nom
        else:
            print("error, el nombre debe tener al menos 3 caracteres y solo letras!")


def validar_telefono():
    while True:
        try:
            tel = int(input("ingrese numero telefono"))
            if len(str(tel))==9 and str(tel)[0]=="9":
                return tel
            else:
                print("error!")
        except:
            print("error")


def validar_correo():
    while True:
        #patterns
        cor = input("ingrese correo: ")
        if cor.strip().lower().endswith("@gmail.com") and len(cor.strip())>=13:
            return cor
        else:
            print("error! solo acepto gmail")
