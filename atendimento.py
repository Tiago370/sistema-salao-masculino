from datetime import datetime
class Atendimento:
    def __init__(self, cliente, nomeProfissional):
        self.cliente = cliente
        self.nomeProfissional = nomeProfissional
        self.servicosRealizados = []
        self.dataEHora = datetime.now()

    def getCliente(self):
        return self.cliente

    def getNomeProfissional(self):
        return self.nomeProfissional

    def getServicosRealizados(self):
        return self.servicosRealizados

    def getValorTotal(self):
        valorTotal = 0
        for servico in self.servicosRealizados:
            valorTotal += servico.getPreco()
        return valorTotal

    def getComissaoTotal(self):
        ComissaoTotal = 0
        for servico in self.servicosRealizados:
            ComissaoTotal += servico.getValorComissao()
        return ComissaoTotal

    def addServico(self, servico):
        self.servicosRealizados.append(servico)
