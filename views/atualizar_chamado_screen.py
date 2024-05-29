from models import Cliente, Usuario, Problema, Chamado
from controllers import ClienteController, UsuarioController, ProblemaController, ChamadoController
import tkinter as tk
from tkinter import messagebox

class AtualizarChamadoScreen:

    def __init__(self, root, id_chamado) -> None:
        self.root = root
        self.chamado_controller = ChamadoController()
        self.usuario_controller = UsuarioController()
        self.chamado = self.chamado_controller.visualizar_chamado(id_chamado)
        self.bold_font = ('Helvetica', 12, 'bold')
        self.title_font = ('Helvetica', 14, 'bold')
        self.root.title('Trabalho de POO - Gerenciar Chamado Screen')
        self.root.geometry('1280x720')
                
        # Cria um frame para os componentes da tela
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        #Titulo da tela
        self.title_label = tk.Label(self.frame, text=f'Chamado {id_chamado:04}', font=self.title_font, anchor='center')
        self.title_label.grid(row=0, column=0, padx=0, pady=5, columnspan=4)

        # Adquiro todos os atendentes
        atendentes = self.usuario_controller.listar_todos()
        nomes_atendentes = [f'{atendente[0]}-{atendente[1]}' for atendente in atendentes]
        # Obtém o ID do atendente associado ao chamado
        id_atendente_chamado = self.chamado[0][5]
        nome_atendente_chamado = ''
        if id_atendente_chamado:
            nome_atendente_chamado = f'{id_atendente_chamado}-{self.usuario_controller.visualizar_usuario(id_atendente_chamado)[0][1]}'  # Corrigi o índice para obter o nome
        
        # Label para o OptionMenu
        self.atendente_chamado_label = tk.Label(self.frame, text='Atendente', font=self.bold_font, anchor='center')
        self.atendente_chamado_label.grid(row=1, column=0, padx=10, pady=5)
        # Variável para armazenar o atendente selecionado
        self.atendente_selecionado = tk.StringVar(root)
        self.atendente_selecionado.set(nome_atendente_chamado if nome_atendente_chamado else "")
        # Select dos atendentes (OptionMenu)
        self.option_menu = tk.OptionMenu(self.frame, self.atendente_selecionado, *nomes_atendentes)
        self.option_menu.grid(row=1, column=1, padx=10, pady=5)
        
    def exit(self) -> None:
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AtualizarChamadoScreen(root)
    root.mainloop()
