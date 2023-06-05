
'''
La función llamada 'pluck' recibe como argumento un arreglo de objetos llamado Array y el nombre de una propiedad
La función debe devolver un nuevo arreglo con solo los valores dentro de la propiedad recibida.
Ej:
varproductos = [{name: 'TV LCD', price: 100},{name: Computadora, price: 500}]
productos.pluck(productos,'name') debera devolver ['TV LCD','Computadora]
'''

def pluck(array,nombreObj):
    class Objeto:

        def __init__(self,nombre,precio):
            self.nombre = nombre
            self.precio = precio
    
    nombresObj = []
    precios = []
    listaObjetos = []

    for i,c in array.items():
        nombresObj.append(i)
        precios.append(c)
    
    for i in range(len(nombresObj)):
        objetoEnlista = Objeto(nombresObj[i],precios[i])
        listaObjetos.append(objetoEnlista)
    
    for i in listaObjetos:
        if i.nombre == nombreObj:
            return [i.nombre,i.precio]


dicc = {'TV LCD' : 100,'Computadora' : 100, 'Mouse':40, 'Keyboard': 50}
print(pluck(dicc,'Computadora' ))
