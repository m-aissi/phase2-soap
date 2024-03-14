from fastapi import FastAPI
import re

app = FastAPI()

@app.post("/")
async def receive_text(text: dict):
    received_text = text.get("text")
    lines = received_text.split("\n")

    extracted_text = {}

    for line in lines:
        parts = line.split(":")
        if len(parts) == 2:
            key = parts[0].strip()
            value = parts[1].strip()
            extracted_text[key] = value

    montant_pret = extracted_text.get("Montant du prêt demandé", "0")
    montant_pret = int(re.sub(r"[^0-9]", "", montant_pret))

    duree_pret = extracted_text.get("Durée du prêt", "0")
    duree_pret = int(re.sub(r"[^0-9]", "", duree_pret))

    revenu_mensuel = extracted_text.get("Revenu mensuel", "0")
    revenu_mensuel = int(re.sub(r"[^0-9]", "", revenu_mensuel))

    depenses_mensuelles = extracted_text.get("Dépenses mensuelles", "0")
    depenses_mensuelles = int(re.sub(r"[^0-9]", "", depenses_mensuelles))

    emprunt_en_cours = extracted_text.get("Emprunt en cour", "0")
    emprunt_en_cours = int(re.sub(r"[^0-9]", "", emprunt_en_cours))

    return {
        "Nom Client": extracted_text.get("Nom du client", ""),
        "Prenom Client": extracted_text.get("Prénom du client", ""),
        "Adresse": extracted_text.get("Adresse", ""),
        "Email": extracted_text.get("Email", ""),
        "Montant du pret": montant_pret,
        "Duree du pret": duree_pret,
        "Description de la propriete": extracted_text.get("Description de la propriete", ""),
        "Revenu mensuel": revenu_mensuel,
        "Depenses mensuelles": depenses_mensuelles,
        "Emprunt en cours": emprunt_en_cours,
        "Valeur Propriete": extracted_text.get("Valeur Propriété", ""),
        "Region de location": extracted_text.get("Région de location", ""),
        "Evaluation du promoteur": extracted_text.get("Évaluation du promoteur", ""),
        "Respecte la loi": extracted_text.get("Respecte la loi", ""),
        "Objectif": extracted_text.get("Objectif", ""),
        "Age": extracted_text.get("Age", "")
    }
