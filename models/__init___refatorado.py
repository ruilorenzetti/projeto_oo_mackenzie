from dataclasses import dataclass

@dataclass
class Cliente:
    nome: str
    email: str
    empresa: str
    telefone: str

@dataclass
class Usuario:
    nome: str
    email: str
    senha: str
    cargo: str

@dataclass
class Problema:
    descricao: str
    sla: str

@dataclass
class Chamado:
    titulo: str
    descricao: str
    status: str
    data_abertura: str
    data_max: str
    data_fechamento: str
