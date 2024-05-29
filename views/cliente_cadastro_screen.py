from models import Cliente, Usuario, Problema, Chamado
from controllers import ClienteController, UsuarioController, ProblemaController, ChamadoController
import tkinter as tk
from tkinter import messagebox

class ClienteCadastroScreen:

    def __init__(self, root) -> None:
        self.root = root
        self.selected_id_chamado = None
        self.bold_font = ('Helvetica', 12, 'bold')
        self.title_font = ('Helvetica', 14, 'bold')
        self.cliente_controller = ClienteController()
        self.chamado_controller = ChamadoController()
        self.usuario_controller = UsuarioController()
        self.problema_controller = ProblemaController()
        self.root.title('Trabalho de POO - Tela de Cadastro Cliente')
        self.root.geometry('1280x720')  

        # Cria um frame para os componentes da tela
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        # Cria titulo da tela       
        self.title_label = tk.Label(self.frame, text='Tela de Cadastro de Cliente', font=self.title_font, anchor='center')
        self.title_label.grid(row=0, column=0, padx=0, pady=5, columnspan=4)

        #Campo de entrada para o nome
        self.name_label = tk.Label(self.frame, text='Nome:', font=self.bold_font, anchor='e', width=13)
        self.name_label.grid(row=1, column=0, padx=0, pady=2)
        self.name_input = tk.Entry(self.frame, width=30)
        self.name_input.grid(row=1,column=1, padx=2, pady=2)

        #Campo de entrada para o email
        self.email_label = tk.Label(self.frame, text='Email:', font=self.bold_font, anchor='e', width=13)
        self.email_label.grid(row=2, column=0, padx=0, pady=2)
        self.email_input = tk.Entry(self.frame, width=30)
        self.email_input.grid(row=2,column=1, padx=2, pady=2)

        #Campo de entrada para o empresa
        self.empresa_label = tk.Label(self.frame, text='Empresa:', font=self.bold_font, anchor='e', width=13)
        self.empresa_label.grid(row=3, column=0, padx=0, pady=2)
        self.empresa_input = tk.Entry(self.frame, width=30)
        self.empresa_input.grid(row=3,column=1, padx=2, pady=2)

        #Campo de entrada para o telefone
        self.telefone_label = tk.Label(self.frame, text='Telefone:', font=self.bold_font, anchor='e', width=13)
        self.telefone_label.grid(row=4, column=0, padx=0, pady=2)
        self.telefone_input = tk.Entry(self.frame, width=30)
        self.telefone_input.grid(row=4,column=1, padx=2, pady=2)

        #Campo de entrada para o senha
        self.senha_label = tk.Label(self.frame, text='Senha:', font=self.bold_font, anchor='e', width=13)
        self.senha_label.grid(row=5, column=0, padx=0, pady=2)
        self.senha_input = tk.Entry(self.frame, width=30)
        self.senha_input.grid(row=5,column=1, padx=2, pady=2)

        self.cadastrar_cliente_button = tk.Button(self.frame, text="Cadastrar cliente", font=self.bold_font, width=15, command=self.cadastrar_cliente)
        self.cadastrar_cliente_button.grid(row=6, column=0, padx=2, pady=10)

        self.voltar_button = tk.Button(self.frame, text="Voltar", font=self.bold_font, width=15, command=self.voltar_atendente_screen)
        self.voltar_button.grid(row=6, column=1, padx=2, pady=10)

    def cadastrar_cliente(self) -> None:
        nome = self.name_input.get()
        email = self.email_input.get()
        empresa = self.empresa_input.get()
        telefone = self.telefone_input.get()
        senha = self.senha_input.get()

        if not self.entradas_validas(nome, email, empresa, telefone, senha):
            messagebox.showerror('Cadastro', 'Preencha todos os campos!')
            return
        
        novo_cliente = Cliente(nome=nome, email=email, empresa=empresa, telefone=telefone, id='', senha=senha)
        self.cliente_controller.criar_cliente(novo_cliente)
        messagebox.showinfo('Cadastrado', 'Cliente cadastrado com sucesso!')
        self.voltar_atendente_screen()
        
    def entradas_validas(self, nome, email, empresa, telefone, senha):
        return nome != '' and email != '' and empresa != '' and telefone != '' and senha != ''

    def voltar_atendente_screen(self) -> None:
        from .atendente_screen import AtendenteScreen
        self.exit()
        new_root = tk.Tk()
        atendente_chamado_app = AtendenteScreen(new_root)
        new_root.mainloop()

    def exit(self) -> None:
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ClienteCadastroScreen(root)
    root.mainloop()
