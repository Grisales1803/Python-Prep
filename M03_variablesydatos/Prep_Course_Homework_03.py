#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:

x = 7
print(x)

# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:


print(type(8.5))



# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:


print(type(x))


# 4) Crear una variable que contenga tu nombre

# In[2]:

nombre = "Juan"


# 5) Crear una variable que contenga un número complejo

# In[3]:

complejo = 5+6j


# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:

print(type(complejo))



# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


pi = 3.1416


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:

valorA = "True"
valorB = True


# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:

print(type(valorA))
print(type(valorB))




# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:

suma = 8 + 8.5



# 11) Realizar una operación de suma de números complejos

# In[2]:

i = 6+6j
j= 7+4j

sumaComplex = i+j


# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:

SumaRealyComplex = 5 + 5j


# 13) Realizar una operación de multiplicación

# In[5]:

print(5*5)



# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:

print(2**3)


# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:

Cociente = 27/4
print(Cociente)


# 16) De la división anterior solamente mostrar la parte entera

# In[9]:

Entero = 27//4
print(Entero)



# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:

Residuo = 27%4
print(Residuo)


# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:

print(Entero*4+Residuo)



# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:

print("Hola" + " Mundo")



# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:


print(bool("2" == 2))


# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:

print(bool(int("2") == 2))



# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:


a = float('3.8')
print(a)

# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido

# In[15]:

variable = 3
variable -= 3
print(variable)


# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:

print(1 << 2)



# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:






# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:



