from models import Cliente, Usuario, Problema, Chamado
from daos.TIPO_ESTADO_CHAMADO import TIPO_ESTADO_CHAMADO
from controllers import ClienteController, UsuarioController, ProblemaController, ChamadoController
import tkinter as tk
from tkinter import messagebox

class AtendenteScreen:

    def __init__(self, root) -> None:
        self.root = root
        self.selected_id_chamado = None
        self.bold_font = ('Helvetica', 12, 'bold')
        self.title_font = ('Helvetica', 14, 'bold')
        self.cliente_controller = ClienteController()
        self.chamado_controller = ChamadoController()
        self.usuario_controller = UsuarioController()
        self.problema_controller = ProblemaController()
        self.root.title('Trabalho de POO - Tela Atendente')
        self.root.geometry('1280x720')
        
        # Cria um frame para os componentes da tela
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        #Titulo da tela
        self.title_label = tk.Label(self.frame, text='Tela de Atendentes', font=self.title_font, anchor='center')
        self.title_label.grid(row=0, column=0, padx=0, pady=5, columnspan=4)

        self.filtro_label = tk.Label(self.frame, text='Filtro:', font=self.title_font, anchor='w')
        self.filtro_label.grid(row=2, column=0, padx=0, pady=5, sticky='w')

        tipos_filtros = ['Todos', 'Aberto', 'Fechado', 'Em andamento']
        
        self.filtro_option = tk.StringVar(root)
        self.filtro_option.set(tipos_filtros[0])
        # Select dos atendentes (OptionMenu)
        self.filtro_combobox = tk.OptionMenu(self.frame, self.filtro_option, *tipos_filtros)
        self.filtro_combobox.grid(row=2, column=1, pady=5, sticky='ew')
        self.filtro_option.trace("w", self.on_option_menu_state_change)

        #Subtitulo Lista de chamados
        self.title_label = tk.Label(self.frame, text='Lista de chamados:', font=self.title_font, anchor='e')
        self.title_label.grid(row=1, column=0, padx=0, pady=5, columnspan=2)

        # Lista de Chamados
        self.chamados_listbox = tk.Listbox(self.frame, font=self.bold_font, width=50, height=20)
        self.chamados_listbox.grid(row=3, column=0, padx=20, pady=20, columnspan=2)

        #Listo todos os chamados na lista de chamados
        self.listar_chamados()
        
        #Caso cliquem em um item da list box
        self.chamados_listbox.bind("<<ListboxSelect>>", self.listar_chamado)

        #Subtitulo Detalhes do chamado
        self.title_label = tk.Label(self.frame, text='Detalhes do chamado', font=self.title_font, anchor='e')
        self.title_label.grid(row=1, column=2, padx=0, pady=5, columnspan=2)

        # Detalhes do Chamado
        self.detalhes_list = tk.Listbox(self.frame, font=self.bold_font, width=50, height=20)
        self.detalhes_list.grid(row=3, column=2, padx=20, pady=20, columnspan=2)
        
        # Botões de Ação
        self.criar_cliente_button = tk.Button(self.frame, text="Criar cliente", font=self.bold_font, width=15, command=self.criar_cliente)
        self.criar_cliente_button.grid(row=4, column=0, padx=20, pady=10)

        self.excluir_usuario_button = tk.Button(self.frame, text="Excluir cliente", font=self.bold_font, width=15, command=self.excluir_cliente)
        self.excluir_usuario_button.grid(row=4, column=1, padx=20, pady=10)

        self.atualizar_chamado_button = tk.Button(self.frame, text="Atualizar chamado", font=self.bold_font, width=15, command=self.atualizar_chamado)
        self.atualizar_chamado_button.grid(row=4, column=2, padx=20, pady=10)

        self.voltar_button = tk.Button(self.frame, text="Voltar", font=self.bold_font, width=15, command=self.voltar_login)
        self.voltar_button.grid(row=4, column=3, padx=20, pady=10)
        
        self.cadastrar_problema_button = tk.Button(self.frame, text="Cadastrar Problema", font=self.bold_font, width=15, command=self.open_cadastro_problem)
        self.cadastrar_problema_button.grid(row=5, column=0, padx=20, pady=10)

    def open_cadastro_problem(self) -> None:
        from .cadastro_problema_screen import CadastroProblemaScreen
        self.exit()
        new_root = tk.Tk()
        cliente_cadastro_app = CadastroProblemaScreen(new_root)
        new_root.mainloop()

    def criar_cliente(self) -> None:
        from .cliente_cadastro_screen import ClienteCadastroScreen
        self.exit()
        new_root = tk.Tk()
        cliente_cadastro_app = ClienteCadastroScreen(new_root)
        new_root.mainloop()

    def excluir_cliente(self) -> None:
        from .excluir_cliente_screen import ExcluirClienteScreen
        self.exit()
        new_root = tk.Tk()
        excluir_cliente_app = ExcluirClienteScreen(new_root)
        new_root.mainloop()
        
    def atualizar_chamado(self) -> None:
        from .atualizar_chamado_screen import AtualizarChamadoScreen
        if self.selected_id_chamado:
            self.exit()
            new_root = tk.Tk()
            gerenciar_chamado_app = AtualizarChamadoScreen(new_root, id_chamado=self.selected_id_chamado)
            new_root.mainloop()
        else:
            messagebox.showerror('Erro', 'Selecione primeiro um dos chamados.')
            return 

    def listar_chamados(self) -> None:
        chamados = self.chamado_controller.listar_todos()
        for chamado in chamados:
            self.chamados_listbox.insert(tk.END, f'ID: {chamado[0]:04}')

    def listar_chamado(self, event) -> None:
        # Limpa a listbox de detalhes
        self.detalhes_list.delete(0, tk.END)
        # Obtém o widget que gerou o evento e o índice do item selecionado
        widget = event.widget
        index_selecionado = widget.curselection()
        if index_selecionado:
            index = index_selecionado[0]
            valor = widget.get(index)
            # Extrai o ID do chamado e remove zeros iniciais
            id_chamado = int(valor.replace("ID: ", ""))
            self.selected_id_chamado = id_chamado
            # Busca os detalhes do chamado
            selected_chamado = self.chamado_controller.visualizar_chamado(id_chamado)
            id_atendente_chamado = selected_chamado[0][5]
            
            nome_atendente = ''
            if id_atendente_chamado:
                nome_atendente_tupla = self.usuario_controller.visualizar_usuario(id_atendente_chamado)
                if(nome_atendente_tupla):
                    nome_atendente = self.usuario_controller.visualizar_usuario(id_atendente_chamado)[0][1]

            if selected_chamado:
                # Insere os detalhes do chamado na listbox
                self.detalhes_list.insert(tk.END, f'ID: {selected_chamado[0][0]:04}')
                self.detalhes_list.insert(tk.END, f'Titulo: {selected_chamado[0][1]}')
                self.detalhes_list.insert(tk.END, f'Descricao: {selected_chamado[0][2]}')
                self.detalhes_list.insert(tk.END, f'Categoria: {selected_chamado[0][10]}')
                self.detalhes_list.insert(tk.END, f'SLA: {selected_chamado[0][11]}')
                self.detalhes_list.insert(tk.END, f'Atendente: {nome_atendente}')
                self.detalhes_list.insert(tk.END, f'Status: {selected_chamado[0][6]}')
                self.detalhes_list.insert(tk.END, f'Data Abertura: {selected_chamado[0][7]}')
                self.detalhes_list.insert(tk.END, f'Data Max: {selected_chamado[0][8]}')
                self.detalhes_list.insert(tk.END, f'Fechamento: {selected_chamado[0][9]}')
            else:
                messagebox.showerror("Erro", "Não foi possível encontrar os detalhes do chamado.")
    
    def on_option_menu_state_change(self, *args) -> None:
        option_selected_on_menu = self.filtro_option.get()
        if option_selected_on_menu == 'Todos':
            self.chamados_listbox.delete(0, tk.END)
            chamados = self.chamado_controller.listar_todos_por_status(TIPO_ESTADO_CHAMADO.TODOS)
            print(chamados)
            for chamado in chamados:
                self.chamados_listbox.insert(tk.END, f'ID: {chamado[0]:04}')
        if option_selected_on_menu == 'Aberto':
            self.chamados_listbox.delete(0, tk.END)
            chamados = self.chamado_controller.listar_todos_por_status(TIPO_ESTADO_CHAMADO.ABERTO)
            for chamado in chamados:
                self.chamados_listbox.insert(tk.END, f'ID: {chamado[0]:04}')
        if option_selected_on_menu == 'Fechado':
            self.chamados_listbox.delete(0, tk.END)
            chamados = self.chamado_controller.listar_todos_por_status(TIPO_ESTADO_CHAMADO.FECHADO)
            for chamado in chamados:
                self.chamados_listbox.insert(tk.END, f'ID: {chamado[0]:04}')
        if option_selected_on_menu == 'Em andamento':
            self.chamados_listbox.delete(0, tk.END)
            chamados = self.chamado_controller.listar_todos_por_status(TIPO_ESTADO_CHAMADO.EM_ANDAMENTO)
            for chamado in chamados:
                self.chamados_listbox.insert(tk.END, f'ID: {chamado[0]:04}')
        
    def voltar_login(self) -> None:
        from .login_screen import LoginScreen
        self.exit()
        new_root = tk.Tk()
        login_screen_app = LoginScreen(new_root)
        new_root.mainloop()

    def open_excluir_atendente_screen(self) -> None:
        pass

    def exit(self) -> None:
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AtendenteScreen(root)
    root.mainloop()
