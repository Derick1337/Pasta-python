""" class ContaBancaria:
    def __init__(self, numero_conta, saldo):
        self.__numero_conta = numero_conta  # Atributo privado
        self.__saldo = saldo                # Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

    def obter_saldo(self):
        return self.__saldo

# Criando uma instância de ContaBancaria
conta = ContaBancaria("12345", 700)

# Acessando e modificando atributos indiretamente por meio de métodos
conta.depositar(500)
conta.sacar(200)

# Obtendo o saldo por meio de um método
saldo = conta.obter_saldo()
print(f"Saldo da conta: {saldo}")
 """
class Carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def __str__(self):
        return f"Carro: {self.modelo} {self.ano} {self.cor}"
carro=input('digite o modelo do carro: ')
ano=input('digite o ano do carro: ')
cor=input('digite a cor do carro: ')
carro1=Carro(carro,ano,cor)
print(carro1)

