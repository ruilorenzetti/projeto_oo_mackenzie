from models import Cliente, Usuario, Problema, Chamado
from controllers import ClienteController, UsuarioController, ProblemaController, ChamadoController
import tkinter as tk
from tkinter import messagebox

class ExcluirAtendenteScreen:

    def __init__(self, root) -> None:
        self.root = root
        self.bold_font = ('Helvetica', 12, 'bold')
        self.title_font = ('Helvetica', 14, 'bold')
        self.cliente_controller = ClienteController()
        self.bold_font = ('Helvetica', 12, 'bold')
        self.root.title('Trabalho de POO - Tela para Excluir Cliente')
        self.root.geometry('1280x720')

        # Cria um frame para os componentes da tela
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        #Titulo da tela
        self.title_label = tk.Label(self.frame, text='Tela de Excluir Cliente', font=self.title_font, anchor='center')
        self.title_label.grid(row=0, column=0, padx=0, pady=5, columnspan=2)

        #Campo de entrada para o usuario
        self.email_user_label = tk.Label(self.frame, text='Email do usuario:', font=self.bold_font, anchor='w')
        self.email_user_label.grid(row=1, column=0, padx=0, pady=2)
        self.email_user_input = tk.Entry(self.frame, width=30)
        self.email_user_input.grid(row=1, column=1, padx=2, pady=2)

        #Botão de Excluir
        self.excluir_button = tk.Button(self.frame, text='Excluir', command=self.excluir_usuario, bg='green', fg='white')
        self.excluir_button.grid(row=2, column=0, sticky='ew', padx=2) #Stick = expandir de leste a oeste

        #Botão de voltar
        self.voltar_button = tk.Button(self.frame, text='Voltar', command=self.voltar_atendente_screen, bg='blue', fg='white')
        self.voltar_button.grid(row=2, column=1, sticky='ew', padx=2) #Stick = expandir de leste a oeste

    def excluir_usuario(self) -> None:
        user_email = self.email_user_input.get()
        user = self.valida_cliente(user_email=user_email)
        
        if user:
            confirm = messagebox.askyesno("Confirmar Exclusão", f"Tem certeza que deseja excluir o cliente: {user[1]} que possui o email: {user[2]}?")
            if(confirm):
                self.cliente_controller.excluir_cliente(user[0])
                messagebox.showinfo("Sucesso", f"Cliente {user[1]} excluído com sucesso.")
                self.voltar_atendente_screen()
        else:
            messagebox.showerror("Erro", "Não foi possível encontrar o cliente. Verifique o email e tente novamente.")

    def valida_cliente(self, user_email) -> tuple | None:

        if not user_email:
            messagebox.showerror("Erro", "Por favor, insira um email.")
            return None

        if user_email != '':
            clientes_banco = self.cliente_controller.listar_todos()
            for cliente in clientes_banco:
                # Assume-se que o email está no índice 2
                if cliente[2] == user_email :
                    return cliente  # Retorna o cliente
            return None  # Retorna None se nenhum cliente válido for encontrado

    
    def voltar_atendente_screen(self) -> None:
        from .atendente_screen import AtendenteScreen
        self.exit()
        new_root = tk.Tk()
        excluir_cliente_app = AtendenteScreen(new_root)
        new_root.mainloop()

    def exit(self) -> None:
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ExcluirAtendenteScreen(root)
    root.mainloop()
