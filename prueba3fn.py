def menu():
    print("Bienvenido!")
    print("1) Grabar")
    print("2) Buscar")
    print("3) Imprimir parejas")
    print("4) Salir")
    return ValidaNro((int),"Elija su opción porfavor: ",1,4)

def ValidaNro(tipo,TextoInput,rmin=None,rmax=None):
    while True:
        try:
            nro=tipo(input(TextoInput))
            if rmin != None and rmax != None:
                if rmin<=nro<=rmax:
                    break
                else:
                    print("Valor fuera de rango.")
            elif rmin!=None:
                if nro>=rmin:
                    break
            else:
                print(f"Valor ingresado debe ser mayor o igual a {rmin}")
            if rmax!=None:
                if nro<=rmax:
                    break
                else:
                    print(f"Valor ingresado debe ser menor o igual a {rmax}")
            else:
                break
        except:
            print("No debe ser letra.")
    return nro

def validar_letra(textoInput):
    while True:
        letra=input(textoInput)
        if letra.isalpha():
            break
        else:
            print("Ingrese solo letras.")
    return letra


def AgregarDatosJugadores(lista1,lista2,lista3,lista4,lista5,lista6,lista7,lista8):
    nombre=Longitud("Ingrese nombre del jugador: ",2)
    nombre=nombre.capitalize()
    lista1.append(nombre)
    agregar_rut=input("Ingrese el rut: ")
    lista2.append(agregar_rut)
    fecha_nac=input("Ingrese la fecha de nacimiento (Día-Mes): ")
    lista3.append(fecha_nac)
    annio_nac=ValidaNro(int,"Ingrese el año de nacimiento (formato 4 dígitos): ",1943,2003)
    lista4.append(annio_nac)
    categoria(lista5)
    celular=ValidaNro(int, "Ingrese el celular: ",9)
    lista6.append(celular)
    correo=AgregarCorreo("Ingrese el correo: ")
    lista7.append(correo)
    identificador=ValidaNro(int, "Ingrese el identificador del jugador (del 1 al 999): ",100,999)
    lista8.append(identificador)

def AgregarNumeros(TextoInput,lonMin):
    agregar_numeros=input(TextoInput)
    while True:
        try:
            numeros=int(agregar_numeros)
            if len(str(numeros))<lonMin:
                print(f"Tiene que ser un minímo de {lonMin} dígitos!")
                continue
            elif len(str(numeros))>lonMin:
                print(f"No puede sobrepasar los {lonMin} dígitos!")
                continue
            else:
                break
        except:
            print("Tiene que ser un número!")
    return agregar_numeros

def AgregarCorreo(TextoInput):
    while True:
        agregar_dato=input(TextoInput)
        try:
            if len(agregar_dato)<6:
                print("El correo debe tener un mínimo de 6 caracteres.")
                continue
            elif "@" not in agregar_dato and "." not in agregar_dato:
                print ("El correo debe contener el símbolo '@' y un punto.")
                continue
            elif "@" not in agregar_dato:
                    print ("El correo debe contener el símbolo '@'")
                    continue
            elif "." not in agregar_dato:
                    print ("El correo debe contener un punto.")
                    continue
        except:
            break
        return agregar_dato

def Longitud(TextoInput,lonMin=None,lonMax=None):
    while True:
        agregar_dato=input((TextoInput))
        longitud=int(len(agregar_dato))
        try:
            if lonMin!=None and longitud<lonMin:
                print(f"Tiene que ser un minímo de {lonMin} caracteres.")
            elif lonMax!=None and longitud>lonMax:
                print(f"No puede sobrepasar los {lonMax} caracteres.")
        except:
            break
        return agregar_dato
    
def categoria(lista):
    categoria=" "
    print("1) Bronce")
    print("2) Plata")
    print("3) Bronce")
    while True:
        opc=input("Seleccione la categoría: ")
        try:
            if opc=="1":
                categoria="Oro"
                break
            elif opc=="2":
                categoria="Plata"
                break
            elif opc=="3":
                categoria="Bronce"
                break
            else:
                raise
        except:
            print("Opción inválida.")
    lista.append(categoria)

def MostrarParticipante(rut,nombreJug,categoria,celular,correo):
    filtro=input("Ingrese Rut del participante: ")
    encontrado=False
    for i in range(len(rut)):
        if rut[i] == filtro:
            encontrado=True
            rut[i] = nombreJug[i]
            rut[i] = categoria[i]
            rut[i] = celular[i]
            rut[i] = correo[i]
            print("Este rut pertenece al jugador: ")
            print("Nombre: ",nombreJug[i])
            print("Rut: ",rut[i])
            print("Categoría: ",categoria[i])
            print("Celular: ",celular[i])
            print("Correo: ",correo[i])
            break
    if encontrado==False:
        print("No se encontró al participante")

def EncontrarCodigo(parejas,nombreJug):
    filtro=ValidaNro(int, "Ingrese el identificador (del 100 al 999): ",100,999)
    encontrado=False
    for i in range(len(parejas)):
        if parejas[i]==filtro:
            encontrado=True
            parejas[i]=nombreJug[i]
            print("Los integrantes de este equipo son: ",nombreJug[i] )
