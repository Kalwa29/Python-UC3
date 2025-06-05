def quadradado_asteristicos(tamanho):
    for i in range (tamanho):
        print("*"*tamanho)



tamanho=int(input("digite um quantidade :"))
def parte_dois(tamanho):
    meio = tamanho // 2
    for i in range (tamanho):
        linha=""

        for j in range (tamanho):
            if i == meio and j == meio:
                linha+=" "
            
            else:
                linha="*"


        print(linha)

parte_dois(tamanho)


def parte_tres(tamanho):
    altura=tamanho//2
    for i in range(altura+1):
        espacos=" " * (altura -i)
        asteristicos= "*" * (2*i+1)
        print(espacos+asteristicos+espacos)
parte_tres(tamanho)