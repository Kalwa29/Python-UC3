

inicio=int(input("informe o seu primeiro número :"))    
fim=int(input("informe o seu segundo número :"))
def somar_intervalo(inicio, fim):
    print(sum(range(inicio, fim+1)))

somar_intervalo(inicio, fim+1)