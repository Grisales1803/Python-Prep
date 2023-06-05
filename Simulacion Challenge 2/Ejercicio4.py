
# Devuelve True si el numero es simetrico
# Número simetrico: Es igual a su reverso

def numeroSimetrico(num):

    #Sacamos el número de cifras
    longitud = 0
    num1 = num
    while True:
        num1 = num1/10
        longitud += 1
        if num1 < 1:
            break
    
    longi = longitud

    valor = True
    for i in range(1,(longitud//2)+1):
        #Sacamos el primer número
        primerNum = num // (10**(longi-1))
        #Sacamos el ultimo número
        ultimoNum = num % (10)
        #Sacamos el nuevo numero sin los extremos
        num = (num - primerNum * (10**(longi-1)))//10
        longi = longi - 2
        if primerNum != ultimoNum:
            valor = False
            return valor
            break
    
    return valor

numero = 217112
print(numeroSimetrico(numero))