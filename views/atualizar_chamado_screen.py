from models import Cliente, Usuario, Problema, Chamado
from controllers import ClienteController, UsuarioController, ProblemaController, ChamadoController
import tkinter as tk
from tkcalendar import DateEntry
from tkinter import messagebox
from datetime import date, datetime

class AtualizarChamadoScreen:

    def __init__(self, root, id_chamado) -> None:
        self.root = root
        self.chamado_controller = ChamadoController()
        self.usuario_controller = UsuarioController()
        self.problemas_controller = ProblemaController()
        self.id_chamado = id_chamado
        self.chamado = self.chamado_controller.visualizar_chamado(id_chamado)
        self.bold_font = ('Helvetica', 12, 'bold')
        self.title_font = ('Helvetica', 14, 'bold')
        self.root.title('Trabalho de POO - Gerenciar Chamado Screen')
        self.root.geometry('1280x720')
                
        # Cria um frame para os componentes da tela
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        #Titulo da tela
        self.title_label = tk.Label(self.frame, text=f'Chamado {id_chamado:04}', font=self.title_font, anchor='center')
        self.title_label.grid(row=0, column=0, padx=0, pady=5, columnspan=4)

        # Adquiro todos os atendentes
        atendentes = self.usuario_controller.listar_todos()
        nomes_atendentes = [f'{atendente[0]}-{atendente[1]}' for atendente in atendentes]
        # Obtém o ID do atendente associado ao chamado
        id_atendente_chamado = self.chamado[0][5]
        nome_atendente_chamado = ''
        if id_atendente_chamado:
            nome_atendente_chamado = f'{id_atendente_chamado}-{self.usuario_controller.visualizar_usuario(id_atendente_chamado)[0][1]}'  # Corrigi o índice para obter o nome
        
        # Label para o OptionMenu
        self.atendente_chamado_label = tk.Label(self.frame, text='Atendente:', font=self.bold_font, anchor='center')
        self.atendente_chamado_label.grid(row=1, column=0, padx=10, pady=5)
        # Variável para armazenar o atendente selecionado
        self.atendente_selecionado = tk.StringVar(root)
        self.atendente_selecionado.set(nome_atendente_chamado if nome_atendente_chamado else "")
        # Select dos atendentes (OptionMenu)
        self.option_menu = tk.OptionMenu(self.frame, self.atendente_selecionado, *nomes_atendentes)
        self.option_menu.grid(row=1, column=1, padx=10, pady=2, sticky='ew')
        
        self.date_abertura_label = tk.Label(self.frame, text='Data Abertura:', font=self.bold_font, anchor='center')
        self.date_abertura_label.grid(row=2, column=0, padx=2, pady=2, sticky='ew')
        # Criação do DateEntry
        self.date_abertura_input = DateEntry(self.frame, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.date_abertura_input.grid(row=2, column=1, padx=10, pady=5, sticky='ew')

        self.date_fechamento_label = tk.Label(self.frame, text='Data Fechamento:', font=self.bold_font, anchor='center')
        self.date_fechamento_label.grid(row=3, column=0, padx=2, pady=2, sticky='ew')
        # Criação do DateEntry
        self.date_fechamento_input = DateEntry(self.frame, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.date_fechamento_input.grid(row=3, column=1, padx=10, pady=5, sticky='ew')

        problemas = self.problemas_controller.listar_todos()
        problemas.append(())
        nomes_problemas = []
        #nomes_problemas = [f'{problema[0]}-{problema[1]}' for problema in problemas]
        for problema in problemas:
            if len(problema) != 0:
                nomes_problemas.append(f'{problema[0]}-{problema[1]}')
            else:
                nomes_problemas.append('')
        # Obtém o ID do problema associado ao chamado
        id_problema_chamado = self.chamado[0][3]
        nome_problema_chamado = ''
        if id_problema_chamado:
            nome_problema_chamado = f'{id_problema_chamado}-{self.problemas_controller.visualizar_problema(id_problema_chamado)[0][1]}'  # Corrigi o índice para obter o nome
        
        self.problema_chamado_label = tk.Label(self.frame, text='Problema:', font=self.bold_font, anchor='center')
        self.problema_chamado_label.grid(row=4, column=0, padx=10, pady=5)
        # Variável para armazenar o atendente selecionado
        self.problema_selecionado = tk.StringVar(root)
        self.problema_selecionado.set(nome_problema_chamado if nome_problema_chamado else "")
        # Select dos atendentes (OptionMenu)
        self.option_menu_problemas = tk.OptionMenu(self.frame, self.problema_selecionado, *nomes_problemas)
        self.option_menu_problemas.grid(row=4, column=1, padx=10, pady=2, sticky='ew')

        self.tipos_status = ['Aberto', 'Em Andamento', 'Fechado']
        self.status_chamado_label = tk.Label(self.frame, text='Status:', font=self.bold_font, anchor='center')
        self.status_chamado_label.grid(row=5, column=0, padx=10, pady=5)
        # Variável para armazenar o atendente selecionado
        self.status_selecionado = tk.StringVar(root)
        self.status_selecionado.set(self.tipos_status[0])
        # Select dos atendentes (OptionMenu)
        self.status_menu_problemas = tk.OptionMenu(self.frame, self.status_selecionado, *self.tipos_status)
        self.status_menu_problemas.grid(row=5, column=1, padx=10, pady=2, sticky='ew')

        self.titulo_label = tk.Label(self.frame, text='Titulo Problema:', font=self.bold_font, anchor='w')
        self.titulo_label.grid(row=6, column=0, padx=10, pady=2, sticky='w')
        self.titulo_input = tk.Entry(self.frame, width=30)
        self.titulo_input.grid(row=6, column=1, padx=10, pady=2, sticky='ew')

        self.text_area_label = tk.Label(self.frame, text='Descrição:', font=self.bold_font, anchor='center')
        self.text_area_label.grid(row=7, column=0, padx=10, pady=5)
        
        # Criação da Área de Texto
        self.text_area_descricao = tk.Text(self.frame, wrap=tk.WORD, width=40, height=10)
        self.text_area_descricao.grid(row=8,column=0, columnspan=2, padx=10, pady=10)

        self.atualizar_chamado_button = tk.Button(self.frame, text="Atualizar chamado", font=self.bold_font, width=15, command=self.atualizar_chamado)
        self.atualizar_chamado_button.grid(row=9, column=0, padx=20, pady=10)

        self.voltar_button = tk.Button(self.frame, text="Voltar", font=self.bold_font, width=15, command=self.voltar_atendente)
        self.voltar_button.grid(row=9, column=1, padx=20, pady=10)

    def atualizar_chamado(self) -> None:
        chamado_obj = Chamado()
        chamado_obj.id = self.id_chamado
        chamado_obj.descricao = self.text_area_descricao.get("1.0", tk.END).strip()
        if(self.status_selecionado.get() == 'Aberto'):
            chamado_obj.data_fechamento = None
            chamado_obj.id_usuario = self.atendente_selecionado.get().split('-')[0]
        
        if(self.status_selecionado.get() == 'Em Andamento'):
            chamado_obj.data_fechamento = None
            if self.atendente_selecionado.get() != '' and self.atendente_selecionado.get() != None:
                chamado_obj.id_usuario = self.atendente_selecionado.get().split('-')[0]
        
        if(self.status_selecionado.get() == 'Fechado'):
            chamado_obj.data_fechamento = self.date_fechamento_input.get()
            if self.atendente_selecionado.get() != '' and self.atendente_selecionado.get() != None:
                chamado_obj.id_usuario = self.atendente_selecionado.get().split('-')[0]
        
        chamado_obj.data_abertura = self.date_abertura_input.get_date()
        
        #TODO falta data-max e status
        if self.problema_selecionado.get() != '' and self.problema_selecionado.get() != None:
            chamado_obj.id_categoria = self.problema_selecionado.get().split('-')[0]
        chamado_obj.status = self.status_selecionado.get()
        chamado_obj.titulo = self.titulo_input.get()
        self.chamado_controller.alterar_chamado(chamado_obj)
        messagebox.showinfo('Atualizar', 'Chamado atualizado com sucesso!')
        self.voltar_atendente()
        
    def voltar_atendente(self) -> None:
        from .atendente_screen import AtendenteScreen
        self.exit()
        new_root = tk.Tk()
        atendente_screen_app = AtendenteScreen(new_root)
        new_root.mainloop()

    def exit(self) -> None:
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AtualizarChamadoScreen(root)
    root.mainloop()
