from flask import Blueprint, request, jsonify
from database import SessionLocal
from models.alimento import Alimento
from sqlalchemy.exc import IntegrityError
import logging

logging.basicConfig(level=logging.DEBUG)

app = Blueprint('app', __name__)

@app.route('/add_alimento', methods=['POST'])
def add_alimento():
    session = SessionLocal()
    data = request.get_json()

    # Verificar se o banco de dados já está preenchido
    existing_alimento = session.query(Alimento).filter_by(id=data['id']).first()
    if existing_alimento:
        logging.info(f"Alimento com ID {data['id']} já existe. Pulando inserção.")
        return jsonify({"error": "Alimento já existe"}), 409

    novo_alimento = Alimento(
        id=data['id'],
        Nome=data['Nome'],
        Umidade=data.get('Umidade', 0),
        Energia_kcal=data.get('Energia_kcal', 0),
        Energia_kj=data.get('Energia_kj', 0),
        Proteina=data.get('Proteina', 0),
        Lipideos=data.get('Lipideos', 0),
        Colesterol=data.get('Colesterol', 0),
        Carboidrato=data.get('Carboidrato', 0),
        Fibra_Alimentar=data.get('Fibra_Alimentar', 0),
        Cinzas=data.get('Cinzas', 0),
        Calcio=data.get('Calcio', 0),
        Magnesio=data.get('Magnesio', 0)
    )

    try:
        session.add(novo_alimento)
        session.commit()
        logging.info(f"Alimento {data['Nome']} adicionado com sucesso!")
        return jsonify({"success": "Alimento adicionado"}), 201
    except IntegrityError as e:
        session.rollback()
        logging.error(f"Erro ao adicionar alimento: {e}")
        return jsonify({"error": "Erro ao adicionar alimento"}), 500
    finally:
        session.close()

@app.route('/alimentos', methods=['GET'])
def get_alimentos():
    session = SessionLocal()
    alimentos = session.query(Alimento).all()
    output = []

    for alimento in alimentos:
        alimento_data = {
            'id': alimento.id,
            'Nome': alimento.Nome,
            'Umidade (%)': alimento.Umidade,
            'Energia (kcal)': alimento.Energia_kcal,
            'Energia (kJ)': alimento.Energia_kj,
            'Proteína (g)': alimento.Proteina,
            'Lipídeos (g)': alimento.Lipideos,
            'Colesterol (mg)': alimento.Colesterol,
            'Carboidrato (g)': alimento.Carboidrato,
            'Fibra Alimentar (g)': alimento.Fibra_Alimentar,
            'Cinzas (g)': alimento.Cinzas,
            'Cálcio (mg)': alimento.Calcio,
            'Magnésio (mg)': alimento.Magnesio
        }
        output.append(alimento_data)

    session.close()
    return jsonify(output)

@app.route('/search_alimentos', methods=['GET'])
def search_alimentos():
    session = SessionLocal()
    query = request.args.get('query', '')
    alimentos = session.query(Alimento).filter(Alimento.Nome.like(f'%{query}%')).all()
    output = []

    for alimento in alimentos:
        alimento_data = {
            'id': alimento.id,
            'Nome': alimento.Nome,
            'Umidade': alimento.Umidade,
            'Energia_kcal': alimento.Energia_kcal,
            'Energia_kj': alimento.Energia_kj,
            'Proteina': alimento.Proteina,
            'Lipideos': alimento.Lipideos,
            'Colesterol': alimento.Colesterol,
            'Carboidrato': alimento.Carboidrato,
            'Fibra_Alimentar': alimento.Fibra_Alimentar,
            'Cinzas': alimento.Cinzas,
            'Calcio': alimento.Calcio,
            'Magnesio': alimento.Magnesio
        }
        output.append(alimento_data)

    session.close()
    return jsonify(output)

    session.close()
    return jsonify(output)
