from models import Cliente, Usuario, Problema, Chamado
from controllers import ClienteController, UsuarioController, ProblemaController, ChamadoController
import tkinter as tk
from tkinter import messagebox
from datetime import date 

class CadastroProblemaScreen:

    def __init__(self, root) -> None:
        self.root = root
        self.bold_font = ('Helvetica', 12, 'bold')
        self.title_font = ('Helvetica', 14, 'bold')
        self.cliente_controller = ClienteController()
        self.chamado_controller = ChamadoController()
        self.usuario_controller = UsuarioController()
        self.problema_controller = ProblemaController()
        self.root.title('Trabalho de POO - Tela de Cadastro de Problemas')
        self.root.geometry('1280x720')
        
        # Cria um frame para os componentes da tela
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        #Titulo da tela
        self.title_label = tk.Label(self.frame, text='Tela de Cadastro de Problemas', font=self.title_font, anchor='center')
        self.title_label.grid(row=0, column=0, padx=0, pady=5, columnspan=4)

        # Lista de Problemas
        self.problemas_listbox = tk.Listbox(self.frame, font=self.bold_font, width=50, height=20)
        self.problemas_listbox.grid(row=1, column=0, padx=20, pady=20, columnspan=3)
        
        self.listar_problemas()

        # Campo Descricao
        self.descricao_label = tk.Label(self.frame, text='Descricao:', font=self.bold_font, anchor='w')
        self.descricao_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.descricao_entry = tk.Entry(self.frame, width=30, fg='grey')
        self.descricao_entry.grid(row=2, column=1, padx=10, pady=10, sticky='ew')

        # Campo SLA
        self.sla_label = tk.Label(self.frame, text='SLA:', font=self.bold_font, anchor='w')
        self.sla_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.sla_entry = tk.Entry(self.frame, width=30, fg='grey')
        self.sla_entry.grid(row=3, column=1, padx=10, pady=10, sticky='ew')

        # Cria um frame para os componentes da tela
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.cadastrar_problema_button = tk.Button(self.frame, text="Cadastrar problema", font=self.bold_font, width=15, command=self.cadastrar_problema)
        self.cadastrar_problema_button.grid(row=4, column=0, padx=20, pady=10)

        self.voltar_button = tk.Button(self.frame, text="Voltar", font=self.bold_font, width=15, command=self.voltar_atendente)
        self.voltar_button.grid(row=4, column=1, padx=20, pady=10)

    def listar_problemas(self):
        lista_problemas = self.problema_controller.listar_todos()
        for problema in lista_problemas:
            self.problemas_listbox.insert(tk.END, f'ID: {problema[0]:04} - Descrição: {problema[1]} - SLA: {problema[2]}')

    def cadastrar_problema(self):
        novo_problema = Problema()
        novo_problema.descricao = self.descricao_entry.get()
        novo_problema.sla = self.sla_entry.get()
        self.problema_controller.criar_problema(novo_problema)
        messagebox.showinfo('Cadastro', 'Problema cadastrado com sucesso!')
        self.voltar_atendente()
    
    def voltar_atendente(self): 
        from .atendente_screen import AtendenteScreen
        self.exit()
        new_root = tk.Tk()
        atendente_screen_app = AtendenteScreen(new_root)
        new_root.mainloop()

    def exit(self):
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = CadastroProblemaScreen(root)
    root.mainloop()