
#def criar_arquivo(nome_arquivo: str, conteudo: str):
#    """Cria um arquivo com o nome e conteúdo fornecidos."""
"""
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(conteudo)
        print('Arquivo criado com sucesso!!!')

nome=input('Digite o nome do arquivo: ')
criar_arquivo(f'./Python-UC3/Aula05/arquivos/{nome}.txt', 'Este é um exemplo de aquivo criado com python')
"""



# Ler o arquivo
#def Ler_arquivo(nome_arquivo: str):
#    """Ler um arquivo com o nome e conteúdo fornecidos."""
"""
    with open(nome_arquivo, 'r') as arquivo:
        return arquivo.read()
        
nome=input('Digite o nome do arquivo: ')
print(Ler_arquivo(f'./Python-UC3/Aula05/arquivos/{nome}.txt'))
"""


# Adicionar conteudo
#def adicionar_arquivo(nome_arquivo: str, conteudo: str):
#    """Adicionar um arquivo com o nome e conteúdo fornecidos."""
"""
    with open(nome_arquivo, 'a') as arquivo:
        arquivo.write('\n' + conteudo)
        print('Arquivo adicionado com sucesso!!!')

nome=input('Digite o nome do arquivo: ')
conteudo=input("Digite a informação: ")
adicionar_arquivo(f'./Python-UC3/Aula05/arquivos/{nome}.txt', conteudo)
"""

# Remover arquivo
#import os
#def remover_arquivo(nome_arquivo: str):
#    """remover um arquivo com o nome e conteúdo fornecidos."""
"""
    if os.path.exists(nome_arquivo):
        os.remove(nome_arquivo)
        print('Arquivo removido com sucesso!!!')

    else:
        print("Este arquivo não existe!!!")

nome=input('Digite o nome do arquivo: ')
remover_arquivo(f'./Python-UC3/Aula05/arquivos/{nome}.txt')
"""

# contar linha
#def contar_linhas(nome_arquivo: str) -> int:
#    """Cria um arquivo com o nome e conteúdo fornecidos."""
#
#    with open(nome_arquivo, 'r') as arquivo:
#        return len(arquivo.readlines()) 
#        
#nome=input('Digite o nome do arquivo: ')
#print(contar_linhas(f'./Python-UC3/Aula05/arquivos/{nome}.txt'))

# verificar se a palavra existe
#def verificar_palavra(nome_arquivo: str, palavra: str) -> bool:
#    """Verificando uma palavra no arquivo."""
#
#    with open(nome_arquivo, 'r') as arquivo:
#        return palavra in arquivo.read()
#
#
#
#nome=input('Digite o nome do arquivo: ')
#print(verificar_palavra(f'./Python-UC3/Aula05/arquivos/{nome}.txt', 'python'))

# 3 linhas
#def somar_numeros(nome_arquivo: str) -> int:
#    """Adicionar um arquivo com o nome e conteúdo fornecidos."""
#
#    with open(nome_arquivo, 'r') as arquivo:
#        return sum(int(linha.strip()) for linha in arquivo)
#    
#
#nome=input('Digite o nome do arquivo: ')
#somar_numeros(f'./Python-UC3/Aula05/arquivos/{nome}.txt')


# atualizar
def atualizar_linha(nome_arquivo: str, novo_conteudo: str, linha_alvo: int):
    """Adicionar um arquivo com o nome e conteúdo fornecidos."""


    with open(nome_arquivo, 'r') as arquivo:
        linhas=arquivo .readlines()

        if 0<= linha_alvo < len(linhas):
            linhas[linha_alvo] = novo_conteudo + '\n'


    with open(nome_arquivo, 'w') as arquivo2:
        arquivo2.writelines(linhas)



    

nome=input('Digite o nome do arquivo: ')
conteudo=input("Digite o conteudo do arquivo: ")
linha=int(input("informe o numero da linha do arquivo: "))
atualizar_linha(f'./Python-UC3/Aula05/arquivos/{nome}.txt')
