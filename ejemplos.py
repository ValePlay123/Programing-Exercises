#busqueda de un numero en un vector
n = int(input("ingrese la cantidad"))
lista = []
for i in range(n):
    num = int(input("ingrese un numero {}:".format(i+1)))
    lista.append(num)
print(lista)

n = int(input("ingrese el numero que quiere encontrar"))
for j in range(len(lista)):
    if(n==lista[j]):
        print("El numero "+str(n)+" se ha encontrado en la prosicion"+str(j))

#carga de vectores mejorado
nombres=[]
identificaciones = []

tamaño = 3

for i in range(tamaño):
    print("ingrese los datos de la persona", i + 1)
    nombre  = input("nombre: ")
    identificacion = input("indentificacion: ")

    nombres.append(nombre)
    identificaciones.append(identificacion)
for i in range(tamaño):
    print("mostrando los datos de la persona", i+1)

    print("nombre", nombres[i])
    print("identificaciones: ", identificaciones[i])

#carga de un diccionario
personas = {}
num = int(input("cuantas personas desea agregar"))
for i in range(0,num):
    id = int(input("ingrese el id: "))
    nombre = input("ingrese el nombre: ")
    edad = int(input("ingrese la edad: "))

    personas[id]=nombre,edad
#muestra de un diccionario
print(personas)

#diccionarios
def dic():
    datos = {
        'nombre':'valentin',
        'edad':19,
        'genero':'masculino'
    }
    #como mostrar un diccionario con for
    for i,j in datos.items():
        print(f'su {i} es {j}')

    diccionario = {
        'int':7,
        'str':'hola',
        'bool': True,
        'float':3.5
    }
    dic1={ #diccionario con indices que yo quiera
        10:7,
        20:(1,2,3),
        30:['control','educacion']
    }

    tienda = {
        'item': ['lapiz','carpeta','marcador'],
        'cantidad':[3,10,5],
        'valor':[3.50,4.25,7.85]
    }

    print(diccionario)
    print(diccionario['bool'])#para llamar un valor especifico del dic
    print(dic1)
    print(dic1[30][0])#primero el indice segundo la posicion del valor
    print(tienda)
    print(tienda['item'][0])

    del tienda['valor'][1]#para borrar algun dato o valor
    print(tienda)

    print(tienda.values())#nos imprime solo los valores 
    print(tienda.keys())#solo nos imprime los items
    print(tienda.items())#nos genera en pares
dic()


#carga de un vector
print("carga de un vector")
num = int(input("cuantos numero desea que tenga su vector"))

vec = []

for i in range(0,num):
    print("ingrese el elemto del indice",i)
    elemento = input()
    vec.insert(i,elemento)

#muestra del vector
print(vec)

#funciones y procedimientos
def suma():
    edad3 = int(input("seleccione una tercera edad "))
    print("la tercera edad es: "+str(edad3))

    edad4 = int(input("ingrese la edad cuatro para sumarla con la tres"))
    print("la cuarta edad es: "+str(edad4))
    
    sum = edad3 + edad4
    print("la suma de la edad 3 y 4 es de: "+str(sum))

def resta(edad,edad2):
    edadT=edad-edad2
    return edadT

edad = int(input("ingrese su edad: "))
print("la edad ingresada es: "+str(edad))

edad2 = int(input("ahora ingrese una segunda edad"))
print("la segunda edad es: "+str(edad2))

print("la resta de ambas edad es de: "+str(resta(edad,edad2)))

suma()

