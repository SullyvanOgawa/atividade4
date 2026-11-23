from typing import Annotated  # Associa o tipo à validação do parâmetro.

from fastapi import FastAPI, HTTPException, Path  # Recursos HTTP.

from modelos import Livro  # Contrato da resposta.
from servico_livros import LivroNaoEncontrado, consultar_livro, listar_livros

app = FastAPI(title="Serviço de Biblioteca")  # Aplicação da biblioteca.


@app.get("/livros", response_model=list[Livro])  # Listagem do acervo.
def obter_livros() -> list[Livro]:
    return listar_livros()  # Sempre 200; lista vazia se não houver livros.


@app.get("/livros/{livro_id}", response_model=Livro)  # Consulta por id.
def obter_livro(
    livro_id: Annotated[int, Path(gt=0)],  # Zero, negativo ou texto geram 422.
) -> Livro:
    try:  # A API traduz o resultado da operação para HTTP.
        return consultar_livro(livro_id)  # Delega a consulta.
    except LivroNaoEncontrado as erro:  # Trata apenas erro esperado.
        raise HTTPException(
            status_code=404,  # Recurso solicitado não existe.
            detail="Livro não encontrado",  # Mensagem pública.
        ) from erro  # Preserva a causa para diagnóstico.
