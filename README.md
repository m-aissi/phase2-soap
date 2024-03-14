### Projet SOAP - Alexis Fiolet, Louis Tonnevy, Mehdi Aissi IATIC5

## Requirements
```bash
pip install requests
pip install uvicorn
pip install fastapi
```

## Lancer les APIs
Se placer dans le dossier /APIs et lancer sur 4 terminals différents:
```bash
uvicorn api_extraction_infos_metier:app --reload --port 5000
uvicorn api_verif_solvabilite:app --reload --port 6000
uvicorn api_evaluation_propriete:app --reload --port 7000
uvicorn api_decision:app --reload --port 8000
```

## Utiliser le programme
Modifié le fichier 'demande.txt' à votre convenance.

Se placer dans le dossier racine
```bash
python3 swc.py
```