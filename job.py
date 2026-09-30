import os

# Récupérer la variable d'environnement passée par le workflow
api_token = os.getenv("MY_SECRET")

print("Le secret récupéré est :", api_token)
