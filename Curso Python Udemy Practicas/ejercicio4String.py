s = "Mi pasión por el chocolate es superior a mis fuerzas"
print(s)
searchWord = str(input("Introduce la palabra a encontrar del texto anterior: "))

word = s.find(searchWord)
final = word + len(searchWord)
subString = s[word:(final + 1)]

print(subString)
