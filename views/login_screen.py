from models import Cliente, Usuario, Problema, Chamado
from controllers import ClienteController, UsuarioController, ProblemaController, ChamadoController
from .atendente_screen import AtendenteScreen
from .atendente_cadastro_screen import AtendenteCadastroScreen
import tkinter as tk
from tkinter import messagebox

class LoginScreen:

    def __init__(self, root) -> None:
        self.root = root
        self.usuario_controller = UsuarioController()
        self.bold_font = ('Helvetica', 12, 'bold')
        self.root.title('Trabalho de POO - Sistema ERP')
        self.root.geometry('1280x720')
        
        # Cria um frame para os componentes de login
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=100)

        #Campo de entrada para o usuario
        self.username_label = tk.Label(self.frame, text='Usuario:', font=self.bold_font, anchor='w')
        self.username_label.grid(row=0, column=0, padx=0, pady=2)
        self.username_input = tk.Entry(self.frame, width=30)
        self.username_input.grid(row=0, column=1, padx=2, pady=2)

        #Campo de entrada para a senha
        self.password_label = tk.Label(self.frame, text='Senha:', font=self.bold_font, anchor='w', width=7)
        self.password_label.grid(row=1, column=0, padx=0, pady=2)
        self.password_input = tk.Entry(self.frame, show='*', width=30)
        self.password_input.grid(row=1,column=1, padx=2, pady=2)

        #Botão de login
        self.login_button = tk.Button(self.frame, text='Entrar', command=self.login, bg='green', fg='white')
        self.login_button.grid(row=2, column=0, sticky='ew', padx=2) #Stick = expandir de leste a oeste

        #Botão de sair
        self.exit_button = tk.Button(self.frame, text='Sair', command=self.exit, bg='#E57373', fg='white')
        self.exit_button.grid(row=2, column=1, sticky='ew', padx=2) #Stick = expandir de leste a oeste

        #Texto clicavel para cadastro de atendente
        self.cadastro_atendente_label = tk.Label(self.frame, text='Cadastrar atendente', fg='blue', cursor='hand2')
        self.cadastro_atendente_label.grid(row=3, column=0, columnspan=2, sticky='ew')
        #Caso a label de "Cadastrar atendente" for clicado pelo botao numero 1 do mouse (esquerdo), chama função
        self.cadastro_atendente_label.bind("<Button-1>", lambda e: self.open_cadastro_atendente_screen())

    def open_cadastro_atendente_screen(self) -> None:
        self.exit()
        new_root = tk.Tk()
        atendente_cadastro_app = AtendenteCadastroScreen(new_root)
        new_root.mainloop()

    def login(self) -> None:
        username = self.username_input.get()
        password = self.password_input.get()

        nome_usuario = self.validar_credenciais(username, password)
        if nome_usuario:
            # Se o retorno não for None, mostra o nome do usuário
            messagebox.showinfo('Login', f'Bem-vindo ao sistema, {nome_usuario}!')
            self.open_atendente_screen()
        else:
            # Se o retorno for None, mostra a mensagem de erro.
            messagebox.showerror('Login', 'Usuário ou senha incorretos!')

    def validar_credenciais(self, email, password) -> str:
        usuarios_banco = self.usuario_controller.listar_todos()
        for usuario in usuarios_banco:
            # Assume-se que o email está no índice 2 e a senha no índice 3, nome no índice 1
            if usuario[2] == email and usuario[3] == password:
                return usuario[1]  # Retorna o nome do usuário
        return None  # Retorna None se nenhum usuário válido for encontrado

    def open_atendente_screen(self) -> None:
        self.exit()
        new_root = tk.Tk()
        atendente_app = AtendenteScreen(new_root)
        new_root.mainloop()

    def exit(self) -> None:
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginScreen(root)
    root.mainloop()