#función buscar amigo
'Recibe como argumento un arrray llamado amigos que contiene en cada posición del arreglo un objeto que tiene'
'como propiedades nombre y edad. También recibe un string llamado nombre. Debe devolver el objeto cuya propiedad'
'nombre coincida con el string nombre recibido por argumento'
'Ej:'
'var amigos = [{nombre: Tony, edad: 33},{nombre: Emi, edad: 25}]'


def buscaramigo(nombreR):
    
    class Amigo:

        def __init__(self,nombre,edad):
            self.nombre = nombre
            self.edad = edad

    amigos = []
    amigos.append(Amigo('Tony',33))
    amigos.append(Amigo('Emi',25)) 
    amigos.append(Amigo('Camilo',18)) 
    amigos.append(Amigo('Gonzalo',23)) 
    amigos.append(Amigo('Roberto',45)) 
    amigos.append(Amigo('Samuel',27)) 

    for i in amigos:
        if i.nombre == nombreR:
            return [i.nombre, i.edad]
            

print(buscaramigo('Camilo'))