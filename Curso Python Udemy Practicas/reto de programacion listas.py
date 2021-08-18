listaProductos = []
print("BIENVENIDO A SU LISTA DE MERCADO\n(SOLO PUEDES INGRESAR 7 PRODUCTOS A LA LISTA)")

for i in range(8):
    producto = input("Ingrese el nombre del producto: ")
    
    listaProductos.append(producto)


listaProductos.sort()



print("TU LISTA")
print("*********************")

print(listaProductos[0])
print(listaProductos[1]) 
print(listaProductos[2])
print(listaProductos[3])
print(listaProductos[4])
print(listaProductos[5])
print(listaProductos[6])

print("**********************")

print ("Gracias compañeritos por poner atencion y que la fuerza los acompañe")
