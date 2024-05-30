from models import Cliente, Usuario, Problema, Chamado
from controllers import ClienteController, UsuarioController, ProblemaController, ChamadoController
import tkinter as tk
from tkinter import messagebox
from datetime import date 

class CadastroChamadoClienteScreen:

    def __init__(self, root, id_cliente) -> None:
        self.root = root
        self.id_cliente = id_cliente
        self.selected_id_chamado = None
        self.bold_font = ('Helvetica', 12, 'bold')
        self.title_font = ('Helvetica', 14, 'bold')
        self.cliente_controller = ClienteController()
        self.chamado_controller = ChamadoController()
        self.usuario_controller = UsuarioController()
        self.problema_controller = ProblemaController()
        self.root.title('Trabalho de POO - Tela de Cadastro do Chamado do Cliente')
        self.root.geometry('1280x720')
        
        # Cria um frame para os componentes da tela
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        #Titulo da tela
        self.title_label = tk.Label(self.frame, text='Tela de Cadastro de Chamados do Cliente', font=self.title_font, anchor='center')
        self.title_label.grid(row=0, column=0, padx=0, pady=5, columnspan=4)

        # Campo Nome
        self.nome_label = tk.Label(self.frame, text='Nome:', font=self.bold_font, anchor='w')
        self.nome_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.nome_entry = tk.Entry(self.frame, width=30, fg='grey')
        self.nome_entry.grid(row=1, column=1, padx=10, pady=10, sticky='ew')

        # Campo Empresa
        self.empresa_label = tk.Label(self.frame, text='Empresa:', font=self.bold_font, anchor='w')
        self.empresa_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.empresa_entry = tk.Entry(self.frame, width=30, fg='grey')
        self.empresa_entry.grid(row=2, column=1, padx=10, pady=10, sticky='ew')

        # Campo Telefone
        self.telefone_label = tk.Label(self.frame, text='Telefone:', font=self.bold_font, anchor='w')
        self.telefone_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.telefone_entry = tk.Entry(self.frame, width=30, fg='grey')
        self.telefone_entry.grid(row=3, column=1, padx=10, pady=10, sticky='ew')

        # Campo Título
        self.titulo_label = tk.Label(self.frame, text='Título:', font=self.bold_font, anchor='w')
        self.titulo_label.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        self.titulo_entry = tk.Entry(self.frame, width=30, fg='grey')
        self.titulo_entry.grid(row=4, column=1, padx=10, pady=10, sticky='ew')

        # Campo Descrição do Relato
        self.descricao_label = tk.Label(self.frame, text='Descrição do Relato:', font=self.bold_font, anchor='w')
        self.descricao_label.grid(row=5, column=0, padx=10, pady=10, sticky='w')

        self.text_area_descricao = tk.Text(self.frame, wrap=tk.WORD, width=40, height=10)
        self.text_area_descricao.grid(row=6,column=0, columnspan=2, padx=10, pady=10)

        # Botão de cadastrar chamado
        self.cadastrar_button = tk.Button(self.frame, text='Cadastrar Chamado', command=self.cadastrar_chamado, bg='green', fg='white')
        self.cadastrar_button.grid(row=7, column=1, pady=20, padx=10, sticky='ew')

        # Botão de voltar
        self.voltar_button = tk.Button(self.frame, text='Voltar', command=self.voltar_cliente_screen, bg='#E57373', fg='white')
        self.voltar_button.grid(row=7, column=2, pady=20, padx=10, sticky='ew') 
        
    def cadastrar_chamado(self) -> None:
        chamado_do_cliente = Chamado()
        chamado_do_cliente.titulo = self.titulo_entry.get()
        chamado_do_cliente.descricao = self.text_area_descricao.get("1.0", tk.END).strip()
        cliente = self.cliente_controller.visualizar_cliente(self.id_cliente)
        chamado_do_cliente.id_cliente = self.id_cliente
        chamado_do_cliente.status = 'Aberto'
        chamado_do_cliente.data_abertura = date.today().strftime("%d/%m/%Y")
        self.chamado_controller.criar_chamado(chamado_do_cliente)
        messagebox.showinfo('Cadastro', 'Chamado cadastrado com sucesso!')
        self.voltar_cliente_screen()

    def voltar_cliente_screen(self) -> None:
        from .cliente_screen import ClienteScreen
        self.exit()
        new_root = tk.Tk()
        login_screen_app = ClienteScreen(new_root, self.id_cliente)
        new_root.mainloop()

    def exit(self) -> None:
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = CadastroChamadoClienteScreen(root)
    root.mainloop()