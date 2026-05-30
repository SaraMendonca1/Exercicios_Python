# Trazendo List e Optional pra "avisar" pro código quais tipos de dados vão entrar 
from typing import List, Optional

#as classes

class ContaBancaria:
    def __init__(self, numero_conta: str, titular: str, saldo_inicial: float = 0.0):
        # Quando a conta é criada, ela precisa receber esses três dados
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor: float) -> None:
        # Só deixa colocar dinheiro se for um valor positivo
        if valor > 0:
            self.saldo += valor

    def sacar(self, valor: float) -> bool:
        #só saca se o valor for maior que zero E se tiver saldo suficiente
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            return True # Deu certo
        return False #não tem saldo

    def verificar_saldo(self) -> float:
        # devolve o número que tá guardado no saldo
        return self.saldo


class Cliente:
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf
        # Todo cliente nasce com uma lista vazia, pronto pra receber várias contas
        self.contas: List[ContaBancaria] = []

    def adicionar_conta(self, conta: ContaBancaria) -> None:
        # Pega a conta nova e pões dentro da lista de contas do cliente
        self.contas.append(conta)


class Banco:
    def __init__(self):
        # O banco também nasce vazio, só com uma lista pra guardar os clientes
        self.clientes: List[Cliente] = []

    def adicionar_cliente(self, cliente: Cliente) -> None:
        self.clientes.append(cliente)

    def buscar_conta(self, numero_conta: str) -> Optional[ContaBancaria]:
        #busca rápida: Procura em todas as contas de todos os clientes se o número bate com o que foi digitado
        return next((c for cli in self.clientes for c in cli.contas if c.numero_conta == numero_conta), None)


#terminal

if __name__ == "__main__":
    # Criando o banco
    banco = Banco()
    nome_banco = "TechBank"

    # Criando o cliente Carlos e já salvando na memória
    cliente1 = Cliente("Carlos Andrade", "777.888.999-11")
    
    # Criando a primeira conta dele com 2500 reais e vinculando ao perfil dele
    conta1 = ContaBancaria("101-A", cliente1.nome, saldo_inicial=2500.0)
    cliente1.adicionar_conta(conta1)
    print(f"Conta {conta1.numero_conta} adicionada ao cliente {cliente1.nome}.")

    # Criando a segunda conta dele
    conta2 = ContaBancaria("102-B", cliente1.nome, saldo_inicial=150.0)
    cliente1.adicionar_conta(conta2)
    print(f"Conta {conta2.numero_conta} adicionada ao cliente {cliente1.nome}.")

    # Registrando o Carlos oficialmente no Banco
    banco.adicionar_cliente(cliente1)
    print(f"Cliente {cliente1.nome} adicionado ao banco {nome_banco}.\n")

    # Varrendo a lista de contas do Carlos e retornando uma por uma
    print(f"Contas de {cliente1.nome}:")
    for conta in cliente1.contas:
        print(f" Número: {conta.numero_conta}, Saldo: R$ {conta.verificar_saldo():.2f}")

    # Testando a matemática do depósito
    valor_deposito = 500.0
    conta1.depositar(valor_deposito)
    print(f"Depósito de R$ {valor_deposito:.2f} realizado. Novo saldo: R$ {conta1.verificar_saldo():.2f}")

    # Testando a matemática do saque
    valor_saque = 800.0
    conta1.sacar(valor_saque)
    print(f"Saque de R$ {valor_saque:.2f} realizado. Novo saldo: R$ {conta1.verificar_saldo():.2f}")

    print(f"Saldo atual da conta {conta1.numero_conta}: R$ {conta1.verificar_saldo():.2f}\n")
    
    # Usando busca rápida pra ver se o Carlos tá na memória do banco
    cliente_encontrado = next((c.nome for c in banco.clientes if c.nome == "Carlos Andrade"), None)
    if cliente_encontrado:
        print(f"Cliente encontrado: {cliente_encontrado}")