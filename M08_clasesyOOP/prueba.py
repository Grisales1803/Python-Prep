
def suma(n1,n2):
    return n1+n2

class Herramientas3:

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

listaNum = [1,2,3,4,5,3,4,5,6,2,3,4,5,2,3,4,2,3,2,1,1,2,3,5,6,7,8,7,6,9,5,9,10,10,4,3,5,9]
Lista1 = Herramientas3(listaNum)
print(Lista1.esPrimoL())

print(suma(1,2))