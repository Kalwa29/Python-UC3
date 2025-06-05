def he_palindrimo(texto):
    texto = texto.replace("","").lower()
    return texto==texto [::-1]

frase=input("Digíte para saber se é Palindromo :")

if he_palindrimo(frase):
    print("É Palindromo")

else:
    print("Não é palindromo")