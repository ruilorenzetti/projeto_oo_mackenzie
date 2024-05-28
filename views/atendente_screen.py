from models import Cliente, Usuario, Problema, Chamado
from controllers import ClienteController, UsuarioController, ProblemaController, ChamadoController
import tkinter as tk
from tkinter import messagebox

class AtendenteScreen:

    def __init__(self, root) -> None:
        self.root = root
        self.bold_font = ('Helvetica', 12, 'bold')
        self.root.title('Trabalho de POO - Tela Atendente')
        self.root.geometry('1280x720')
        
        # Cria um frame para os componentes de login
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=100)

if __name__ == "__main__":
    root = tk.Tk()
    app = AtendenteScreen(root)
    root.mainloop()