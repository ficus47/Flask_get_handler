# Utilisation de l'image de base Python pour Flask
FROM python:3.8-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires (main.py et autres dépendances)
COPY main.py requirements.txt /app/

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port sur lequel Flask écoute (dans notre cas, 5000)
EXPOSE 5000

# Commande pour démarrer l'application Flask
CMD ["python", "main.py"]
