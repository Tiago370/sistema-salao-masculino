class Servico:
    def __init__(self, nomeServico, preco, valorComissao):
        self.nomeServico = nomeServico
        self.preco = preco
        self.valorComissao = valorComissao

    def getNomeServico(self):
        return self.nomeServico

    def getPreco(self):
        return self.preco

    def getValorComissao(self):
        return self.valorComissao

    def getReceitaSalao(self):
        return self.preco - self.valorComissao


