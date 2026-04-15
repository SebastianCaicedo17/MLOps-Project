# On part d'une image Python officielle légère
FROM python:3.10-slim

# On définit le dossier de travail à l'intérieur du conteneur
WORKDIR /app

# On copie d'abord le fichier de dépendances
COPY requirements.txt .

# On installe les dépendances 
RUN pip install --no-cache-dir -r requirements.txt

# On copie le reste des fichiers de notre projet (main.py, dossier models, etc.) 
COPY . .

# On expose le port 8000 sur lequel l'API va écouter
EXPOSE 8000

# On définit la commande pour démarrer le service API 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]