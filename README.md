# ML FastAPI Docker

API de exemplo para servir um modelo de Machine Learning com FastAPI e Docker.

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


