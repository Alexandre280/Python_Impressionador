from datetime import datetime
import pytz

class ContaCorrente():


    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []

    def consultar_saldo(self):
        print('Seu saldo atual é de R${:,.2f}'.format(self.saldo))

    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):
        self.limite = -1000
        return self.limite

    def sacar_dinheiro(self, valor):
        if self.saldo - valor < self._limite_conta():
            print('Você não tem saldo suficiente para sacar esse valor')
            self.consultar_saldo()
        else:
            self.saldo -= valor
            self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))

    def consulta_limite_conta(self):
        print('Seu limite de Cheque Especial é de R${:,.2f}'. format(self._limite_conta()))

    def consulta_historico_transacoes(self):
        print('Historico de Transações')
        print('Valor, Saldo, Data e Hora')
        for transacao in self.transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        self.saldo -= valor
        self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))
        conta_destino.saldo += valor
        conta_destino.transacoes.append((valor, conta_destino.saldo, ContaCorrente._data_hora()))


#programa
conta_Alexandre = ContaCorrente('Alexandre', '999.999.999-99', '12345', '963258741')
conta_Alexandre.consultar_saldo()

#depositando dinheiro na conta
conta_Alexandre.depositar(10000)
conta_Alexandre.consultar_saldo()

#sacando um valor menor que o limite
conta_Alexandre.sacar_dinheiro(4000)
conta_Alexandre.consultar_saldo()

print('-'*20)
print(conta_Alexandre.consulta_historico_transacoes())

print('-'*20)
conta_Bru = ContaCorrente('Bru', '222,222,222-22', 7777, 77777777)
conta_Alexandre.transferir(2000, conta_Bru)

conta_Alexandre.consultar_saldo()
conta_Bru.consultar_saldo()

print('-'*20)
print(conta_Alexandre.consulta_historico_transacoes())

print('-'*20)
print(conta_Bru.consulta_historico_transacoes())

print(conta_Alexandre.transacoes)
print(conta_Bru.transacoes)