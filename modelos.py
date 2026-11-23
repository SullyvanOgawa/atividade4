from pydantic import BaseModel, Field  # Modelos e regras de validação.


class Livro(BaseModel):  # Contrato dos dados de um livro.
    id: int = Field(gt=0, strict=True)  # Identificador inteiro e positivo.
    titulo: str = Field(min_length=1)  # Título obrigatório e não vazio.
    autor: str = Field(min_length=1)  # Autor obrigatório e não vazio.
    ano_publicacao: int = Field(gt=0, strict=True)  # Ano inteiro e positivo.
    disponivel: bool  # Indica se o livro pode ser emprestado.
