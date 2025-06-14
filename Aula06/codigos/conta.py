class ContaCorrente:
    def __init__(self, nome_cliente, num_conta, senha, saldo=0.0):
        self.nome_cliente = nome_cliente
        self.num_conta = num_conta
        #self.agencia = agencia
        self.senha = senha
        #self.cartao_credito = cartao_credito
        #self.finaciamento = financiamento
        self.saldo = saldo
        #self.cheque_especial = cheque_especial

    def mostrar_saldo(self):
        print(f'O saldo de {self.nome_cliente} disponivel é {self.saldo:.2f}')

    def sacar(self, valor):
        if valor in self.saldo:
            conta = self.saldo[valor]
            if self.saldo >= valor:
                self.saldo(valor)
                print(f"Saque de R${valor:.2f} realizado na conta")
            else:
                print(f"Saldo insuficiente na conta")
        
    def depositar(self, valor):
        if 0<valor <= self.saldo:
            self.saldo -= valor
            print(f'O saldo de {self.nome_cliente} disponivel é {self.saldo:.2f}')

    def transferir(sef, valor, destinatario):
        if self!= destinatario.num_conta:
            ContaCorrente.sacar(self, valor)
            ContaCorrente.depositar(destinatario, valor)
        else:
            print("não pode realizar a transferência")




