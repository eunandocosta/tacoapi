Claro, aqui está a atualização do README para incluir a existência do `Dockerfile` e do `docker-compose.yml`.

# Alimento API

Esta aplicação é uma API RESTful construída com Flask para gerenciar informações nutricionais de alimentos. A API permite adicionar, listar e buscar alimentos em um banco de dados. A aplicação utiliza SQLAlchemy para interação com o banco de dados.

## Estrutura do Projeto

- `app.py`: Contém as rotas e lógica principal da API.
- `models/alimento.py`: Define o modelo Alimento.
- `database.py`: Configura a conexão com o banco de dados.
- `Dockerfile`: Define a imagem Docker para a aplicação.
- `docker-compose.yml`: Define os serviços Docker para a aplicação.
- `README.md`: Documentação do projeto.

## Requisitos

- Python 3.x
- Flask
- SQLAlchemy
- Docker (opcional)
- Docker Compose (opcional)

## Instalação

### Manualmente

1. Clone o repositório:

```bash
git clone https://github.com/usuario/alimento-api.git
cd alimento-api
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Configure o banco de dados em `database.py`:

```python
DATABASE_URL = "sqlite:///./test.db"  # Exemplo de banco de dados SQLite
```

5. Crie o banco de dados:

```bash
python
>>> from database import Base, engine
>>> Base.metadata.create_all(bind=engine)
>>> exit()
```

### Usando Docker

1. Clone o repositório:

```bash
git clone https://github.com/usuario/alimento-api.git
cd alimento-api
```

2. Construa e inicie os containers Docker:

```bash
docker-compose up --build
```

A API estará disponível em `http://127.0.0.1:5000`.

## Uso

### Iniciar o Servidor

Inicie o servidor Flask:

```bash
flask run
```

A API estará disponível em `http://127.0.0.1:5000`.

### Endpoints

#### Adicionar Alimento

Adiciona um novo alimento ao banco de dados.

- **URL**: `/add_alimento`
- **Método**: `POST`
- **Corpo da Requisição**: JSON

```json
{
  "id": 1,
  "Nome": "Maçã",
  "Umidade": 85.6,
  "Energia_kcal": 52,
  "Energia_kj": 218,
  "Proteina": 0.26,
  "Lipideos": 0.17,
  "Colesterol": 0,
  "Carboidrato": 13.81,
  "Fibra_Alimentar": 2.4,
  "Cinzas": 0.19,
  "Calcio": 6,
  "Magnesio": 5
}
```

- **Resposta de Sucesso**: `201 Created`
- **Resposta de Erro**: `409 Conflict` se o alimento já existe.

#### Listar Alimentos

Retorna uma lista de todos os alimentos no banco de dados.

- **URL**: `/alimentos`
- **Método**: `GET`
- **Resposta de Sucesso**: `200 OK`

#### Buscar Alimentos

Busca alimentos pelo nome.

- **URL**: `/search_alimentos`
- **Método**: `GET`
- **Parâmetro de Consulta**: `query` (string)

- **Exemplo**:

  `GET /search_alimentos?query=Maçã`

- **Resposta de Sucesso**: `200 OK`

## Modelo de Dados

O modelo de dados `Alimento` é definido em `models/alimento.py` e possui os seguintes campos:

- `id` (Integer): Identificador único do alimento.
- `Nome` (String): Nome do alimento.
- `Umidade` (Float): Percentual de umidade do alimento.
- `Energia_kcal` (Float): Energia em quilocalorias.
- `Energia_kj` (Float): Energia em quilojoules.
- `Proteina` (Float): Quantidade de proteína em gramas.
- `Lipideos` (Float): Quantidade de lipídeos em gramas.
- `Colesterol` (Float): Quantidade de colesterol em miligramas.
- `Carboidrato` (Float): Quantidade de carboidratos em gramas.
- `Fibra_Alimentar` (Float): Quantidade de fibra alimentar em gramas.
- `Cinzas` (Float): Quantidade de cinzas em gramas.
- `Calcio` (Float): Quantidade de cálcio em miligramas.
- `Magnesio` (Float): Quantidade de magnésio em miligramas.

## Logging

A aplicação utiliza o módulo `logging` para registrar informações sobre as operações executadas, como adição de alimentos e erros.

## Tratamento de Erros

A aplicação trata erros de integridade (como duplicação de ID) e retorna mensagens de erro apropriadas ao cliente.

## Docker

A aplicação inclui suporte para Docker, permitindo fácil configuração e implantação.

### Dockerfile

O `Dockerfile` define a imagem Docker para a aplicação.

### docker-compose.yml

O `docker-compose.yml` define os serviços Docker para a aplicação, facilitando a execução em ambientes de desenvolvimento e produção.

### Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

### Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo `LICENSE` para mais detalhes.
