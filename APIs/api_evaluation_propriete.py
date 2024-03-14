from fastapi import FastAPI

app = FastAPI()

@app.post("/")
async def evalution_propriete(data: dict):
    # Convertir les données reçues en variables individuelles
    # Réponse de l'API: {'Nom Client': 'Bern', 'Prenom Client': 'Stephane', 'Adresse': '1 Places d’armes, Versailles', 'Email': 'stephdu78@gmail.com', 'Montant du pret': 2000000, 'Duree du pret': 20, 'Description de la propriete': 'Joli château en plein versailles avec couloir plein de miroirs', 'Revenu mensuel': 8000, 'Depenses mensuelles': 2000, 'Emprunt en cours': 50, 'Valeur Propriete': '2000000', 'Region de location': '2', 'Evaluation du promoteur': '10', 'Respecte la loi': 'OUI', 'Objectif': 'LOCATION', 'Age': '59'}
    duree_pret = data.get("Duree du pret", 0)
    valeur_propriete = data.get("Valeur Propriete", "")
    region_de_location = data.get("Region de location", "")
    evaluation_du_promoteur = data.get("Evaluation du promoteeur", 0)
    respecte_la_loi = data.get("Respecte la loi", "")
    objectif = data.get("Objectif", "")
    age = data.get("Age", 0)

    valeur_propriete = float(valeur_propriete)
    duree_pret = float(duree_pret)
    evaluation_du_promoteur = float(evaluation_du_promoteur)
    region_de_location = int(region_de_location)
    age = int(age)
    
    if region_de_location==0:#region a fort taux de vente
        if objectif=="PROPRIETE":
            valeur_propriete=valeur_propriete*0.7
        else:
            valeur_propriete=valeur_propriete*0.08*duree_pret
    elif region_de_location==1:#region a faible taux de vente
        if objectif=="PROPRIETE":
            valeur_propriete=valeur_propriete*2
        else:
            valeur_propriete=valeur_propriete*0.03*duree_pret
    elif region_de_location==2:#region très attractive en tous points
        if objectif=="PROPRIETE":
            valeur_propriete=valeur_propriete*2.5
        else:
            valeur_propriete=valeur_propriete*0.09*duree_pret
    else:#il ne s'y passe rien, c'est plus ou moins la creuze
        if objectif=="PROPRIETE":
            valeur_propriete=valeur_propriete*0.5
        else:
            valeur_propriete=valeur_propriete*0.01*duree_pret
                
    valeur_propriete=valeur_propriete*float((evaluation_du_promoteur+3)/10)


    if respecte_la_loi!="OUI":
        valeur_propriete=0
        
    return {"Valeur Propriete": valeur_propriete}
