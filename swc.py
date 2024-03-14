import requests
        
def send_text_to_api():
    # on declare reponse
    data = None
    # Définir l'URL de l'API
    url = "http://localhost:5000"
    with open("demande.txt", "r") as file:
        text = file.read()
    data = {"text": text}
    data = requests.post(url, json=data)
    if data.status_code == 200:
        print("Réponse de l'API:", data.json())
    else:
        print("La requête a échoué avec le code de statut:", data.status_code)
    return data
        
def verif_solvabilite(data):
    url = "http://localhost:6000"

    data = requests.post(url, json=data.json())

    if data.status_code == 200:
        print("Réponse de l'API:", data.json())
    else:
        print("La requête a échoué avec le code de statut:", data.status_code)
    return data

def eval_propriete(data):
    url = "http://localhost:7000"

    data = requests.post(url, json=data.json())

    if data.status_code == 200:
        print("Réponse de l'API:", data.json())
    else:
        print("La requête a échoué avec le code de statut:", data.status_code)
    return data

def decision(data):
    url = "http://localhost:8000"

    data = requests.post(url, json=data.json())
    if data.status_code == 200:
        print("Réponse de l'API:", data.json())
    else:
        print("La requête a échoué avec le code de statut:", data.status_code)
    return data

# Appeler la fonction pour interroger l'API
donnee_client = send_text_to_api()
score = verif_solvabilite(donnee_client)
valeur_propriete = eval_propriete(donnee_client)

# On va parcourir rep pour modifier la valeur de 'Valeur Propriete' & ajoute le champ  {'Score Credit': 0} dans resp, on va
# modifier la valeur de 'Valeur Propriete' pour qu'elle soit égale à valeur_propriete
# et on set la valeur de score_credit à score

donnee_client.json()['Valeur Propriete'] = valeur_propriete
donnee_client.json()['Score Credit'] = score

                 

decision = decision(donnee_client)

with open("resultat.txt", "w") as file:
    file.write(str(decision.json()))
    
print("Le résultat a été enregistré dans le fichier resultat.txt")