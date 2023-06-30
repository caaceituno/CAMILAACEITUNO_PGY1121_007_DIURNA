import prueba3fn as fn

nombreJug=[]
rutJug=[]
fechaNac=[]
annioNac=[]
categoria=[]
celular=[]
correo=[]
parejas=[]

opc1=0
while opc1!=4:
    opc1=fn.menu()
    if opc1==1:
        fn.AgregarDatosJugadores(nombreJug,rutJug,fechaNac,annioNac,categoria,celular,correo,parejas)
    elif opc1==2:
        fn.MostrarParticipante(rutJug,nombreJug,categoria,celular,correo)
    elif opc1==3:
        fn.EncontrarCodigo(parejas,nombreJug)
    else:
        print("Adiós!")