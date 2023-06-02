#!/usr/bin/env python
# coding: utf-8

# ## Manejo de errores

# 1) Con la clase creada en el módulo 7, tener en cuenta diferentes casos en que el código pudiera arrojar error. Por ejemplo, en la creación del objeto recibimos una lista de números enteros pero ¿qué pasa si se envía otro tipo de dato?

# In[1]:


def factorial(num):
    
    # Uso de Assert para verificar que todo esté en orden:
    '''
    assert type(num) != str, f'{num} no puede ser str'
    assert type(num) != float, f'{num} tiene que ser entero'
    assert num > 0, f'{num} tiene que ser mayor a cero'
    '''

    if type(num) == str:
        raise ValueError(f'{num} no puede ser str')  
    elif type(num) == float:
        raise ValueError(f'{num} tiene que ser entero')
    elif num < 1:
        raise ValueError(f'{num} tiene que ser un entero positivo')  
    else:
        fact = 1
        for i in range(1,num+1):
            fact = fact * i
        
        return fact

print(factorial(3))
print(factorial(-2))
print(factorial(1.23))
print(factorial('6'))

    

# 2) En la función que hace la conversión de grados, validar que los parámetros enviados sean los esperados, de no serlo, informar cuáles son los valores esperados.

# In[5]:






# 3) Importar el modulo "unittest" y crear los siguientes casos de pruebas sobre la clase utilizada en el punto 2<br>
# Creacion del objeto incorrecta<br>
# Creacion correcta del objeto<br>
# Metodo valor_modal()<br>
# 
# Se puede usar "raise ValueError()" en la creación de la clase para verificar el error. Investigar sobre esta funcionalidad.

# In[9]:




# 4) Probar una creación incorrecta y visualizar la salida del "raise"

# In[13]:




# 6) Agregar casos de pruebas para el método verifica_primos() realizando el cambio en la clase, para que devuelva una lista de True o False en función de que el elemento en la posisicón sea o no primo

# In[14]:




# 7) Agregar casos de pruebas para el método conversion_grados()

# In[17]:




# 8) Agregar casos de pruebas para el método factorial()

# In[20]:




