# API de Consulta ao Acervo da Biblioteca

API desenvolvida em Python com FastAPI para consultar os livros de uma biblioteca. Os dados ficam armazenados em memória.

## Estrutura do projeto

| Arquivo | Responsabilidade |
|---|---|
| `modelos.py` | Modelo `Livro` com as regras de validação dos campos |
| `livro_repositorio.py` | Acervo em memória; único módulo que acessa a coleção de livros |
| `servico_livros.py` | Regras da consulta e exceção `LivroNaoEncontrado` |
| `livros.py` | Rotas da API e conversão de `LivroNaoEncontrado` em HTTP 404 |

## Como executar

1. Criar e ativar o ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

No Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Instalar as dependências:

```bash
pip install -r requirements.txt
```

3. Iniciar o servidor:

```bash
fastapi dev livros.py
```

4. Acessar a documentação interativa em http://127.0.0.1:8000/docs

## Rotas

| Método | Rota | Descrição |
|---|---|---|
| GET | `/livros` | Retorna a lista de livros cadastrados |
| GET | `/livros/{livro_id}` | Retorna o livro correspondente ao identificador |

## Respostas da consulta por identificador

| Código | Situação | Exemplo |
|---|---|---|
| 200 | Livro encontrado | `/livros/1` |
| 404 | Identificador válido, mas sem livro correspondente | `/livros/99` |
| 422 | Identificador inválido (zero, negativo ou texto) | `/livros/0`, `/livros/-1`, `/livros/abc` |

A listagem `/livros` sempre retorna 200 com uma lista JSON. Se o acervo estiver vazio, retorna `[]`.

## Exemplo de resposta

`GET /livros/1`

```json
{
  "id": 1,
  "titulo": "Dom Casmurro",
  "autor": "Machado de Assis",
  "ano_publicacao": 1899,
  "disponivel": true
}
```
