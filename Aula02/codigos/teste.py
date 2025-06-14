class Conta:
    def __init__(self, numero, titular, saldo=0.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor

    def exibir_dados(self):
        print(f"Número: {self.numero}")
        print(f"Titular: {self.titular}")
        print(f"Saldo: {self.saldo}")

        # Criando duas contas
conta1 = Conta(12345, "Ana Costa", 1500.0)
conta2 = Conta(67890, "Carlos Oliveira")

# Exibindo os dados das contas
print("=== Conta 1 ===")
conta1.exibir_dados()

print("\n=== Conta 2 ===")
conta2.exibir_dados()