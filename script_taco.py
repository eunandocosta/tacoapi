import pandas as pd
import requests
import logging
import os
import numpy as np

logging.basicConfig(level=logging.DEBUG)

# Caminho do arquivo CSV
csv_file_path = 'taco-db-nutrientes.csv'
# URL da API
api_url = 'http://192.168.1.15:5000/add_alimento'

# Verifica se o arquivo existe no caminho fornecido
if not os.path.exists(csv_file_path):
    logging.error(f"Arquivo {csv_file_path} não encontrado.")
    exit()

# Ler o CSV ignorando a segunda linha (unidades de medida) e lidando com erros
try:
    df = pd.read_csv(csv_file_path, skiprows=[1], delimiter=',', on_bad_lines='skip')
except pd.errors.ParserError as e:
    logging.error(f"Erro ao ler o arquivo CSV: {e}")
    exit()

# Remover espaços extras dos nomes das colunas
df.columns = df.columns.str.strip() 

# Remover a coluna 'Unnamed: 13' se existir
if 'Unnamed: 13' in df.columns:
    df.drop(columns=['Unnamed: 13'], inplace=True)

# Remover espaços extras dos valores nas colunas de string
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Imprimir as colunas do DataFrame para verificação
print(df.columns)

# Função para verificar valores ausentes ou inválidos
def is_valid_value(value):
    if pd.isna(value) or value in ['NA', 'Tr', '*']:
        return False
    return True

# Função para converter valores para float, tratando possíveis erros
def convert_to_float(value):
    try:
        float_val = float(value)
        if np.isinf(float_val) or np.isnan(float_val):
            return 0.0
        return float_val
    except ValueError:
        return 0.0

# Inserir dados no banco de dados
for index, row in df.iterrows():
    # Verifica se a linha é válida, ou seja, contém todos os campos necessários
    if not is_valid_value(row.get('id')) or not is_valid_value(row.get('Nome')):
        logging.warning(f"Linha ignorada devido a dados ausentes: {row}")
        continue

    # Substituir valores inválidos por zeros ou strings vazias
    data = {
        'id': int(row['id']),
        'Nome': row['Nome'] if is_valid_value(row['Nome']) else '',
        'Umidade (%)': convert_to_float(row['Umidade (%)']),
        'Energia (kcal)': convert_to_float(row['Energia (kcal)']),
        'Energia (kJ)': convert_to_float(row['Energia (kJ)']),
        'Proteína (g)': convert_to_float(row['Proteína (g)']),
        'Lipídeos (g)': convert_to_float(row['Lipídeos (g)']),
        'Colesterol (mg)': convert_to_float(row['Colesterol (mg)']),
        'Carboidrato (g)': convert_to_float(row['Carboidrato (g)']),
        'Fibra Alimentar (g)': convert_to_float(row['Fibra Alimentar (g)']),
        'Cinzas (g)': convert_to_float(row['Cinzas (g)']),
        'Cálcio (mg)': convert_to_float(row['Cálcio (mg)']),
        'Magnésio (mg)': convert_to_float(row['Magnésio (mg)'])
    }

    try:
        response = requests.post(api_url, json=data)
        if response.status_code == 200:
            logging.info(f"Alimento {row['Nome']} adicionado com sucesso!")
        else:
            logging.error(f"Falha ao adicionar {row['Nome']}. Erro: {response.text}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Erro ao enviar requisição: {e}")
