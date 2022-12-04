#funcion de busqueda
def busca(dni,nu):
    x=-1
    for c in range(len(dni)):
        if(nu==dni[c]):
            x=c
            break
    return x
#carga de los dotos
def carga(dni,sexo,alt,peso,edad):
    i=0
    while True:
        rta=input("desea cargar los datos de un paciente? si/no: ").lower()
        if(rta!='si')and(rta!='no'):
            print("escribir si o no")
        else:
            break
        
    while rta=='si':
        
        while True:
            nu = int(input("ingrese el numero de dni de la persona: "))
            if(nu<0):
                print("los numeros DNI no son menores que cero")
            else:
                break
        xbus = busca(dni,nu)
        
        if(xbus==-1):
            i = i + 1
            dni.append(nu)

            while True:
                sex = input("ingrese el sexo de la persona, M/F: ").lower()
                if(sex!='m')and(sex!='f'):
                    print("el sexo debe ser M/F")
                else:
                    break            
            sexo.append(sex)

            while True:
                altu = float(input("ingrese la altura de la persona: "))
                if(altu<0):
                    print("la altura no puede ser menor a 0")
                else:
                    break    
            alt.append(altu)

            while True:
                pes=float(input("ingrese el peso de la persona: "))
                if(pes<0):
                    print("el peso de una persona no puede ser menor a cero")
                else:
                    break
            peso.append(pes)

            while True:
                ed=int(input("ingrese la edad de la persona: "))
                if(ed<0):
                    print("la edad de una persona no puede ser menor a cero")
                else:
                    break
            edad.append(ed)

            global j
            j=i

            while True:
                rta=input("desea cargar los datos de otra persona? si/no: ").lower()
                if(rta!='si')and(rta!='no'):
                    print("escribir si o no")
                else:
                    break
        else:
            print("el numero de DNI ya esta repetido...")

#muestra de todos los datos
def muestra(dni,sexo,alt,peso,edad,acum):
    print("muestra: ")
    for m in range(0,acum):
        print("Mostrando los datosde la persona")
        print("DNI: "+str(dni[m])+" Sexo: "+sexo[m]+" Altura: "+str(alt[m])+" Peso: "+str(peso[m])+" Edad: "+str(edad[m]))

#consulta segun el dni
def consulta(dni,sexo,alt,peso,edad):
    nu = int(input("Ingrese el numero de DNI para la consulta"))
    for m in range(len(dni)):
        if nu == dni[m]:
            print("DNI: "+str(dni[m])+" Sexo: "+sexo[m]+" Altura: "+str(alt[m])+" Peso: "+str(peso[m])+" Edad: "+str(edad[m]))

#modificacion
def modificacion(dni,sexo,alt,peso,edad):
    op=-1
    while True:
        nu = int(input("Ingrese el numero de dni de la persona para la modificacion: "))
        if(nu<0):
            print("El numero de dni no puede ser menor que cero")
        else:
            break
    xbus = busca(dni,nu)
    
    if(xbus!=-1):
        print("Se encontró a la persona: ")
        print("DNI: "+str(dni[xbus])+" Sexo: "+sexo[xbus]+" Altura: "+str(alt[xbus])+" Peso: "+str(peso[xbus])+" Edad: "+str(edad[xbus]))

        while True:
            rta=input("desea modificar los datos de la persona? si/no: ").lower()
            if(rta!='si')and(rta!='no'):
                print("escribir si o no")
            else:
                break

        if rta == 'si': 
            while op!=6:
                    print("1- Dni")
                    print("2- Sexo")
                    print("3- Altura")
                    print("4- Peso")
                    print("5- Edad")
                    print("6- Salir")
                    op = int(input("Seleccione el dato que quiere modificar: "))
                    match op:
                        case 1: 
                            while True:
                                nu = int(input("Ingrese el nuevo numero de dni: "))
                                if (nu<0):
                                    print("Los numeros de dni no pueden ser menores que cero")
                                else:
                                    break
                            print(str(xbus))
                            xbus1 = busca(dni,nu)
                            print(str(xbus))
                            if(xbus1==-1):
                                dni[xbus] = nu
                            else:
                                print("Este numero de dni ya esta repetido")
                        case 2:
                            while True:
                                sex = input("Ingrese el nuevo sexo de la persona. M/F: ").lower()
                                if(sex!='m')and(sex!='f'):
                                    print("Solo poner M/F")
                                else:
                                    break
                            sexo[xbus] = sex 
                        case 3:
                            while True:
                                altu = float(input("Ingrese la nueva edad de la persona: "))
                                if(altu<0):
                                    print("La altura no puede ser menor que cero")
                                else:
                                    break
                            alt[xbus]=altu
                        case 4:
                            while True:
                                pes = float(input("Ingrese el nuevo peso de la persona: "))
                                if(pes<0):
                                    print("El peso no puede ser menor que cero")
                                else:
                                    break
                            peso[xbus]=pes
                        case 5:
                            while True:
                                ed = int(input("Ingrese la nueva edad de la persona: "))
                                if(ed<0):
                                    print("La edad no puede ser menor que cero")
                                else:
                                    break
                            edad[xbus]=ed
    else:
        print("No se han encontrado datos de la pesona")

#eliminacion de un paciente
def eliminacion(dni,sexo,alt,peso,edad):
    while True:
        nu = int(input("Ingrese el numero de dni que desea eliminar: "))
        if(nu<0):
            print("El numero de dni no puede ser menor que 0")
        else:
            break
    xbus=busca(dni,nu)
    if(xbus!=-1):
        print("Datos de la persona: ")
        print("DNI: "+str(dni[xbus])+" Sexo: "+sexo[xbus]+" Altura: "+str(alt[xbus])+" Peso: "+str(peso[xbus])+" Edad: "+str(edad[xbus]))
        while True:
            rta = input("Desea eliminar los datos de esta persona? si/no").lower()
            if(rta!='si')and(rta!='no'):
                print("Escribir si o no")
            else:
                break
        if(rta=='si'):
            dni.pop(xbus)
            sexo.pop(xbus)
            alt.pop(xbus)
            peso.pop(xbus)
            edad.pop(xbus)

        global acum
        acum = acum - 1
    else:
        print("No se han encontra los datos del paciente")

