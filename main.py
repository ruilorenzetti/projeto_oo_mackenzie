# main.py
from controllers import ClienteController, UsuarioController, ProblemaController, ChamadoController
from models import Cliente, Usuario, Problema, Chamado

# Exemplo de uso
if __name__ == "__main__":
    cliente_controller = ClienteController()
    usuario_controller = UsuarioController()
    problema_controller = ProblemaController()
    chamado_controller = ChamadoController()

    # Criação de um cliente
    novo_cliente = Cliente(nome="João", email="joao@example.com", empresa="Empresa X", telefone="12345678")
    cliente_controller.criar_cliente(novo_cliente)

    # Visualização de um cliente
    cliente = cliente_controller.visualizar_cliente(1)
    print(cliente)

    # Criação de um usuário
    novo_usuario = Usuario(nome="Maria", email="maria@example.com", senha="senha123", cargo="Atendente")
    usuario_controller.criar_usuario(novo_usuario)

    # Visualização de um usuário
    usuario = usuario_controller.visualizar_usuario(1)
    print(usuario)

    # Criação de um problema
    novo_problema = Problema(descricao="Problema de rede", sla="24h")
    problema_controller.criar_problema(novo_problema)

    # Visualização de um problema
    problema = problema_controller.visualizar_problema(1)
    print(problema)

    # Criação de um chamado
    novo_chamado = Chamado(titulo="Chamado 1", descricao="Descrição do chamado", status="Aberto", data_abertura="2023-05-25", data_max="2023-05-30", data_fechamento="")
    chamado_controller.criar_chamado(novo_chamado)

    # Visualização de um chamado
    chamado = chamado_controller.visualizar_chamado(1)
    print(chamado)
