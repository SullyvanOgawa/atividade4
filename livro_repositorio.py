from modelos import Livro  # Modelo usado para representar o acervo.

# Acervo didático em memória; somente este módulo acessa a coleção.
# O dicionário usa o id como chave para facilitar a busca direta.
_LIVROS = {
    1: Livro(id=1, titulo="Dom Casmurro", autor="Machado de Assis", ano_publicacao=1899, disponivel=True),
    2: Livro(id=2, titulo="O Cortiço", autor="Aluísio Azevedo", ano_publicacao=1890, disponivel=False),
    3: Livro(id=3, titulo="Vidas Secas", autor="Graciliano Ramos", ano_publicacao=1938, disponivel=True),
    4: Livro(id=4, titulo="Capitães da Areia", autor="Jorge Amado", ano_publicacao=1937, disponivel=True),
    5: Livro(id=5, titulo="A Hora da Estrela", autor="Clarice Lispector", ano_publicacao=1977, disponivel=False),
}


def listar_todos() -> list[Livro]:
    # Retorna cópias para que o chamador não altere os livros guardados.
    # Se estiver vazio, o resultado é uma lista vazia.
    return [livro.model_copy() for livro in _LIVROS.values()]


def buscar_por_id(livro_id: int) -> Livro | None:
    livro = _LIVROS.get(livro_id)  # Se retornar None, isso indica ausência.
    # A cópia impede que o chamador altere o objeto guardado no acervo.
    return livro.model_copy() if livro is not None else None
