menu = ['1. lista, 2. estudar, 3. xadrez, 4. sair']
def contador_menu():
    contador = 0
    while True:
        print(menu)
        opcao=int(input("escolha uma opção :"))
        if opcao == 4:
            break
        else:
            contador +=1
