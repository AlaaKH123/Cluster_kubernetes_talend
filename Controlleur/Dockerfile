# Utilisez une image de base Python
FROM python:3.9

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt /app

# Installer les dépendances Python
RUN pip install -r requirements.txt

# Copier le code source de l'application dans le conteneur
COPY . /app

# Exposer le port 5000 pour l'application Flask
EXPOSE 5000

# Commande par défaut pour exécuter l'application Flask
CMD ["python", "flask-kube.py"]