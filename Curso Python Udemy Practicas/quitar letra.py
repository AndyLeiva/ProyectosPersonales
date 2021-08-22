palabra = "Mi mama me mima"
print(palabra)
letter = input("Cual letra quieres quitar del texto?: ")

p = palabra.lower()
l= letter.lower()

for c in p:
    if c == l:
        continue
    else:
        print(c, end="")