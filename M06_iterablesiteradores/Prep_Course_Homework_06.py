#!/usr/bin/env python
# coding: utf-8

# ## Iteradores e iterables

# 1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1

# In[1]:

lista = []

numero = -15
while numero <= -1:
    lista.append(numero)
    numero += 1 

print(lista)

# 2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?

# In[3]:

i = 0
while i < len(lista):
    if lista[i]%2 == 0:
        print(lista[i])
    i += 1


# 3) Resolver el punto anterior sin utilizar un ciclo while

# In[4]:

for i in lista:
    if (i % 2 == 0):
        print(i)


# 4) Utilizar el iterable para recorrer sólo los primeros 3 elementos

# In[7]:

for elemento in lista[:3]:
    print(elemento)

# 5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento

# In[9]:

for i in enumerate(lista):
    print(i)


# 6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]

# In[10]:

lista = [1,2,5,7,8,10,13,14,15,17,20]

for i in range(1,21):
    if i != lista[i+1]:
        lista.insert(i-1,i)

print(lista)


# In[11]:


n = 1



# 7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
# n(0) = 0
# n(1) = 1
# n(i) = n(i-1) + n(i-2)
# Crear una lista con los primeros treinta números de la sucesión.<br>

# In[23]:

fibo = [0,1]

for i in range(2,30):
    fibo.append(fibo[i-1]+fibo[i-2])

print(fibo)



# 8) Realizar la suma de todos elementos de la lista del punto anterior

# In[24]:

print(sum(fibo))


# 9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
# Donde i es la cantidad total de elementos<br>
# n(i-1) / n(i)
# n(i-2)/ n(i-1)
# n(i-3) / n(i-2)
# n(i-4) / n(i-3)
# n(i-5) / n(i-4)
#  

# In[38]:

aurea = []
for i in range(25,30):
    aurea.append(fibo[i]/fibo[i-1])

print(aurea)

# 10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>
# cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

# In[39]:

cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

posiciones = []
pos = 0
for i in cadena:
    if i == 'n':
        posiciones.append(pos)
    pos += 1

print('Las posiciones en las que aparecen la letra n son:')
print(posiciones)

for i, c in enumerate(cadena):  # Itera sobre la cadena y obtiene el índice y el carácter en cada iteración
    if c == 'n':  # Verifica si el carácter es igual a 'n'
        print(i)  # Imprime el índice correspondiente al carácter 'n'

# 11) Crear un diccionario e imprimir sus claves utilizando un iterador

# In[40]:

dicc = {'Clave 1':1,
        'Clave 2':2,
        'Clave 3':3}

for i in dicc:
    print(i)


# 12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 

# In[41]:

listaC = list(cadena)

recorre = iter(listaC)  # Crea un iterador a partir de la cadena
largo = len(listaC)  # Obtiene la longitud de la cadena
for i in range(0, largo):  # Itera sobre el rango de índices desde 0 hasta largo-1
    print(next(recorre))  # Imprime el próximo elemento del iterador


# In[45]:





# 13) Crear dos listas y unirlas en una tupla utilizando la función zip

# In[48]:

Lista1 = [1,2,3,4,5]
Lista2 = ['a','b','c']

combinacion = zip(Lista1, Lista2)
combinacionN = list(combinacion)

print(combinacionN)


# 14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
# lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

# In[49]:

lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

lisN = []
for i in lis:
    if i%7 == 0:
        lisN.append(i)

print(lisN)

#Se usa para crear una lista nueva a partir de otra considerando una condición
lisNA = [i for i in lis if i%7 == 0]

print(lisNA)


# 15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
# lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

# In[56]:

lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

cont = 0
for i in lis:
    if type(i)==list:
        cont += len(i)
    else:
        cont += 1

print('La cantidad total de elemento de la lista es: ',cont)


# In[51]:





# In[57]:





# 16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es

# In[58]:

listaNueva = []
for x in lis:
    if type(x) != list:
        listaNueva.append([x])
    else:
        listaNueva.append(x)

print(listaNueva)

#Con enumerate solo cambio las posiciones dentro de la misma lista, no tengo que crear una nueva
for i,c in enumerate(lis):
    if type(c) != list:
        lis[i] = [c]

print(lis)


