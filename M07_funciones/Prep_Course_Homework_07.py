#!/usr/bin/env python
# coding: utf-8

# ## Funciones

# 1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es

# In[1]:


def esPrimo(num):
    
    cont = 0
    for i in range(1,num+1):
        if num%i == 0:
            cont += 1
    if num == 0 or num == 1:
        return True
    elif cont == 2:
        return True
    else:
        return False
    
print(esPrimo(0))


# 2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista

# In[25]:

def esPrimoL(lista):
    
    listaN = []

    for num in lista:
        cont = 0
        for i in range(1,num+1):
            if num%i == 0:
                cont += 1
        if num == 0 or num == 1:
            listaN.append(num)
        elif cont == 2:
            listaN.append(num)
    
    return listaN
    

listaNum = [1,2,3,4,5,6,7,8,9,10]
nuevalista = esPrimoL(listaNum)
print(nuevalista)


# 3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera

# In[33]:

def repetidos(lista):
    
    #Ordenamos la lista de menor a mayor
    lista.sort()

    #Creamos una lista que nos va a guardar todos los números que tiene la lista original
    num = [lista[1]]

    #Creamos una lista que nos guarda el número de veces que se encuentra ese número en la lista original
    contador = []

    #Me identifica los números que hay dentro de la lista
    for i in range(1,len(lista)):
        if lista[(i-1)] != lista[(i)]: #Cuando hay un cambio de números
            num.append(lista[i])
            cont = lista.count(i)
    
    #Sacamos las veces que se encuentra cada  uno de los números en la lista original
    for i in num:
        cont = lista.count(i)
        contador.append(cont)

    #Sacamos el mayor dentro de la lista de contadores
    mayor = contador[i-1]
    for i in range(1,len(contador)):
        if contador[i-1] < contador[i]:
            mayor = contador[i]

    #Buscamos el indice donde se encuentra ese mayor
    pos = contador.index(mayor)

    #imprimimos el número que está en esa misma posición del mayor de la lista de contador
    numeroMasRep = num[pos]

    return numeroMasRep


listaNumRep = [1,2,3,4,5,3,4,5,6,2,3,4,5,2,3,4,2,3,2,1,1,2,3,5,6,7,8,7,6]
print('El número más repetido de las lista ',listaNumRep, ' es el: ',repetidos(listaNumRep))


# 4) A la función del punto 3, agregar un parámetro más, que permita elegir si se requiere el menor o el mayor de los mas repetidos.

# In[45]:

def repetidosN(lista,respuesta):
    
    #Ordenamos la lista de menor a mayor
    lista.sort()

    #Creamos una lista que nos va a guardar todos los números que tiene la lista original
    num = [lista[1]]

    #Creamos una lista que nos guarda el número de veces que se encuentra ese número en la lista original
    contador = []

    #Me identifica los números que hay dentro de la lista
    for i in range(1,len(lista)):
        if lista[(i-1)] != lista[(i)]: #Cuando hay un cambio de números
            num.append(lista[i])
            cont = lista.count(i)
    
    #Sacamos las veces que se encuentra cada  uno de los números en la lista original
    for i in num:
        cont = lista.count(i)
        contador.append(cont)

    #Sacamos el mayor dentro de la lista de contadores
    mayor = contador[i-1]
    for i in range(1,len(contador)):
        if contador[i-1] < contador[i]:
            mayor = contador[i]

    #Sacamos el menor dentro de la lista de contadores
    menor = contador[i-1]
    for i in range(1,len(contador)):
        if contador[i-1] > contador[i]:
            menor = contador[i]


    #Buscamos el indice donde se encuentra ese mayor
    posMayor = contador.index(mayor)
    #Buscamos el indice donde se encuentra ese menor
    posMenor = contador.index(menor)

    #imprimimos el número que está en esa misma posición del mayor de la lista de contador
    numeroMasRep = num[posMayor]
    #imprimimos el número que está en esa misma posición del menor de la lista de contador
    numeroMenosRep = num[posMenor]

    if respuesta == 'Mayor':
        print('El número más repetido de las lista ',listaNumRep, ' es el: ',numeroMasRep)
    else:
        print('El número menos repetido de las lista ',listaNumRep, ' es el: ',numeroMenosRep)

Incorrecto = True
while Incorrecto:
    print('Requiere escoger el mayor o el menor de la lista? (Responder Mayor o Menor)):')
    resp = input()
    if resp == 'Mayor' or resp == 'Menor':
        Incorrecto = False

repetidosN(listaNumRep,resp)


# 5) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F<br>
# Fórmula 2	: °C + 273.15 = °K<br>
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
# 

# In[56]:

def conversion(temp,unidadIn,unidadOut):

    if unidadIn == 'C' and unidadOut == 'F':
        conver = (temp * 9/5) + 32
    elif unidadIn == 'C' and unidadOut == 'K':
        conver = (temp) + 273.15
    elif unidadIn == 'F' and unidadOut == 'C':
        conver = (temp - 32)*5/9
    elif unidadIn == 'F' and unidadOut == 'K':
        conver = (temp - 32)*5/9 + 273.15
    elif unidadIn == 'K' and unidadOut == 'C':
        conver = (temp) - 273.15
    elif unidadIn == 'K' and unidadOut == 'F':
        conver = (((temp) - 273.15) * 9/5) + 32
    elif unidadIn == unidadOut:
        conver = temp
    
    return conver


Incorrecto = True
while Incorrecto == True:
    print('Por favor ingrese solo el valor numerico de la temperatura')
    temp = float(input())
    if type(temp) == float:
        Incorrecto = False

Incorrecto = True
while Incorrecto == True:
    print('Entrada: Ingrese la palabra F si es en Farenheit, C si es en Cesius o K si es en Kelvin')
    unidadIn = input()
    if unidadIn == "F" or unidadIn == "C" or unidadIn == "K":
        Incorrecto = False

Incorrecto = True
while Incorrecto == True:
    print('Salida: Ingrese la palabra F si es en Farenheit, C si es en Cesius o K si es en Kelvin')
    unidadOut = input()
    if unidadOut == "F" or unidadOut == "C" or unidadOut == "K":
        Incorrecto = False

print(temp,'°',unidadIn,' son: ',conversion(temp,unidadIn,unidadOut),'°',unidadOut)


# 6) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:

# In[62]:

listaTemp = [-5,240,20]
listaTIn = ['F','K','C']
listaTOut = ['C','C','K']

for i in range(len(listaTemp)):
    convers = conversion(listaTemp[i],listaTIn[i],listaTOut[i])
    print(listaTemp[i],'°',listaTIn[i],' son: ',convers,'°',listaTOut[i])



# 7) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo

# In[65]:

def factorial(numero):
    if(type(numero) != int):
        return 'El numero debe ser un entero'
    if(numero < 0):
        return 'El numero debe ser pisitivo'
    if (numero > 1):
        numero = numero * factorial(numero - 1)
    return numero
    
print(factorial(3))
print(factorial(-2))
print(factorial(1.23))
print(factorial('6'))


