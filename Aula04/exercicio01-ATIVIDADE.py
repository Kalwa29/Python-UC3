import random

frutas = ["maçã", "banana", "uva", "abacaxi", "pêra"]

lista_frutas=[]
conjunto_frutas=set()
tupla_frutas=()
dicionario_frutas={}

for frutas in frutas:
    lista_frutas.append(frutas)
    conjunto_frutas.add(frutas)
    tupla_frutas=tuple(frutas)

for i, fruta in enumerate(frutas):
    dicionario_frutas[i]=fruta

print("lista :", lista_frutas)
print("set :", conjunto_frutas)
print("tupla :", tupla_frutas)
print("dicionario :", dicionario_frutas)

print("\n Lista de frutas :")

lista_aleatoria=[]
for _ in range(5):
    fruta_sorteada=random.sample(frutas, k=5)
    

print("lista aleatoria", lista_aleatoria)