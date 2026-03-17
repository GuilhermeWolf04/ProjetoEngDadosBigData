# Projeto - ETL de Universidades por Pais

## Integrantes do grupo
Preencha com os nomes completos (maximo de 3 pessoas):

1. Nome completo do integrante 1
2. Nome completo do integrante 2
3. Nome completo do integrante 3

## Objetivo
Consultar a Universities API por pais, extrair o JSON retornado e salvar os dados em um banco SQLite.

Cada pais informado gera uma tabela no banco `universities.db`.

## Estrutura do projeto

```text
ProjetoEngDadosBigData/
|-- main.py
|-- pyproject.toml
|-- requirements.txt
|-- requirements-dev.txt
`-- src/
    |-- __init__.py
    |-- extract.py
    `-- load.py
```

## Requisitos
- Python 3.8+
- pip

## Configuracao do ambiente
1. Criar ambiente virtual:
   ```bash
   python -m venv .venv
   ```
2. Ativar ambiente virtual:
   ```bash
   .venv\Scripts\activate
   ```
3. Instalar dependencias:
   ```bash
   pip install -r requirements-dev.txt
   ```

## Como executar
Execucao padrao:

```bash
python main.py
```

Para usar outro pais no terminal Python:

```python
from main import salvar_universidades_por_pais
salvar_universidades_por_pais("Canada")
```

## Boas praticas aplicadas
- Docstrings e tipagem nos metodos.
- Separacao de responsabilidades com POO:
  - `Extract`: consumo e desserializacao da API.
  - `Load`: criacao de tabela e carga no SQLite.
- Formato de codigo padronizado com Black.

## Formatar com Black

```bash
black .
```

## Diferencial
Criar e publicar repositorio no GitHub para armazenar o projeto.

Importante: nao subir pasta de ambiente virtual (`venv`, `.venv`).
