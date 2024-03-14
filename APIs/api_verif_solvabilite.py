from fastapi import FastAPI

app = FastAPI()

@app.post("/")
async def scoring_de_credit(data: dict):
    # Convertir les données reçues en variables individuelles
    # Réponse de l'API: {'Nom Client': 'Bern', 'Prenom Client': 'Stephane', 'Adresse': '1 Places d’armes, Versailles', 'Email': 'stephdu78@gmail.com', 'Montant du pret': 2000000, 'Duree du pret': 20, 'Description de la propriete': 'Joli château en plein versailles avec couloir plein de miroirs', 'Revenu mensuel': 8000, 'Depenses mensuelles': 2000, 'Emprunt en cours': 50, 'Valeur Propriete': '2000000', 'Region de location': '2', 'Evaluation du promoteur': '10', 'Respecte la loi': 'OUI', 'Objectif': 'LOCATION', 'Age': '59'}

    nom_client = data.get("Nom Client", "")
    prenom_client = data.get("Prenom Client", "")
    adresse = data.get("Adresse", "")
    email = data.get("Email", "")
    montant_pret = data.get("Montant du pret", 0)
    duree_pret = data.get("Duree du pret", 0)
    revenu_mensuel = data.get("Revenu mensuel", 0)
    depenses_mensuelles = data.get("Depenses mensuelles", 0)
    emprunt_en_cours = data.get("Emprunt en cours", 0)
    valeur_propriete = data.get("Valeur Propriete", "")
    region_de_location = data.get("Region de location", "")
    evaluation_du_promoteur = data.get("Evaluation du promoteeur", "")
    respecte_la_loi = data.get("Respecte la loi", "")
    objectif = data.get("Objectif", "")
    age = data.get("Age", 0)

    score_credit=100.00
    taux_risque=0
    if montant_pret>1000000:
        taux_risque=taux_risque+1
    if duree_pret>20:
        taux_risque=taux_risque+1
    if revenu_mensuel<2000:
        taux_risque=taux_risque+1

        
    score_credit = float(score_credit) - (float(taux_risque)*10)
    
    restant = float(revenu_mensuel-depenses_mensuelles)
    if restant<0:
        restant=float(-1/restant)
    
    score_credit=score_credit+ (restant%100)

    for i in range(0,emprunt_en_cours):
        score_credit=score_credit-10
        
    if float(valeur_propriete)<float(montant_pret):
        score_credit=0

    return {"Score Credit": score_credit}
