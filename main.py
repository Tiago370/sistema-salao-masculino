import tkinter as tk
import cliente as cli
import profissional as pro
import atendimento as ate
import servico as ser

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('1400x700')
        self.menubar = tk.Menu(self.root)        
        self.atendimentoMenu = tk.Menu(self.menubar)
        self.servicoMenu = tk.Menu(self.menubar)
        self.clienteMenu = tk.Menu(self.menubar)
        self.profissionalMenu = tk.Menu(self.menubar)    

        self.atendimentoMenu.add_command(label="Cadastrar Atendimento", \
                    command=self.controle.cadastrarAtendimento)
        self.atendimentoMenu.add_command(label="Remover Atendimento", \
                    command=self.controle.removerAtendimento)
        self.menubar.add_cascade(label="Atendimento", \
                    menu=self.atendimentoMenu)

        self.servicoMenu.add_command(label="Cadastrar Serviço", \
                    command=self.controle.cadastrarServico)
        self.servicoMenu.add_command(label="Remover Serviço", \
                    command=self.controle.removerServico)
        self.menubar.add_cascade(label="Serviço", \
                    menu=self.servicoMenu)

        self.clienteMenu.add_command(label="Cadastrar Cliente", \
                    command=self.controle.cadastrarCliente)
        self.clienteMenu.add_command(label="Remover Cliente", \
                    command=self.controle.removerCliente)
                             
        self.menubar.add_cascade(label="Cliente", \
                    menu=self.clienteMenu)        

        self.profissionalMenu.add_command(label="Cadastrar Profissional", \
                    command=self.controle.cadastrarProfissional)
        self.profissionalMenu.add_command(label="Remover Profissional", \
                    command=self.controle.removerProfissional)
        self.menubar.add_cascade(label="Profissional", \
                    menu=self.profissionalMenu)

        self.root.config(menu=self.menubar)

      
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlCliente = cli.ctrlCliente()
        #self.ctrlDisciplina = disc.CtrlDisciplina()
        #self.ctrlTurma = trm.CtrlTurma(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Sistema Gerenciador de Salão Masculino")
        # Inicia o mainloop
        self.root.mainloop()
       
    def cadastrarAtendimento(self):
        self.ctrlAtendimento.cadastrarAtendimento()

    def removerAtendimento(self):
        self.ctrlAtendimento.removerAtendimento()

    def cadastrarServico(self):
        self.ctrlServico.cadastrarServico()

    def removerServico(self):
        self.ctrlServico.removerServico()

    def cadastrarCliente(self):
        self.ctrlCliente.cadastrarCliente()

    def removerCliente(self):
        self.ctrlCliente.removerCliente()

    def cadastrarProfissional(self):
        self.ctrlProfissional.cadastrarProfissional()

    def removerProfissional(self):
        self.ctrlProfissional.removerProfissional()

if __name__ == '__main__':
    c = ControlePrincipal()