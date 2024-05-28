import tkinter as tk
from tkinter import messagebox, font as tkfont
from datetime import datetime, timedelta
from GerenciadorUsuarios import *
from GerenciadorChamados import *

class PlaceholderEntry(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey', font=None, show=None):
        super().__init__(master, font=font, show=show, relief='flat',
                         highlightbackground="#d3d3d3", highlightcolor="#d3d3d3", highlightthickness=1)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']
        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)
        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

class LoginScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("Projeto Final POO - Gerenciador de Chamados")
        self.master.geometry("1280x720")
        self.master.config(bg="#f3f4f6")

        self.title_font = tkfont.Font(family="Helvetica", size=24, weight="bold")
        self.label_font = tkfont.Font(family="Helvetica", size=14)
        self.button_font = tkfont.Font(family="Helvetica", size=12)

        self.frame = tk.Frame(self.master, bg="#f3f4f6")
        self.frame.pack(pady=100)

        self.usuario_controller = UsuarioController()
        self.chamado_controller = ChamadoController()

        self.atendente_name_logado = None  # Track the logged-in attendant's name

        self.show_login_form()

    def create_button(self, parent, text, command, width=20, height=1, bg="#4CAF50", fg="white"):
        return tk.Button(parent, text=text, command=command, font=self.button_font,
                         bg=bg, fg=fg, height=height, width=width, relief="groove", borderwidth=2, padx=5, pady=5)

    def show_login_form(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        tk.Label(self.frame, text="Gerenciamento de Chamados do ERP", font=self.title_font, bg="#f3f4f6").pack(pady=(0, 10))
        tk.Label(self.frame, text="Digite aqui as suas informações", font=self.label_font, bg="#f3f4f6").pack(pady=(0, 20))

        self.entry_username = PlaceholderEntry(self.frame, placeholder="Email", font=self.label_font)
        self.entry_username.pack(pady=(0, 20), ipadx=10, ipady=5, fill='x')
        self.entry_password = PlaceholderEntry(self.frame, placeholder="Senha", font=self.label_font, show="*")
        self.entry_password.pack(pady=(0, 20), ipadx=10, ipady=5, fill='x')

        self.create_button(self.frame, "ACESSAR", self.validate_login).pack(pady=(20, 10), fill='x')

        tk.Label(self.frame, text="Cadastre aqui um atendente!", font=self.button_font, fg="blue", bg="#f3f4f6", cursor="hand2").pack()
        self.frame.winfo_children()[-1].bind("<Button-1>", self.show_register_form)

    def show_register_form(self, event=None):
        for widget in self.frame.winfo_children():
            widget.destroy()

        tk.Label(self.frame, text="Cadastro de Atendente", font=self.title_font, bg="#f3f4f6").pack(pady=(0, 10))
        tk.Label(self.frame, text="Preencha os dados abaixo", font=self.label_font, bg="#f3f4f6").pack(pady=(0, 20))

        self.entry_name = PlaceholderEntry(self.frame, placeholder="Nome", font=self.label_font)
        self.entry_name.pack(pady=(0, 20), ipadx=10, ipady=5, fill='x')
        self.entry_email = PlaceholderEntry(self.frame, placeholder="Email", font=self.label_font)
        self.entry_email.pack(pady=(0, 20), ipadx=10, ipady=5, fill='x')
        self.entry_password = PlaceholderEntry(self.frame, placeholder="Senha", font=self.label_font, show="*")
        self.entry_password.pack(pady=(0, 20), ipadx=10, ipady=5, fill='x')

        self.create_button(self.frame, "Cadastrar", self.register_user).pack(pady=(20, 10), fill='x')

    def validate_login(self):
        email = self.entry_username.get()
        senha = self.entry_password.get()
        try:
            usuario = self.usuario_controller.buscar_usuario_por_email(email)
            if usuario and usuario.senha == senha:
                if usuario.cargo.lower() == "atendente":
                    self.atendente_name_logado = usuario.nome  # Store the logged-in attendant's name
                    messagebox.showinfo("Login Sucesso", "Você entrou com sucesso!")
                    self.show_atendente_screen()
                else:
                    messagebox.showinfo("Você é um cliente", "Você é um cliente")
            else:
                messagebox.showerror("Login Falha", "Usuário ou senha incorretos")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao tentar logar: {str(e)}")

    def show_atendente_screen(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Configurations for main interface after login
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=0)
        self.frame.grid_columnconfigure(0, weight=1)

        main_frame = tk.Frame(self.frame, bg="#f3f4f6")
        main_frame.grid(row=0, column=0, sticky="nsew", pady=(0, 5))
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

        chamado_list_frame = tk.Frame(main_frame, bg="#f3f4f6")
        chamado_list_frame.grid(row=0, column=0, sticky="nsew", padx=(10, 5))
        tk.Label(chamado_list_frame, text="Chamados", font=self.title_font, bg="#f3f4f6").pack(pady=(0, 10))
        self.chamado_listbox = tk.Listbox(chamado_list_frame, font=self.label_font, bg="#ffffff", bd=0, highlightthickness=0, selectbackground="#ff5c5c", selectforeground="#ffffff")
        self.chamado_listbox.pack(fill="both", expand=True)
        self.populate_chamado_listbox()

        details_frame = tk.Frame(main_frame, bg="#f3f4f6")
        details_frame.grid(row=0, column=1, sticky="nsew", padx=(5, 10))
        tk.Label(details_frame, text="Detalhes do Chamado", font=self.title_font, bg="#f3f4f6").pack(pady=(0, 10))
        self.details_text = tk.Text(details_frame, font=self.label_font, bg="#ffffff", bd=0, highlightthickness=0)
        self.details_text.pack(fill="both", expand=True)

        button_frame = tk.Frame(self.frame, bg="#f3f4f6")
        button_frame.grid(row=1, column=0, sticky="ew")
        self.create_button(button_frame, "Cadastrar Novo Chamado", self.cadastrar_novo_chamado, width=20, bg="#5c85ff").pack(side="left", padx=10)
        self.create_button(button_frame, "Voltar para Login", self.show_login_form, width=20, bg="#f44336").pack(side="left", padx=10)

    def populate_chamado_listbox(self):
        chamados = self.chamado_controller.listar_chamados()
        for chamado in chamados:
            self.chamado_listbox.insert("end", f"Chamado {chamado.id:06d}")
        self.chamado_listbox.bind("<<ListboxSelect>>", self.show_chamado_details)

    def cadastrar_novo_chamado(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        tk.Label(self.frame, text="Cadastro de Novo Chamado", font=self.title_font, bg="#f3f4f6").pack(pady=(0, 20))

        self.entry_nome_cliente = PlaceholderEntry(self.frame, placeholder="Nome do Cliente", font=self.label_font)
        self.entry_nome_cliente.pack(pady=10, fill='x')
        self.entry_email_cliente = PlaceholderEntry(self.frame, placeholder="Email do Cliente", font=self.label_font)
        self.entry_email_cliente.pack(pady=10, fill='x')
        self.entry_empresa_cliente = PlaceholderEntry(self.frame, placeholder="Empresa do Cliente", font=self.label_font)
        self.entry_empresa_cliente.pack(pady=10, fill='x')
        self.entry_telefone_cliente = PlaceholderEntry(self.frame, placeholder="Telefone do Cliente", font=self.label_font)
        self.entry_telefone_cliente.pack(pady=10, fill='x')
        self.entry_titulo = PlaceholderEntry(self.frame, placeholder="Título do Problema", font=self.label_font)
        self.entry_titulo.pack(pady=10, fill='x')
        self.entry_descricao = PlaceholderEntry(self.frame, placeholder="Descrição do Problema", font=self.label_font)
        self.entry_descricao.pack(pady=10, fill='x')

        self.create_button(self.frame, "Salvar Chamado", self.salvar_chamado, width=20, bg="#4CAF50").pack(pady=(20, 10))

    def salvar_chamado(self):
        nome_cliente = self.entry_nome_cliente.get()
        email_cliente = self.entry_email_cliente.get()
        empresa_cliente = self.entry_empresa_cliente.get()
        telefone_cliente = self.entry_telefone_cliente.get()
        titulo = self.entry_titulo.get()
        descricao = self.entry_descricao.get()
        atendente_name = self.atendente_name_logado

        # Create Chamado instance
        chamado = Chamado(
            id=None, titulo=titulo, descricao=descricao, status="Aberto",
            data_abertura=datetime.now(), data_max=datetime.now() + timedelta(days=7), data_fechamento=None,
            nome_cliente=nome_cliente, email_cliente=email_cliente,
            empresa_cliente=empresa_cliente, telefone_cliente=telefone_cliente,
            atendente_name= atendente_name
        )

        # Register the customer if not already registered
        cliente_existente = self.usuario_controller.buscar_usuario_por_email(email_cliente)
        if not cliente_existente:
            novo_cliente = Usuario(None, nome_cliente, email_cliente, "defaultpassword", "cliente")
            self.usuario_controller.criar_usuario(novo_cliente)

        # Create Chamado in the database
        self.chamado_controller.criar_chamado(chamado)

        messagebox.showinfo("Cadastro Efetuado", "Chamado cadastrado com sucesso!")
        self.show_atendente_screen()

    def show_chamado_details(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            chamado_id_str = event.widget.get(index).split()[-1]
            chamado_id = int(chamado_id_str)

            chamado = self.chamado_controller.visualizar_chamado(chamado_id)
            if chamado:
                details = (
                    f"ID: {chamado.id:06d}\n"
                    f"Nome: {chamado.nome_cliente}\n"
                    f"Descrição: {chamado.descricao}\n"
                    f"Email: {chamado.email_cliente}\n"
                    f"Empresa: {chamado.empresa_cliente}\n"
                    f"Telefone: {chamado.telefone_cliente}\n"
                )
                self.details_text.config(state=tk.NORMAL)
                self.details_text.delete(1.0, tk.END)
                self.details_text.insert(tk.END, details)
                self.details_text.config(state=tk.DISABLED)

    def register_user(self):
        nome = self.entry_name.get()
        email = self.entry_email.get()
        senha = self.entry_password.get()
        try:
            novo_usuario = Usuario(None, nome, email, senha, "atendente")
            self.usuario_controller.criar_usuario(novo_usuario)
            messagebox.showinfo("Sucesso", "Atendente cadastrado com sucesso!")
            self.show_login_form()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar atendente: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginScreen(root)
    root.mainloop()