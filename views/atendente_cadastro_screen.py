from models import Cliente, Usuario, Problema, Chamado
from controllers import ClienteController, UsuarioController, ProblemaController, ChamadoController
import tkinter as tk
from tkinter import messagebox

class AtendenteCadastroScreen:

    def __init__(self, root) -> None:
        self.root = root
        self.id_atendente = ''
        self.usuario_controller = UsuarioController()
        self.bold_font = ('Helvetica', 12, 'bold')
        self.title_font = ('Helvetica', 14, 'bold')
        self.root.title('Trabalho de POO - Tela de Cadastro de Atendente')
        self.root.geometry('1280x720')
        
        # Cria um frame para os componentes de login
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Cria um frame interno para centralizar os widgets
        self.inner_frame = tk.Frame(self.frame)
        self.inner_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Titulo da tela
        self.title_label = tk.Label(self.inner_frame, text='Cadastro de Atendentes', font=self.title_font, anchor='center')
        self.title_label.grid(row=0, column=0, padx=0, pady=5, columnspan=2)
        
        # Lista de Chamados
        self.atendentes_listbox = tk.Listbox(self.inner_frame, font=self.bold_font, width=50, height=20)
        self.atendentes_listbox.grid(row=8, column=0, padx=20, pady=20, columnspan=2)

        self.listar_atendentes()

        self.atendentes_listbox.bind("<<ListboxSelect>>", self.listar_id_atendente)

        # Campo de entrada para o nome
        self.name_label = tk.Label(self.inner_frame, text='Nome:', font=self.bold_font, anchor='e', width=13)
        self.name_label.grid(row=1, column=0, padx=0, pady=2)
        self.name_input = tk.Entry(self.inner_frame, width=30)
        self.name_input.grid(row=1,column=1, padx=2, pady=2)

        # Campo de entrada para o email
        self.email_label = tk.Label(self.inner_frame, text='Email:', font=self.bold_font, anchor='e', width=13)
        self.email_label.grid(row=2, column=0, padx=0, pady=2)
        self.email_input = tk.Entry(self.inner_frame, width=30)
        self.email_input.grid(row=2,column=1, padx=2, pady=2)

        # Campo de entrada para a senha
        self.password_label = tk.Label(self.inner_frame, text='Senha:', font=self.bold_font, anchor='e', width=13)
        self.password_label.grid(row=3, column=0, padx=0, pady=2)
        self.password_input = tk.Entry(self.inner_frame, show='*', width=30)
        self.password_input.grid(row=3,column=1, padx=2, pady=2)

        # Campo de entrada para a confirmação de senha
        self.confirmation_password_label = tk.Label(self.inner_frame, text='Confirmar senha:', font=self.bold_font, anchor='e', width=13)
        self.confirmation_password_label.grid(row=4, column=0, padx=0, pady=2)
        self.confirmation_password_input = tk.Entry(self.inner_frame, show='*', width=30)
        self.confirmation_password_input.grid(row=4,column=1, padx=2, pady=2)
        
        # Botão de cadastro
        self.cadastro_button = tk.Button(self.inner_frame, text='Cadastrar', bg='green', fg='white', command=self.cadastrar_atendente)
        self.cadastro_button.grid(row=5, column=0, columnspan=2, sticky='ew', padx=2, pady=2) #Stick = expandir de leste a oeste
        
        # Botão de voltar
        self.voltar_button = tk.Button(self.inner_frame, text='Voltar', bg='blue', fg='white', command=self.open_login_screen)
        self.voltar_button.grid(row=6, column=0, columnspan=2, sticky='ew', padx=2, pady=2) #Stick = expandir de leste a oeste
        
        # Botão de delete
        self.deletar_button = tk.Button(self.inner_frame, text='Deletar', bg='red', fg='white', command=self.delete_atendente)
        self.deletar_button.grid(row=7, column=0, columnspan=2, sticky='ew', padx=2, pady=2) #Stick = expandir de leste a oeste

    def delete_atendente(self) -> None:
        if(not self.id_atendente):
            messagebox.showerror('Erro', 'Selecione um atendente primeiro!')
        else:
            usuario = self.usuario_controller.visualizar_usuario(self.id_atendente)
            confirm = messagebox.askyesno("Confirmar Exclusão", f"Tem certeza que deseja excluir o cliente: {usuario[0][1]} que possui o id: {usuario[0][0]}?")
            if(confirm):
                self.usuario_controller.excluir_usuario(usuario[0][0])
                messagebox.showinfo("Sucesso", f"Cliente {usuario[0][1]} excluído com sucesso.")
                self.listar_atendentes()

    def listar_id_atendente(self, event) -> None:
        # Obtém o widget que gerou o evento e o índice do item selecionado
        widget = event.widget
        index_selecionado = widget.curselection()
        if index_selecionado:
            index = index_selecionado[0]
            valor = widget.get(index)
            # Extrai o ID do atendente da string
            id_str = valor.split(" - ")[0].replace("ID: ", "")
            self.id_atendente = int(id_str)

    def listar_atendentes(self) -> None:
        self.atendentes_listbox.delete(0, tk.END)
        lista_atendentes = self.usuario_controller.listar_todos()
        for atendente in lista_atendentes:
            self.atendentes_listbox.insert(tk.END, f'ID: {atendente[0]:04} - Nome: {atendente[1]}')

    def cadastrar_atendente(self) -> None:
        nome = self.name_input.get()
        email = self.email_input.get()
        senha = self.password_input.get()
        confirmacao_senha = self.confirmation_password_input.get()
        
        if not self.entradas_validas(nome, email, senha, confirmacao_senha):
            messagebox.showerror('Cadastro', 'Preencha todos os campos!')
            return

        if senha != confirmacao_senha:
            messagebox.showerror('Cadastro', 'As senhas são diferentes!')
            return

        novo_usuario = Usuario(nome=nome, email=email, senha=senha, cargo="Atendente", id='')
        self.usuario_controller.criar_usuario(novo_usuario)
        messagebox.showinfo('Cadastro', f'Atendente {nome} cadastrado com sucesso!')
        self.listar_atendentes()

    def entradas_validas(self, nome, email, senha, confirmacao_senha) -> bool:
        return nome != '' and email != '' and senha != '' and confirmacao_senha != ''

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
