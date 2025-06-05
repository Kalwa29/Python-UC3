
inicio=int(input("informe o seu primeiro número :"))    
limite=int(input("informe o seu valor final :"))

def imprimir_numero(inicio, limite):
    for numero in range(inicio, limite + 1):
        print(f"{numero}")

imprimir_numero(inicio, limite)