import tkinter as tk
import os.path
class Cliente:
    def __init__(self, nomeCliente, whatsApp):
        self.nomeCliente = nomeCliente
        self.whatsApp = whatsApp

    def getNomeCliente(self):
        return self.nomeCliente

    def getWhatsApp(self):
        return self.whatsApp

class LimiteCadastrarClientes(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Cadastrar Cliente")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameWhatsApp = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameWhatsApp.pack()
        self.frameButton.pack()
      
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelWhatsApp = tk.Label(self.frameWhatsApp,text="WhatsApp: ")
        self.labelNome.pack(side="left")
        self.labelWhatsApp.pack(side="left")  

        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")
        self.inputWhatsApp = tk.Entry(self.frameWhatsApp, width=20)
        self.inputWhatsApp.pack(side="left")             
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)


class ctrlCliente():       
    def __init__(self):
        if not os.path.isfile("cliente.pickle"):
            self.listaClientes =  []
        else:
            with open("cliente.pickle", "rb") as f:
                self.listaClientes = pickle.load(f)

    def salvaClientes(self):
        if len(self.listaClientes) != 0:
            with open("cliente.pickle","wb") as f:
                pickle.dump(self.listaClientes, f)

    def cadastrarCliente(self):
        self.limiteCadastrar = LimiteCadastrarClientes(self) 


    def getListaNroMatric(self):
        listaNro = []
        for est in self.listaEstudantes:
            listaNro.append(est.getNroMatric())
        return listaNro

    def insereEstudantes(self):
        self.limiteIns = LimiteInsereEstudantes(self) 

    def mostraEstudantes(self):
        str = 'Nro Matric. -- Nome\n'
        for est in self.listaEstudantes:
            str += est.getNroMatric() + ' -- ' + est.getNome() + '\n'       
        self.limiteLista = LimiteMostraEstudantes(str)

    def enterHandler(self, event):
        nroMatric = self.limiteIns.inputNro.get()
        nome = self.limiteIns.inputNome.get()
        estudante = Estudante(nroMatric, nome)
        self.listaEstudantes.append(estudante)
        self.limiteIns.mostraJanela('Sucesso', 'Estudante cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputNro.delete(0, len(self.limiteIns.inputNro.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()
    