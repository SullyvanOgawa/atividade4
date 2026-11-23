import livro_repositorio  # Centraliza a leitura dos dados.
from modelos import Livro  # Tipo retornado pelas consultas.


class LivroNaoEncontrado(Exception):  # Erro sem dependência de HTTP.
    pass  # O próprio tipo identifica o problema.


def listar_livros() -> list[Livro]:
    return livro_repositorio.listar_todos()  # Delega a leitura ao repositório.


def consultar_livro(livro_id: int) -> Livro:
    livro = livro_repositorio.buscar_por_id(livro_id)  # Consulta.
    if livro is None:  # Aplica o comportamento para livro ausente.
        raise LivroNaoEncontrado(f"Livro {livro_id} não encontrado")
    return livro  # Entrega o livro à API.
