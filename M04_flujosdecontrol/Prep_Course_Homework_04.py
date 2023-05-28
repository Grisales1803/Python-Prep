#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:

print("Por favor ingrese un número:")
x = int(input())

if x > 0:
    print("El numero es mayor a 0")
else:
    print("El numero es menor a 0")



# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:

var1 = 2
var2 = '2'

if type(var1) == type(var2):
    print("Las variables son del mismo tipo")
else:
     print("Las variables no del mismo tipo")


# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:

for i in range(1,21):
    if i % 2 == 0:
        print("El número ", i, " es par")
    else:
        print("El número ", i, " es impar")



# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:

for i in range(0,6):
    print(i,'^3 = ', i**3)


# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:

x = 4

for i in range(1,x+1):
    print('ciclo ',i)


# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:

while True:
    print('Por favor ingrese un número mayor a cero para sacar factorial:')
    x = int(input())
    if x > 0:
        break

print(x,'! = ', end='')
fact = x
while x > 1:
    fact = fact * (x-1)
    x = x - 1

print(fact)


# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:

while True:
    for i in range(1,6):
        print('ciclo ', i)
    break


# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:




# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:

cont = 0
print('Los números primos son:')
print(1)
for i in range(1,31):
    for j in range(1,i+1):
        if i%j == 0:
            cont = cont + 1
    if cont == 2:
        print(i)
    cont = 0


# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:





# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:




# In[57]:




# 12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?

# In[58]:





# In[59]:




# 13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:

i = 99
print('Los números divisibles por 12 entre 100 y 300 son:')
while i < 301:
    i = i+1 
    if i%12 != 0:
        continue
    print(i)
    

# 14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:

continuar = True
while continuar == True:
    print('Ingrese el número para revisar si es primo')
    x = int(input())
    cont = 0
    for j in range(1,x+1):
        if x%j == 0:
            cont = cont + 1
    if cont == 2:
        print('El número es primo')
    else:
        print('El número NO es primo')
    print('Desea encontrar otro número primo? SI/NO')
    Validar = True
    while Validar == True:
        resp = input()
        if resp != "SI" and resp != "NO":
            print('Por favor ingrese SI o NO')
        else:
            Validar = False
            if resp == 'SI':
                continuar = True
            else:
                continuar = False
            

# 15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:

Encontro = True
while Encontro == True:
    for i in range(100,301):
        if i%3 == 0 and i%6==0:   
            print('dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6 es:', i)
            break
    Encontro = False

