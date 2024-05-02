import json
import requests

# Définir les données JSON pour la requête (si nécessaire)
json_data = {
    "name": "jobgenerate",
    "image": "alakh1111/jgeneratedata_kube"
}

# Définir le type de contenu de la requête comme étant JSON
headers = {"Content-Type": "application/json"}

# Envoyer une requête POST à l'endpoint /runjob de votre application Flask avec les données JSON et les en-têtes appropriés
response = requests.post("http://127.0.0.1:5000/runjob", json=json_data, headers=headers)

# Afficher la réponse pour le débogage
print(response.text)
