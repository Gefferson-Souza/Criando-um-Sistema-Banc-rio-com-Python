from typing import List, Type

class Banco:
    MAX_SAQUES_DIARIOS:int = 3
    VALOR_MAXIMO_SAQUE:float = 500.0

    def __init__(self):
        self.saldo: float = 0.0
        self.saques_diarios: int = 0
        self.transacoes: List[str] = []

    def depositar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self.saldo += valor
        self.transacoes.append(f'Depósito: +{valor}R$')

    def sacar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente.")
        if self.saques_diarios >= Banco.MAX_SAQUES_DIARIOS:
            raise ValueError("Você só pode fazer 3 saques por dia.")
        if valor > Banco.VALOR_MAXIMO_SAQUE:
            raise ValueError("O valor máximo para saque é de 500R$.")
        
        self.saldo -= valor
        self.saques_diarios += 1
        self.transacoes.append(f'Saque: -{valor}R$')

    def extrato(self) -> None:
        print('Extrato:')
        for transacao in self.transacoes:
            print(transacao)
        print(f'Saldo atual: {self.saldo}R$')


def menu() -> None:
    banco:Banco = Banco()
    opcao:int = 0
    while opcao != 4:
        print('====================================================================================================')
        print(f'Saldo atual: {banco.saldo}R$')
        print('1 - Depositar\n2 - Sacar\n3 - Extrato\n4 - Sair')
        try:
            opcao = int(input('Escolha uma opção: '))
            if opcao == 1:
                valor = float(input('Digite o valor a ser depositado: '))
                banco.depositar(valor)
            elif opcao == 2:
                valor = float(input('Digite o valor a ser sacado: '))
                banco.sacar(valor)
            elif opcao == 3:
                banco.extrato()
            elif opcao == 4:
                print("Obrigado por usar nosso banco!")
                break
            else:
                print('Opção inválida. Por favor, escolha uma opção válida.')
        except ValueError as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    menu()