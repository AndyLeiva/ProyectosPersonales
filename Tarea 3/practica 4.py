nombre = input("Ingrese su nombre completo: ")
edad = int(input("Ingrese su edad: "))
hobby = input("Cual es tu hobby: ")
sueno = input("¿Tienes sueño?(Si/No): ")

n = nombre.istitle()
e = (edad >= 16) and (edad <= 40)
h = len(hobby) >= 10
s = sueno.isalnum()

if n and e and h and s == True:
    print("Puedes tener la entrevista con Pyratilla!")
else:
    print("No puedes tener la entrevista, lo siento")