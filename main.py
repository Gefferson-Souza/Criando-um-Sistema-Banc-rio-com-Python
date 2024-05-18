from typing import List

class Banco:
    def __init__(self):
        self.saldo: float = 0.0
        self.saques_diarios: int = 0
        self.transacoes: List[str] = []

    def depositar(self, valor: float) -> None:
        self.saldo += valor
        self.transacoes.append(f'Depósito: +{valor}R$')

    def sacar(self, valor: float) -> None:
        if (valor > self.saldo):
            print('Saldo insuficiente')
        elif(self.saques_diarios > 3):
            print('Você só pode fazer 3 saques por dia.')
        elif(valor > 500):
            print('O valor máximo para saque é de 500R$')
        if (self.saques_diarios < 3 and valor <= 500 and valor <= self.saldo):
            self.saldo -= valor
            self.saques_diarios += 1
            self.transacoes.append(f'Saque: -{valor}R$')

        else:
            print('Não foi possível realizar o saque. ')

    def extrato(self) -> None:
        print('Extrato:')
        for transacao in self.transacoes:
            print(transacao)
        print(f'Saldo atual: {self.saldo}R$')


banco: Banco = Banco()
opcao: int = 0
while opcao != 4:
    print('====================================================================================================')
    print(f'Saldo atual: {banco.saldo}R$')
    print('1 - Depositar\n2 - Sacar\n3 - Extrato\n4 - Sair')
    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        valor: float = float(input('Digite o valor a ser depositado: '))
        banco.depositar(valor)
    elif opcao == 2:
        valor: float = float(input('Digite o valor a ser sacado: '))
        banco.sacar(valor)
    elif opcao == 3:
        banco.extrato()
    elif opcao == 4:
        break
    else:
        print('Opção inválida')