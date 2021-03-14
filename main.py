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

        self.atendimentoMenu.add_command(label="Cadastar Atendimento", \
                    command=self.controle.insereEstudantes)
        self.atendimentoMenu.add_command(label="Remover Atendimento", \
                    command=self.controle.mostraEstudantes)
        self.menubar.add_cascade(label="Atendimento", \
                    menu=self.atendimentoMenu)

        self.servicoMenu.add_command(label="Cadastrar Serviço", \
                    command=self.controle.insereDisciplinas)
        self.servicoMenu.add_command(label="Remover Serviço", \
                    command=self.controle.mostraDisciplinas)        
        self.menubar.add_cascade(label="Serviço", \
                    menu=self.servicoMenu)

        self.clienteMenu.add_command(label="Cadastrar Cliente", \
                    command=self.controle.insereTurmas)
        self.clienteMenu.add_command(label="Remover Cliente", \
                    command=self.controle.mostraTurmas)
                             
        self.menubar.add_cascade(label="Cliente", \
                    menu=self.clienteMenu)        

        self.profissionalMenu.add_command(label="Cadastrar Profissional", \
                    command=self.controle.salvaDados)
        self.menubar.add_cascade(label="Profissional", \
                    menu=self.profissionalMenu)

        self.root.config(menu=self.menubar)

      
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        #self.ctrlEstudante = est.CtrlEstudante()
        #self.ctrlDisciplina = disc.CtrlDisciplina()
        #self.ctrlTurma = trm.CtrlTurma(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Sistema Gerenciador de Salão Masculino")
        # Inicia o mainloop
        self.root.mainloop()
       
    def insereEstudantes(self):
        self.ctrlEstudante.insereEstudantes()

    def mostraEstudantes(self):
        self.ctrlEstudante.mostraEstudantes()

    def insereDisciplinas(self):
        self.ctrlDisciplina.insereDisciplinas()

    def mostraDisciplinas(self):
        self.ctrlDisciplina.mostraDisciplinas()

    def insereTurmas(self):
        self.ctrlTurma.insereTurmas()

    def mostraTurmas(self):
        self.ctrlTurma.mostraTurmas()

    def removeAluno(self):
        self.ctrlTurma.removeAluno()

    def salvaDados(self):
        self.ctrlEstudante.salvaEstudantes()
        self.ctrlDisciplina.salvaDisciplina()
        self.ctrlTurma.salvaTurmas()
        self.root.destroy()

if __name__ == '__main__':
    c = ControlePrincipal()