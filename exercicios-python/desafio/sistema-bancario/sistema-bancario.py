from typing import List, Optional


class ContaBancaria:
    def __init__(self, numero_conta: str, titular: str, saldo_inicial: float = 0.0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor: float) -> None:
        if valor > 0:
            self.saldo += valor

    def sacar(self, valor: float) -> bool:
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            return True
        return False

    def verificar_saldo(self) -> float:
        return self.saldo


class Cliente:
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf
        self.contas: List[ContaBancaria] = []

    def adicionar_conta(self, conta: ContaBancaria) -> None:
        self.contas.append(conta)


class Banco:
    def __init__(self):
        self.clientes: List[Cliente] = []

    def adicionar_cliente(self, cliente: Cliente) -> None:
        self.clientes.append(cliente)

    def buscar_conta(self, numero_conta: str) -> Optional[ContaBancaria]:
        return next((c for cli in self.clientes for c in cli.contas if c.numero_conta == numero_conta), None)



if __name__ == "__main__":
    banco = Banco()
    nome_banco = "TechBank"

    cliente1 = Cliente("Carlos Andrade", "777.888.999-11")
    
    conta1 = ContaBancaria("101-A", cliente1.nome, saldo_inicial=2500.0)
    cliente1.adicionar_conta(conta1)
    print(f"Conta {conta1.numero_conta} adicionada ao cliente {cliente1.nome}.")

    conta2 = ContaBancaria("102-B", cliente1.nome, saldo_inicial=150.0)
    cliente1.adicionar_conta(conta2)
    print(f"Conta {conta2.numero_conta} adicionada ao cliente {cliente1.nome}.")

    banco.adicionar_cliente(cliente1)
    print(f"Cliente {cliente1.nome} adicionado ao banco {nome_banco}.")

    cliente2 = Cliente("Fernanda Costa", "444.555.666-22")
    
    conta3 = ContaBancaria("201-C", cliente2.nome, saldo_inicial=0.0)
    cliente2.adicionar_conta(conta3)
    print(f"Conta {conta3.numero_conta} adicionada ao cliente {cliente2.nome}.")

    banco.adicionar_cliente(cliente2)
    print(f"Cliente {cliente2.nome} adicionado ao banco {nome_banco}.\n")

    print(f"Contas de {cliente1.nome}:")
    for conta in cliente1.contas:
        print(f" Número: {conta.numero_conta}, Saldo: R$ {conta.verificar_saldo():.2f}")

    valor_deposito = 500.0
    conta1.depositar(valor_deposito)
    print(f"Depósito de R$ {valor_deposito:.2f} realizado. Novo saldo: R$ {conta1.verificar_saldo():.2f}")

    valor_saque = 800.0
    conta1.sacar(valor_saque)
    print(f"Saque de R$ {valor_saque:.2f} realizado. Novo saldo: R$ {conta1.verificar_saldo():.2f}")

    print(f"Saldo atual da conta {conta1.numero_conta}: R$ {conta1.verificar_saldo():.2f}\n")

    
    cliente_encontrado = next((c.nome for c in banco.clientes if c.nome == "Carlos Andrade"), None)
    if cliente_encontrado:
        print(f"Cliente encontrado: {cliente_encontrado}")

    conta_encontrada = banco.buscar_conta("201-C")
    if conta_encontrada:
        print(f"Conta encontrada: {conta_encontrada.numero_conta} do titular {conta_encontrada.titular}")