#Ordenacion por burbuja mejorada
def ordenacion(dni,sexo,alt,peso,edad):
    m=0
    ban=0
    while(m<acum-1)and(ban==0):
        ban=1
        m=m+1
        for x in range(0,(acum-m)):
            if(dni[x]<dni[x+1]):
                aux = dni[x]
                dni[x] = dni[x+1]
                dni[x+1] = aux

                aux = sexo[x]
                sexo[x] = sexo[x+1]
                sexo[x+1] = aux

                aux = alt[x]
                alt[x] = alt[x+1]
                alt[x+1] = aux

                aux = peso[x]
                peso[x] = peso[x+1]
                peso[x+1] = aux

                aux = edad[x]
                edad[x] = edad[x+1]
                edad[x+1] = aux
    
    print("Ordenado por burbuja mejorada")
    for m in range(0,acum):
        print("DNI: "+str(dni[m])+" Sexo: "+sexo[m]+" Altura: "+str(alt[m])+" Peso: "+str(peso[m])+" Edad: "+str(edad[m]))

def cantidad(sexo,edad):
    contM=0
    contm=0
    contF=0
    contf=0
    while True:
        sex = input("Ingrese un sexo para saber la cantidad de personas mayores de edad y menor. M/F: ").lower()
        if(sex!='f')and(sex!='m'):
            print("Solo ingresar m/f")
        else:
            break
    for m in range(0,acum):
        if(sex=='m'):
            if(edad[m]>=18):
                contM=contM+1
            else:
                contm=contm+1
        if(sex=='f'):
            if(edad[m]>=18):
                contF=contF+1
            else:
                contf=contf+1
    if(sex=='m'):
        print("La cantidad de pacientes mayores de edad del sexo Maculino es: "+str(contM)+" y menores: "+str(contm))
    if(sex=='f'):
        print("La cantidad de pacientes mayores de edad del sexo femenino es: "+str(contF)+" y menores: "+str(contf))

def pesoprom(sexo,peso):
    pesM=0; contM=0; pesF=0; contF=0
    while True:
        sex=input("Ingrese un sexo para saber el peso promedio. M/F").lower()
        if(sex!='m')and(sex!='f'):
            print("Solo escribir M/F")
        else:
            break
    for m in range(0,acum):
        if(sexo[m]=='m'):
            contM=contM+1
            pesM=pesM+peso[m]
        if(sexo[m]=='f'):
            contF=contF+1
            pesF=pesF+peso[m]

    if sex=='m':
        promM=pesM/contM
        print("El peso promedio del sexo Masculino es de: "+str(promM))
    else:
        promF=pesF/contF
        print("El peso promedio del sexo femenino es de: "+str(promF))

def rango(dni,sexo,alt,peso,edad):
    print("Ingrese un rango de edad inicial y edad final para mostrar los pacientes de esa edad")
    while True:
        vi = int(input("Edad Inicial: "))
        if(vi<0):
            print("Las edades no pueden ser negativas")
        else:
            break
    while True:
        vf = int(input("Ingrese la edad final: "))
        if(vf<vi):
            print("La edad fianl debe ser mayor o igual que la edad inicial")
        else:
            break
    print("Los pacientes entre a esas edades son: ")
    for m in range(0,acum):
        if(edad[m]>=vi)and(edad[m]<=vf):
            print("DNI: "+str(dni[m])+" Sexo: "+sexo[m]+" Altura: "+str(alt[m])+" Peso: "+str(peso[m])+" Edad: "+str(edad[m]))

def altura(alt,edad):
    acumA = 0; acumP=0
    for m in range(0,acum):
        if(edad[m]>=18):
            acumA = acumA + alt[m]
            acumP = acumP + 1 
    promA = acumA / acumP
    return(promA)

dni = []; sexo = []; alt = []; peso = []; edad = []; acum=0
rta1 = 'si'

while rta1 == 'si':
    print("segun el siguiente menu seleccione")
    print("")
    print("1- Carga")
    print("2- Muestra")
    print("3- Consulta segun el dni")
    print("4- Modificacion de un paciente")
    print("5- Eliminacion de un paciente")
    print("6- Ordenacion por burbuja mejorada")
    print("7- Cantidad de pacientes mayores y menores de edad")
    print("8- Peso promedio de pacientes")
    print("9- Muestra de pacientes segun un rango de edad")
    print("10- Altura promedio de los pacientes mayores de edad")
    print("11- Salir")
    rta = int(input("seleccione: "))

    match rta:
        case 1:
            carga(dni,sexo,alt,peso,edad)
            acum = acum + j
        case 2:
            muestra(dni,sexo,alt,peso,edad,acum)
        case 3: 
            consulta(dni,sexo,alt,peso,edad)
        case 4:
            modificacion(dni,sexo,alt,peso,edad)
        case 5: 
            eliminacion(dni,sexo,alt,peso,edad)
        case 6:
            ordenacion(dni,sexo,alt,peso,edad)
        case 7:
            cantidad(sexo,edad)
        case 8:
            pesoprom(sexo,peso)
        case 9:
            rango(dni,sexo,alt,peso,edad)
        case 10:
            print("La altura promedio de las personas mayores de edad es de: " + str(altura(alt,edad)))