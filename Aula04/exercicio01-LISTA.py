numeros=[5, 20, 50, 70]
print("numeros:", numeros)

print(numeros[2])

numeros[3]='100'
print(numeros)

numeros.append('150')
print(numeros)

numeros.insert(1, '25')
print(numeros)

numeros.remove('25')
print(numeros)

del numeros[4]
print(numeros)

numeros.pop(1)
print(numeros)