# TACOAPI - API para Gerenciamento de Alimentos

## Descrição

TACOAPI é uma API desenvolvida para gerenciar dados de alimentos, permitindo adicionar, buscar e manipular informações nutricionais. A API utiliza Flask para o backend, SQLAlchemy para ORM e MySQL como banco de dados. Toda a aplicação é containerizada usando Docker e Docker Compose.

## Tecnologias Utilizadas

- **Flask**: Framework de micro serviços para construção de APIs em Python.
- **SQLAlchemy**: ORM para interação com o banco de dados.
- **MySQL**: Banco de dados relacional.
- **Docker**: Para containerização da aplicação.
- **Docker Compose**: Para orquestração dos containers.
- **Pandas**: Biblioteca de manipulação de dados para Python.

## Estrutura do Projeto

- `app.py`: Arquivo principal da aplicação Flask.
- `config.py`: Configurações da aplicação.
- `database.py`: Configuração do banco de dados e inicialização do SQLAlchemy.
- `models`: Contém os modelos do SQLAlchemy.
- `routes`: Contém as rotas da API.
- `Dockerfile`: Arquivo para construir a imagem Docker da aplicação.
- `Dockerfile.script`: Arquivo para construir a imagem Docker do script de importação.
- `docker-compose.yml`: Arquivo de configuração do Docker Compose.
- `requirements.txt`: Arquivo com as dependências do projeto.
- `script_taco.py`: Script para importar dados do CSV para o banco de dados.
- `wait-for-it.sh`: Script para garantir que o MySQL esteja disponível antes de iniciar a aplicação Flask.
- `taco-db-nutrientes.csv`: Arquivo CSV com os dados dos alimentos.

## Instalação

### Pré-requisitos

- Docker e Docker Compose instalados na sua máquina.

### Passos para Configuração

1. Clone o repositório:

    ```bash
    git clone https://github.com/eunandocosta/tacoapi.git
    cd tacoapi
    ```

2. Configure as variáveis de ambiente no arquivo `docker-compose.yml` se necessário.

3. Inicie os containers Docker:

    ```bash
    docker-compose up --build
    ```

4. A aplicação estará disponível em `http://localhost:5000`.

## Endpoints

### Adicionar Alimento

- **URL**: `/add_alimento`
- **Método**: `POST`
- **Descrição**: Adiciona um novo alimento.
- **Corpo da Requisição**:
    ```json
    {
        "id": 1,
        "Nome": "Banana",
        "Umidade": 74.91,
        "Energia_kcal": 89,
        "Energia_kj": 372,
        "Proteina": 1.09,
        "Lipideos": 0.33,
        "Colesterol": 0,
        "Carboidrato": 22.84,
        "Fibra_Alimentar": 2.6,
        "Cinzas": 0.82,
        "Calcio": 5,
        "Magnesio": 27
    }
    ```

### Buscar Alimentos

- **URL**: `/alimentos`
- **Método**: `GET`
- **Descrição**: Retorna uma lista de todos os alimentos.

### Buscar Alimentos por Nome

- **URL**: `/search_alimentos`
- **Método**: `GET`
- **Descrição**: Busca alimentos pelo nome.
- **Parâmetros**:
    - `query`: Nome ou parte do nome do alimento a ser buscado.

## Contribuição

1. Faça um fork do repositório.
2. Crie uma nova branch com sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`).
4. Push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.
