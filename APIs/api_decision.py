from fastapi import FastAPI
import re

app = FastAPI()

@app.post("/")
async def decision(data: dict):
    #Politques a recup depuis la base
    politiqueA=1#refus de clients sans benefice net
    politiqueB=0.05#taux d'interets de la banque
    politiqueC=3.0#taux de risque maximum envisagé par la banque

    montant_pret = data.get("Montant du pret", 0)
    duree_pret = data.get("Duree du pret", 0)
    revenu_mensuel = data.get("Revenu mensuel", 0)
    depenses_mensuelles = data.get("Depenses mensuelles", 0)
    valeur_propriete = data.get("Valeur Propriete", 0)
    respecte_la_loi = data.get("Respecte la loi", "")
    age = data.get("Age", 0)
    score_credit = data.get("Score Credit", 0)

    refuse="NON"
    motif=""

    duree_pret = float(duree_pret)
    montant_pret = float(montant_pret)
    revenu_mensuel = float(revenu_mensuel)
    depenses_mensuelles = float(depenses_mensuelles)
    valeur_propriete = float(valeur_propriete)
    age = int(age)
    score_credit = float(score_credit)

    
    taux_de_risque=10.0
    
    if age+duree_pret>100:
        taux_de_risque=taux_de_risque-(100-(age+duree_pret))*2


    if valeur_propriete>(montant_pret)/2:
        taux_de_risque=taux_de_risque-((valeur_propriete-montant_pret)/10000)

    if valeur_propriete<montant_pret/2:
        taux_de_risque=taux_de_risque-((valeur_propriete-montant_pret)/5000)

    if revenu_mensuel>depenses_mensuelles:
        if ((revenu_mensuel-depenses_mensuelles)*duree_pret)<montant_pret:
            taux_de_risque+=(depenses_mensuelles-((revenu_mensuel-depenses_mensuelles)*duree_pret*12))/1000

    taux_de_risque=taux_de_risque*(politiqueB+1)

    taux_de_risque=taux_de_risque-score_credit/10

    if revenu_mensuel<depenses_mensuelles and politiqueA==1:
        return "Entree d'argent inferieures aux sorties d'argent, impossible de preter dans ces conditions"

    if score_credit < 0:
        return "Votre score de credit est inférieur 0, nous ne pouvons pas vous accorder de pret"
    if respecte_la_loi!="OUI":
        return "propriete illegale, on appelle la maréchaussée tout de suite"

    if politiqueC<taux_de_risque:
        return "Nous nous voyons dans l'incapacité d'accepter votre demande de pret, vous nous en voyez désolés"

    somme_mensuelle=(montant_pret*politiqueB)/(duree_pret*12)
    somme_annuelle=(montant_pret*politiqueB)/(duree_pret)
    if politiqueC>taux_de_risque:
        Accord= str("Nous sommes ravis de pouvoir vous dire que votre prêt a été validé par notre système. \nAvec le taux d'interet de "+str(politiqueB)+" % vous serez soumis à un paiment de "+str(somme_mensuelle)+" euros par mois( ou "+str(somme_annuelle)+" euros par an) pendant "+str(duree_pret)+" ans")
        return Accord
    return 'erreur'



    tableau_entrees=String_entree.split('*')

    JSON_Information=tableau_entrees[0]
    JSON_Valeur_Propriete=tableau_entrees[1]
    JSON_Solvabilite=tableau_entrees[2]

    tableau_information,tableau_solvabilite,tableau_valeur_propriete=[],[],[]

    lignes = JSON_Information.split(';')
    for ligne in lignes:
        elements = ligne.split(': ')
        tableau_information+=[elements]

    lignes = JSON_Valeur_Propriete.split(';')
    for ligne in lignes:
        elements = ligne.split(': ')
        tableau_valeur_propriete+=[elements]

    lignes = JSON_Solvabilite.split(';')
    for ligne in lignes:
        elements = ligne.split(': ')
        tableau_solvabilite+=[elements]


    #print("\n\n tableau_information: ",tableau_information,"\n\n")
    #print("\n\n tableau_valeur_propriete: ",tableau_valeur_propriete,"\n\n")
    #print("\n\n tableau_solvabilite: ",tableau_solvabilite,"\n\n")


    Duree_emprunt=int(tableau_information[0][1])
    Age=int(tableau_information[1][1])
    Valeur_pret=float(tableau_information[2][1])
    respecte_loi=tableau_information[3][1]

    Sorties=float(tableau_solvabilite[0][1])
    Entree=float(tableau_solvabilite[1][1])
    STR_pret=tableau_solvabilite[2][1]
    Score_Credit=float(tableau_solvabilite[3][1])

    Valeur_propriete=float(tableau_valeur_propriete[0][1])


    Autres_prets=[]
    prets_temp=STR_pret.split('%')
    for j in range(len(prets_temp)-1):
        Autres_prets+=[int(prets_temp[j])]

    #print("\n\n tableau prets: ",Autres_prets,"\n\n")
    PolitiqueA=1#refus de clients sans benefice net
    PolitiqueB=50000#refus de dettes superieures à #valeur#
    PolitiqueC=3.0#taux de risque maximum envisagé par la banque
    PolitiqueD=0.05#taux d'interets de la banque

    Taux_de_risque=0.0
    if Age+Duree_emprunt>100:
        Taux_de_risque=Taux_de_risque-(100-(Age+Duree_emprunt))*2

    #print("taux de risque lie à l'age: ",Taux_de_risque)

    Somme_dettes=0
    for k in Autres_prets:
        Somme_dettes+=k

    Taux_de_risque=Taux_de_risque+(Somme_dettes/10000)

    #print("taux de risque lie aux dettes: ",Taux_de_risque)

    if Valeur_propriete>Valeur_pret:
        Taux_de_risque=Taux_de_risque-((Valeur_propriete-Valeur_pret)/10000)

    #print("taux de risque lie à la valuation de la propriete: ",Taux_de_risque)

    if Valeur_propriete<Valeur_pret:
        Taux_de_risque=Taux_de_risque-((Valeur_propriete-Valeur_pret)/5000)

    #print("taux de risque lie à la dévaluation de la propriete: ",Taux_de_risque)

    if Entree>Sorties:
        if ((Entree-Sorties)*Duree_emprunt)<Valeur_pret:
            Taux_de_risque+=(Valeur_pret-((Entree-Sorties)*Duree_emprunt*12))/1000

    #print("taux de risque lie au ratio emprunt/capacite à rembourser: ",Taux_de_risque)

    Taux_de_risque=Taux_de_risque*(PolitiqueD+1)

    #print("taux de risque lie au taux d'interet: ",Taux_de_risque)

    Taux_de_risque=Taux_de_risque-Score_Credit/2

    #print("taux de risque lie au score de credit: ",Taux_de_risque)

    if Entree<Sorties and PolitiqueA==1:
        return "Entree d'argent inferieures aux sorties d'argent, impossible de preter dans ces conditions"

    if Somme_dettes>PolitiqueB:
        return "Désolé, notre banque n'autorise pas les emprunts pour les personnes ayant contracté plus de ",PolitiqueB," euros d'emprunts"


    if respecte_loi!="OUI":
        return "propriete illegale, on appelle la maréchaussée tout de suite"

    if PolitiqueC<Taux_de_risque:
        return "Nous nous voyons dans l'incapacité d'accepter votre demande de pret, vous nous en voyez désolés"

    somme_mensuelle=(Valeur_pret*PolitiqueD)/(Duree_emprunt*12)
    somme_annuelle=(Valeur_pret*PolitiqueD)/(Duree_emprunt)
    if PolitiqueC>Taux_de_risque:
        Accord= str("Nous sommes ravis de pouvoir vous dire que votre prêt a été validé par notre système. AVec le taux d'interet de "+str(PolitiqueD)+" % vous serez soumis à un paiment de "+str(somme_mensuelle)+" euros par mois( ou "+str(somme_annuelle)+" euros par an) pendant "+str(Duree_emprunt)+" ans")
        return Accord
    return 'erreur'