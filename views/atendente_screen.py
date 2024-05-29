from models import Cliente, Usuario, Problema, Chamado
from controllers import ClienteController, UsuarioController, ProblemaController, ChamadoController
import tkinter as tk
from tkinter import messagebox

class AtendenteScreen:

    def __init__(self, root) -> None:
        self.root = root
        self.bold_font = ('Helvetica', 12, 'bold')
        self.title_font = ('Helvetica', 14, 'bold')
        self.cliente_controller = ClienteController()
        self.root.title('Trabalho de POO - Tela Atendente')
        self.root.geometry('1280x720')
        
        # Cria um frame para os componentes da tela
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        #Titulo da tela
        self.title_label = tk.Label(self.frame, text='Tela de Atendentes', font=self.title_font, anchor='center')
        self.title_label.grid(row=0, column=0, padx=0, pady=5, columnspan=4)

        #Subtitulo Lista de chamados
        self.title_label = tk.Label(self.frame, text='Lista de chamados:', font=self.title_font, anchor='e')
        self.title_label.grid(row=1, column=0, padx=0, pady=5, columnspan=2)

        # Lista de Chamados
        self.chamados_listbox = tk.Listbox(self.frame, font=self.bold_font, width=50, height=20)
        self.chamados_listbox.grid(row=2, column=0, padx=20, pady=20, columnspan=2)

        #Subtitulo Detalhes do chamado
        self.title_label = tk.Label(self.frame, text='Detalhes do chamado', font=self.title_font, anchor='e')
        self.title_label.grid(row=1, column=2, padx=0, pady=5, columnspan=2)

        # Detalhes do Chamado
        self.detalhes_text = tk.Text(self.frame, font=self.bold_font, width=50, height=21)
        self.detalhes_text.grid(row=2, column=2, padx=20, pady=20, columnspan=2)
        
        # Botões de Ação
        self.criar_usuario_button = tk.Button(self.frame, text="Criar usuario", font=self.bold_font, width=15, command=self.criar_cliente)
        self.criar_usuario_button.grid(row=3, column=0, padx=20, pady=10)

        self.excluir_usuario_button = tk.Button(self.frame, text="Excluir usuario", font=self.bold_font, width=15, command=self.excluir_cliente)
        self.excluir_usuario_button.grid(row=3, column=1, padx=20, pady=10)
        
        self.consultar_chamado_button = tk.Button(self.frame, text="Consultar chamado", font=self.bold_font, width=15, command=self.consultar_chamado)
        self.consultar_chamado_button.grid(row=3, column=2, padx=20, pady=10)

        self.atualizar_chamado_button = tk.Button(self.frame, text="Atualizar chamado", font=self.bold_font, width=15, command=self.atualizar_chamado)
        self.atualizar_chamado_button.grid(row=3, column=3, padx=20, pady=10)

    def criar_cliente(self):
        pass

    def excluir_cliente(self) -> None:
        from .excluir_cliente_screen import ExcluirClienteScreen
        self.exit()
        new_root = tk.Tk()
        excluir_cliente_app = ExcluirClienteScreen(new_root)
        new_root.mainloop()

    def consultar_chamado(self):
        messagebox.showinfo("Info", "Função consultar chamado ainda não implementada")

    def atualizar_chamado(self):
        messagebox.showinfo("Info", "Função atualizar chamado ainda não implementada")

    def listar_chamados(self):
        pass

    def exit(self) -> None:
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AtendenteScreen(root)
    root.mainloop()
