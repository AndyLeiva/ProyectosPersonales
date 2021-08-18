fiboActual = 1
fiboAnterior = 1
indice = 3

while indice <=20:
    temp = fiboActual
    fiboActual = fiboActual + fiboAnterior
    fiboAnterior = temp
    
    print(f"La posicion de {fiboActual} es la numero {indice}")
    
    indice +=1