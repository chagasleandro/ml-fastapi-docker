# ML FastAPI Docker

API de exemplo para servir um modelo de Machine Learning com FastAPI e Docker.

🔗 Repositório GitHub: [github.com/chagasleandro/ml-fastapi-docker](https://github.com/chagasleandro/ml-fastapi-docker)

## 🧠 Sobre o Projeto

Este projeto serve um modelo `RandomForestClassifier` treinado com a base de dados Iris via uma API REST feita com **FastAPI**. Tudo empacotado em **Docker** para facilitar o deploy.

## 📦 Requisitos

- Python 3.10+
- Docker
- Git

## 🚀 Como usar

### 1. Treinar o modelo
```bash
python train_model.py

## Como usar

1. Treine o modelo:
   ```bash
   python train_model.py
   ```

2. Build da imagem:
   ```bash
   docker build -t ml-fastapi-docker .
   ```

3. Execute a API:
   ```bash
   docker run -p 8000:8000 ml-fastapi-docker
   ```

4. Envie uma requisição:
   ```bash
   curl -X POST http://localhost:8000/predict \
        -H "Content-Type: application/json" \
        -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
   ```

## Tecnologias
- FastAPI
- Scikit-learn
- Docker


