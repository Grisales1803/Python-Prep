#!/usr/bin/env python
# coding: utf-8

# ## Clases y Programación Orientada a Objetos

# 1) Crear la clase vehículo que contenga los atributos:<br>
# Color<br>
# Si es moto, auto, camioneta ó camión<br>
# Cilindrada del motor

# In[1]:

class Vehiculo:

    def __init__(self,color,tipo,cilindraje):
        self.color = color
        self.tipo = tipo
        self.cilindraje = cilindraje
    
# 2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
# Acelerar<br>
# Frenar<br>
# Doblar<br>

# In[5]:

class Vehiculo:

    def __init__(self,color,tipo,cilindraje):
        self.color = color
        self.tipo = tipo
        self.cilindraje = cilindraje
        self.velocidad = 0
        self.grados = 0

    def acelerar(self, vel):
        self.velocidad += vel
        return print('Acelera el ', self.tipo, 'de color', self.color,'a una velocidad de ', self.velocidad, 'km/h')

    def frenar(self):
        return print('Frena el ', self.tipo, 'de color', self.color)

    def doblar(self,grados):
        self.grados += grados
        return print('Dobla el ', self.tipo, 'de color', self.color, self.grados,' grados')


    # 3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado

    # In[6]:

objeto1 = Vehiculo('Rojo','Auto',1.4)
objeto2 = Vehiculo('Negro', 'Moto', 1)
objeto3 = Vehiculo('Azul', 'Camioneta', 3)

objeto1.acelerar(5)
objeto2.frenar()
objeto3.doblar(90)

# 4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada

# In[12]:

class Vehiculo:

    def __init__(self,color,tipo,cilindraje):
        self.color = color
        self.tipo = tipo
        self.cilindraje = cilindraje
        self.velocidad = 0
        self.grados = 0

    def acelerar(self, vel):
        self.velocidad += vel
        return print('Acelera el ', self.tipo, 'de color', self.color,'a una velocidad de ', self.velocidad, 'km/h')

    def frenar(self,vel):
        self.velocidad -= vel
        return print('Frena el ', self.tipo, 'de color', self.color,'a una velocidad de ', self.velocidad, 'km/h')

    def doblar(self,grados):
        self.grados += grados
        return print('Dobla el ', self.tipo, 'de color', self.color, self.grados,' grados')
    
    def estado(self,vel,grados):
        self.velocidad += vel
        self.grados += grados
        return print('El vehiculo está andando a ',  self.velocidad, 'km/h y  a una dirección de ', self.grados, 'grados' )

    def presentarse(self):
        return print(self.tipo, 'de color', self.color, ' y un cilindraje de ', self.cilindraje)


# In[13]:

objeto1 = Vehiculo('Rojo','Auto',1.4)
objeto2 = Vehiculo('Negro', 'Moto', 1)
objeto3 = Vehiculo('Azul', 'Camioneta', 3)

objeto1.acelerar(5)
objeto1.doblar(90)
objeto2.doblar(90)
objeto1.estado(8, 30)
objeto2.presentarse()


# 5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 7<br>
# Verificar Primo<br>
# Valor modal<br>
# Conversión grados<br>
# Factorial<br>

# In[33]:

class Herramientas:

    def __init__(self):
        pass

    def esPrimoL(self,lista):
    
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
    
    def repetidos(self,lista):
    
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
    
    def conversion(self, temp,unidadIn,unidadOut):

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
    
    def factorial(self, numero):
        if(type(numero) != int):
            return 'El numero debe ser un entero'
        if(numero < 0):
            return 'El numero debe ser pisitivo'
        if (numero > 1):
            numero = numero * self.factorial(numero - 1)
        return numero




# 6) Probar las funciones incorporadas en la clase del punto 5

# In[28]:

#Para esPrimo
listaNum = [1,2,3,4,5,3,4,5,6,2,3,4,5,2,3,4,2,3,2,1,1,2,3,5,6,7,8,7,6,9,5,9,10,10,4,3,5,9]
Lista1 = Herramientas() 
print(Lista1.esPrimoL(listaNum))

#Para repetidos
repeticion = Lista1.repetidos(listaNum)
print('El número más repetido de las lista es el: ',repeticion)

#Para coversion
convTemp = Herramientas()
temp = 8
unidadIn = 'C'
unidadOut = 'F'
conv = convTemp.conversion(temp, unidadIn, unidadOut)
print(temp,'°',unidadIn,' son: ',conv,'°',unidadOut)

#Para factorial
fact = Herramientas()
print(fact.factorial(3))
print(fact.factorial(-2))
print(fact.factorial(1.23))
print(fact.factorial('6'))



# 7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las funciones incorporadas

# In[55]:

class Herramientas2:

    def __init__(self,lista):
        self.lista = lista

    def esPrimoL(self):
    
        listaN = []

        for num in self.lista:
            cont = 0
            for i in range(1,num+1):
                if num%i == 0:
                    cont += 1
            if num == 0 or num == 1:
                listaN.append(num)
            elif cont == 2:
                listaN.append(num)
        
        return listaN
    
    def repetidos(self):
    
        #Ordenamos la lista de menor a mayor
        self.lista.sort()

        #Creamos una lista que nos va a guardar todos los números que tiene la lista original
        num = [self.lista[1]]

        #Creamos una lista que nos guarda el número de veces que se encuentra ese número en la lista original
        contador = []

        #Me identifica los números que hay dentro de la lista
        for i in range(1,len(self.lista)):
            if self.lista[(i-1)] != self.lista[(i)]: #Cuando hay un cambio de números
                num.append(self.lista[i])
                cont = self.lista.count(i)
        
        #Sacamos las veces que se encuentra cada  uno de los números en la lista original
        for i in num:
            cont = self.lista.count(i)
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
    
    def conversion(self, temp,unidadIn,unidadOut):

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
    
    def factorial(self, numero):
        if(type(numero) != int):
            return 'El numero debe ser un entero'
        if(numero < 0):
            return 'El numero debe ser pisitivo'
        if (numero > 1):
            numero = numero * self.factorial(numero - 1)
        return numero

#Para esPrimo
listaNum = [1,2,3,4,5,3,4,5,6,2,3,4,5,2,3,4,2,3,2,1,1,2,3,5,6,7,8,7,6,9,5,9,10,10,4,3,5,9]
Lista1 = Herramientas2(listaNum) 
print(Lista1.esPrimoL())

#Para repetidos
repeticion = Lista1.repetidos()
print('El número más repetido de las lista es el: ',repeticion)

#Para coversion
convTemp = Herramientas2(listaNum)
temp = 8
unidadIn = 'C'
unidadOut = 'F'
conv = convTemp.conversion(temp, unidadIn, unidadOut)
print(temp,'°',unidadIn,' son: ',conv,'°',unidadOut)

#Para factorial
fact = Herramientas2(listaNum)
print(fact.factorial(3))
print(fact.factorial(-2))
print(fact.factorial(1.23))
print(fact.factorial('6'))



# 8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones

# In[1]:

import prueba

print('La suma es:')
print(prueba.suma(2,4))

listaNum = [1,2,3,4,5,3,4,5,6,2,3,4,5,2,3,4,2,3,2,1,1,2,3,5,6,7,8,7,6,9,5,9,10,10,4,3,5,9]
Lista1 = prueba.Herramientas3(listaNum)
print(Lista1.esPrimoL())



