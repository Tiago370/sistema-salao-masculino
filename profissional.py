from datetime import datetime
class Profissional:
    def __init__(self, nomeProfissional):
        self.nomeProfissional = nomeProfissional
        self.atendimentosRealizados = []
        self.saldo = 0        
        retiradas = []

    def getNomeProfissional(self):
        return self.nomeProfissional

    def getAtendimentosRealizados(self):
        return self.atendimentosRealizados

    def getSaldo(self):
        return self.saldo

    def addAtendimento(self, atendimento):
        self.atendimentosRealizados.append(atendimento)
        comissao = atendimento.getComissaoTotal()
        self.depositarNoSaldo(comissao)

    def depositarNoSaldo(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.retiradas.push((datetime.now(), valor))
            return True
        else:
            return False
