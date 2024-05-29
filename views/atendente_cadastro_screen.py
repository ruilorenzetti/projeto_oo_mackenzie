from models import Cliente, Usuario, Problema, Chamado
from controllers import ClienteController, UsuarioController, ProblemaController, ChamadoController
import tkinter as tk
from tkinter import messagebox

class AtendenteCadastroScreen:

    def __init__(self, root) -> None:
        self.root = root
        self.usuario_controller = UsuarioController()
        self.bold_font = ('Helvetica', 12, 'bold')
        self.title_font = ('Helvetica', 14, 'bold')
        self.root.title('Trabalho de POO - Tela de Cadastro de Atendente')
        self.root.geometry('1280x720')
        
        # Cria um frame para os componentes de login
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=200)

        #Titulo da tela
        self.title_label = tk.Label(self.frame, text='Cadastro de Atendentes', font=self.title_font, anchor='center')
        self.title_label.grid(row=0, column=0, padx=0, pady=5, columnspan=2)

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

        #Campo de entrada para a senha
        self.password_label = tk.Label(self.frame, text='Senha:', font=self.bold_font, anchor='e', width=13)
        self.password_label.grid(row=3, column=0, padx=0, pady=2)
        self.password_input = tk.Entry(self.frame, show='*', width=30)
        self.password_input.grid(row=3,column=1, padx=2, pady=2)

        #Campo de entrada para a confirmação de senha
        self.confirmation_password_label = tk.Label(self.frame, text='Confirmar senha:', font=self.bold_font, anchor='e', width=13)
        self.confirmation_password_label.grid(row=4, column=0, padx=0, pady=2)
        self.confirmation_password_input = tk.Entry(self.frame, show='*', width=30)
        self.confirmation_password_input.grid(row=4,column=1, padx=2, pady=2)
        
        #Botão de cadastro
        self.cadastro_button = tk.Button(self.frame, text='Cadastrar', bg='green', fg='white', command=self.cadastrar_atendente)
        self.cadastro_button.grid(row=5, column=0, columnspan=2, sticky='ew', padx=2, pady=2) #Stick = expandir de leste a oeste
        
        #Botão de voltar
        self.voltar_button = tk.Button(self.frame, text='Voltar', bg='blue', fg='white', command=self.open_login_screen)
        self.voltar_button.grid(row=6, column=0, columnspan=2, sticky='ew', padx=2, pady=2) #Stick = expandir de leste a oeste

    def cadastrar_atendente(self) -> None:
        nome = self.name_input.get()
        email = self.email_input.get()
        senha = self.password_input.get()
        confirmacao_senha = self.confirmation_password_input.get()
        
        if not self.entradas_validas(nome, email, senha):
            messagebox.showerror('Cadastro', 'Preencha todos os campos!')
            return

        if senha != confirmacao_senha:
            messagebox.showerror('Cadastro', 'As senhas são diferentes!')
            return

        novo_usuario = Usuario(nome=nome, email=email, senha=senha, cargo="Atendente", id='')
        self.usuario_controller.criar_usuario(novo_usuario)
        messagebox.showinfo('Cadastro', f'Atendente {nome} cadastrado com sucesso!')
        self.open_login_screen()

    def entradas_validas(self, nome, email, senha) -> bool:
        return nome != '' and email != '' and senha != ''

    def open_login_screen(self) -> None:
        from .login_screen import LoginScreen
        self.exit()
        new_root = tk.Tk()
        login_app = LoginScreen(new_root)
        new_root.mainloop()
    
    def exit(self) -> None:
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AtendenteCadastroScreen(root)
    root.mainloop()