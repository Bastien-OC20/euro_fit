import os
import sys
import pytest
import random

# Ajouter le dossier parent afin que le package "database" soit trouvé
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from database.fake_my_db import (
    create_fake_adresse,
    create_fake_code_postal,
    create_fake_assurance,
    create_fake_club,
    create_fake_agent_securite,
    create_fake_agent_nettoyage,
    create_fake_utilisation_machine,
    create_fake_specialisation,
    create_fake_pratique,
    create_fake_salle_activite,
    create_fake_club_salle,
    create_fake_souscrit,
    create_fake_coach,
    create_fake_abonnement,
    create_fake_medecin,
    create_fake_transaction,
    create_fake_salle,
    create_fake_machine,
    create_fake_capteur,
    create_fake_pays,
    create_fake_ville,
    create_fake_activite,
    create_fake_equipement,
    create_fake_analyse_corporelle,
    create_fake_membre,
    generate_fake_data,
    session
)
from database.create_db import Membre

# Tests pour les fonctions de génération individuelles

def test_create_fake_adresse():
    adresse = create_fake_adresse()
    assert isinstance(adresse.numero_rue, int)
    assert isinstance(adresse.nom_rue, str)
    assert isinstance(adresse.id_code_postal, int)

def test_create_fake_code_postal():
    cp = create_fake_code_postal()
    assert isinstance(cp.code_postal, str)
    assert isinstance(cp.id_ville, int)

def test_create_fake_assurance():
    assurance = create_fake_assurance()
    assert isinstance(assurance.nom, str)
    assert isinstance(assurance.telephone, str)
    assert isinstance(assurance.id_adresse, int)

def test_create_fake_club():
    club = create_fake_club()
    assert isinstance(club.nom, str)
    assert isinstance(club.surface_m_, int)
    assert isinstance(club.nb_salles, int)
    assert isinstance(club.nb_machines, int)

def test_create_fake_agent_securite():
    agent = create_fake_agent_securite()
    assert isinstance(agent.nom, str)
    assert isinstance(agent.prenom, str)
    assert isinstance(agent.telephone, str)

def test_create_fake_agent_nettoyage():
    agent = create_fake_agent_nettoyage()
    assert isinstance(agent.nom, str)
    assert isinstance(agent.prenom, str)
    assert isinstance(agent.telephone, str)

def test_create_fake_utilisation_machine():
    util = create_fake_utilisation_machine()
    assert isinstance(util.id_membre, int)
    assert isinstance(util.id_machine, int)
    assert hasattr(util, "date_utilisation")
    assert isinstance(util.duree_minute, int)

def test_create_fake_specialisation():
    spec = create_fake_specialisation()
    assert isinstance(spec.id_coach, int)
    assert isinstance(spec.id_activite, int)

def test_create_fake_pratique():
    pratique = create_fake_pratique()
    assert isinstance(pratique.id_membre, int)
    assert isinstance(pratique.id_activite, int)

def test_create_fake_salle_activite():
    salle_act = create_fake_salle_activite()
    assert isinstance(salle_act.id_salle, int)
    assert isinstance(salle_act.id_activite, int)

def test_create_fake_club_salle():
    club_salle = create_fake_club_salle()
    assert isinstance(club_salle.id_club, int)
    assert isinstance(club_salle.id_salle, int)

def test_create_fake_souscrit():
    souscrit = create_fake_souscrit()
    assert isinstance(souscrit.id_membre, int)
    assert isinstance(souscrit.id_abonnement, int)
    assert isinstance(souscrit.id_club, int)
    assert isinstance(souscrit.duree_mois, int)
    assert hasattr(souscrit, "date_inscription")

def test_create_fake_coach():
    coach = create_fake_coach()
    assert isinstance(coach.nom, str)
    assert isinstance(coach.prenom, str)
    assert isinstance(coach.email, str)

def test_create_fake_abonnement():
    abo = create_fake_abonnement()
    assert isinstance(abo.nom, str)
    assert isinstance(abo.description, str)
    assert isinstance(abo.tarif, float)

def test_create_fake_medecin():
    medecin = create_fake_medecin()
    assert isinstance(medecin.nom, str)
    assert isinstance(medecin.prenom, str)
    assert isinstance(medecin.email, str)
    assert isinstance(medecin.telephone, str)

def test_create_fake_transaction():
    trans = create_fake_transaction()
    assert hasattr(trans, "date_paiement")
    assert hasattr(trans, "montant")

def test_create_fake_salle():
    salle = create_fake_salle()
    assert isinstance(salle.nom, str)
    assert isinstance(salle.type_salle, str)
    assert isinstance(salle.superficie_m_, int)

def test_create_fake_machine():
    machine = create_fake_machine()
    assert isinstance(machine.type_machine, str)
    assert isinstance(machine.marque, str)
    assert isinstance(machine.etat, str)
    assert isinstance(machine.num_serie, str)
    assert isinstance(machine.id_salle, int)

def test_create_fake_capteur():
    capteur = create_fake_capteur()
    assert isinstance(capteur.type_capteur, str)
    assert isinstance(capteur.valeur, float)
    assert hasattr(capteur, "date_mesure")
    assert isinstance(capteur.id_salle, int)

def test_create_fake_pays():
    pays = create_fake_pays()
    assert isinstance(pays.nom_pays, str)

def test_create_fake_ville():
    ville = create_fake_ville()
    assert isinstance(ville.nom_ville, str)
    assert isinstance(ville.id_pays, int)

def test_create_fake_activite():
    activite = create_fake_activite()
    assert isinstance(activite.nom, str)
    assert isinstance(activite.description, str)

def test_create_fake_equipement():
    equip = create_fake_equipement()
    assert isinstance(equip.type_equipement, str)
    assert isinstance(equip.marque, str)
    assert isinstance(equip.etat, str)
    assert isinstance(equip.id_salle, int)

def test_create_fake_analyse_corporelle():
    analyse = create_fake_analyse_corporelle()
    assert hasattr(analyse, "IMC")
    assert hasattr(analyse, "metabolisme_base")
    assert hasattr(analyse, "masse_grasse")
    assert hasattr(analyse, "masse_musculaire")
    assert isinstance(analyse.id_membre, int)

def test_create_fake_membre():
    membre = create_fake_membre()
    assert isinstance(membre.nom, str)
    assert isinstance(membre.prenom, str)
    assert hasattr(membre, "date_naissance")
    assert isinstance(membre.email, str)
    assert isinstance(membre.telephone, str)
    assert isinstance(membre.numero_licence, str)
    assert isinstance(membre.id_medecin, int)
    assert isinstance(membre.id_coach, int)

# Test de la génération globale des données
def test_generate_fake_data():
    # Réinitialiser/évacuer la session si besoin
    session.expunge_all()
    
    # Générer et insérer toutes les données fictives
    generate_fake_data()
    
    # Vérifier qu'au moins 200 membres ont été insérés
    membre_count = session.query(Membre).count()
    assert membre_count >= 200, f"Nombre de membres insérés : {membre_count}. Devrait être au moins 200."