from models import Cliente, Usuario, Problema, Chamado
from controllers import ClienteController, UsuarioController, ProblemaController, ChamadoController
import tkinter as tk
from tkinter import messagebox

class ClienteScreen:

    def __init__(self, root) -> None:
        self.root = root
        self.selected_id_chamado = None
        self.bold_font = ('Helvetica', 12, 'bold')
        self.title_font = ('Helvetica', 14, 'bold')
        self.cliente_controller = ClienteController()
        self.chamado_controller = ChamadoController()
        self.usuario_controller = UsuarioController()
        self.problema_controller = ProblemaController()
        self.root.title('Trabalho de POO - Tela Cliente')
        self.root.geometry('1280x720')
        
        # Cria um frame para os componentes da tela
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        


if __name__ == "__main__":
    root = tk.Tk()
    app = ClienteScreen(root)
    root.mainloop()