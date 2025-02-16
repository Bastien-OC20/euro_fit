from faker import Faker
from sqlalchemy.orm import sessionmaker
from database.create_db import Base, Coach, Abonnement, Medecin, Transaction, Salle, Machine, Membre, Capteur, Pays, Ville, Activite, Equipement, AnalyseCorporelle, CodePostal, Adresse, Assurance, Club, AgentSecurite, AgentNettoyage, UtilisationMachine, Paiement, Specialisation, Pratique, SalleActivite, ClubSalle, Souscrit, init_db
from sqlalchemy import create_engine
import random
from datetime import datetime, timedelta

# Initialisation de Faker
fake = Faker()

# Initialisation de la session SQLAlchemy
session = init_db()

def create_fake_adresse():
    """
    Crée une fausse entrée pour la table Adresse.
    Les champs utilisés sont 'numero_rue', 'nom_rue' et 'id_code_postal' (clé étrangère).
    """
    return Adresse(
        numero_rue=random.randint(1, 200),
        nom_rue=fake.street_name(),
        id_code_postal=random.randint(1, 100)
    )

def create_fake_code_postal():
    """
    Crée une fausse entrée pour la table Code_postal.
    """
    return CodePostal(
        code_postal=fake.zipcode(),
        id_ville=random.randint(1, 100)
    )

def create_fake_assurance():
    """
    Crée une fausse entrée pour la table Assurance.
    """
    return Assurance(
        nom=fake.company(),
        telephone=fake.phone_number(),
        id_adresse=random.randint(1, 100)
    )

def create_fake_club():
    """
    Crée une fausse entrée pour la table Club.
    """
    return Club(
        nom=fake.unique.company(),
        surface_m_=random.randint(100, 2000),
        nb_salles=random.randint(1, 10),
        nb_machines=random.randint(10, 200),
        id_adresse=random.randint(1, 100),
        id_assurance=random.randint(1, 100)
    )

def create_fake_agent_securite():
    """
    Crée une fausse entrée pour la table Agent_Sécurité.
    """
    return AgentSecurite(
        nom=fake.last_name(),
        prenom=fake.first_name(),
        telephone=fake.phone_number(),
        id_club=random.randint(1, 100)
    )

def create_fake_agent_nettoyage():
    """
    Crée une fausse entrée pour la table Agent_Nettoyage.
    """
    return AgentNettoyage(
        nom=fake.last_name(),
        prenom=fake.first_name(),
        telephone=fake.phone_number(),
        id_club=random.randint(1, 100)
    )

def create_fake_utilisation_machine():
    """
    Crée une fausse entrée pour la table Utilisation_Machine.
    Utilise 'date_utilisation' et 'duree_minute' pour enregistrer la période d'utilisation.
    """
    start = fake.date_time_this_year()
    duration = random.randint(10, 120)
    return UtilisationMachine(
        id_membre=random.randint(1, 100),
        id_machine=random.randint(1, 100),
        date_utilisation=start,
        duree_minute=duration
    )

def create_fake_specialisation():
    """
    Crée une fausse entrée pour la table Spécialisation.
    """
    return Specialisation(
        id_coach=random.randint(1, 100),
        id_activite=random.randint(1, 100)
    )

def create_fake_pratique():
    """
    Crée une fausse entrée pour la table Pratique.
    """
    return Pratique(
        id_membre=random.randint(1, 100),
        id_activite=random.randint(1, 100)
    )

def create_fake_salle_activite():
    """
    Crée une fausse entrée pour la table Salle_Activité.
    """
    return SalleActivite(
        id_salle=random.randint(1, 100),
        id_activite=random.randint(1, 100)
    )

def create_fake_club_salle():
    """
    Crée une fausse entrée pour la table Club_Salle.
    """
    return ClubSalle(
        id_club=random.randint(1, 100),
        id_salle=random.randint(1, 100)
    )

def create_fake_souscrit():
    """
    Crée une fausse entrée pour la table souscrit.
    """
    return Souscrit(
        id_membre=random.randint(1, 100),
        id_abonnement=random.randint(1, 100),
        id_club=random.randint(1, 100),
        duree_mois=random.randint(1, 24),
        date_inscription=fake.date_this_year()
    )

def create_fake_coach():
    """
    Crée une fausse entrée pour la table Coach.
    """
    return Coach(
        nom=fake.last_name(),
        prenom=fake.first_name(),
        email=fake.unique.email()
    )

def create_fake_abonnement():
    """
    Crée une fausse entrée pour la table Abonnement.
    """
    return Abonnement(
        nom=fake.unique.catch_phrase(),
        description=fake.text(max_nb_chars=200),
        tarif=round(random.uniform(10.0, 100.0), 2)
    )

def create_fake_medecin():
    """
    Crée une fausse entrée pour la table Médecin.
    """
    return Medecin(
        nom=fake.last_name(),
        prenom=fake.first_name(),
        email=fake.unique.email(),
        telephone=fake.phone_number()
    )

def create_fake_transaction():
    """
    Crée une fausse entrée pour la table Transaction.
    """
    return Transaction(
        date_paiement=fake.date_time_this_year(),
        montant=round(random.uniform(20.0, 1000.0), 2)
    )

def create_fake_salle():
    """
    Crée une fausse entrée pour la table Salle.
    """
    return Salle(
        nom=fake.unique.company(),
        type_salle=random.choice(["cardio", "musculation", "polyvalente"]),
        superficie_m_=random.randint(50, 500)
    )

def create_fake_machine():
    """
    Crée une fausse entrée pour la table Machine.
    """
    return Machine(
        type_machine=random.choice(["tapis", "elliptique", "vélo", "rameur"]),
        marque=fake.company(),
        etat=random.choice(["neuf", "usagé", "en maintenance"]),
        num_serie=fake.unique.ean(length=8),
        id_salle=random.randint(1, 100)
    )

def create_fake_capteur():
    """
    Crée une fausse entrée pour la table Capteur.
    """
    return Capteur(
        type_capteur=random.choice(["température", "humidité", "vibration"]),
        valeur=round(random.uniform(0, 100), 2),
        date_mesure=fake.date_time_this_year(),
        id_salle=random.randint(1, 100)
    )

def create_fake_pays():
    """
    Crée une fausse entrée pour la table Pays.
    """
    return Pays(
        nom_pays=fake.country()
    )

def create_fake_ville():
    """
    Crée une fausse entrée pour la table Ville.
    """
    return Ville(
        nom_ville=fake.city(),
        id_pays=random.randint(1, 100)
    )

def create_fake_activite():
    """
    Crée une fausse entrée pour la table Activité.
    """
    return Activite(
        nom=fake.unique.word().capitalize(),
        description=fake.text(max_nb_chars=200)
    )

def create_fake_equipement():
    """
    Crée une fausse entrée pour la table Équipement.
    """
    return Equipement(
        type_equipement=random.choice(["poids", "banc", "tapis"]),
        marque=fake.company(),
        etat=random.choice(["neuf", "usagé", "en réparation"]),
        id_salle=random.randint(1, 100)
    )

def create_fake_analyse_corporelle():
    """
    Crée une fausse entrée pour la table Analyse_Corporelle.
    """
    return AnalyseCorporelle(
        date_analyse=fake.date_this_year(),
        IMC=round(random.uniform(15.0, 40.0), 2),
        metabolisme_base=round(random.uniform(1000, 3000), 2),
        masse_grasse=round(random.uniform(10.0, 40.0), 2),
        masse_musculaire=round(random.uniform(30.0, 80.0), 2),
        id_membre=random.randint(1, 100)
    )

def create_fake_membre():
    """
    Crée une fausse entrée pour la table Membre.
    """
    return Membre(
        nom=fake.last_name(),
        prenom=fake.first_name(),
        date_naissance=fake.date_of_birth(minimum_age=18, maximum_age=80),
        email=fake.unique.email(),
        telephone=fake.phone_number(),
        numero_licence=fake.unique.bban(),  # identifiant unique fictif
        id_medecin=random.randint(1, 100),
        id_coach=random.randint(1, 100)
    )

def generate_fake_data():
    try:
        # Insertion des fausses données pour d'autres tables
        for _ in range(200):
            session.add(create_fake_adresse())
            session.add(create_fake_code_postal())
            session.add(create_fake_assurance())
            session.add(create_fake_club())
            session.add(create_fake_agent_securite())
            session.add(create_fake_agent_nettoyage())
            session.add(create_fake_coach())
            session.add(create_fake_abonnement())
            session.add(create_fake_medecin())
            session.add(create_fake_transaction())
            session.add(create_fake_salle())
            session.add(create_fake_machine())
            session.add(create_fake_capteur())
            session.add(create_fake_pays())
            session.add(create_fake_ville())
            session.add(create_fake_activite())
            session.add(create_fake_equipement())
            session.add(create_fake_analyse_corporelle())
            session.add(create_fake_membre())  # Ajout de membres
            session.add(create_fake_souscrit())
        
        # Gérer la génération de données pour les tables à contraintes uniques (paiement etc.)
        paiement_pairs = set()
        while len(paiement_pairs) < 200:
            id_membre = random.randint(1, 100)
            id_transaction = random.randint(1, 100)
            paiement_pairs.add((id_membre, id_transaction))
        for id_membre, id_transaction in paiement_pairs:
            session.add(Paiement(id_membre=id_membre, id_transaction=id_transaction))
        
        # Suite pour les autres tables avec clés composées (Pratique, Specialisation, SalleActivite, ClubSalle, UtilisationMachine, etc.)
        
        session.commit()
        print("Données fictives insérées avec succès !")
    except Exception as e:
        session.rollback()
        print(f"Une erreur est survenue lors de l'insertion des données fictives : {e}")

if __name__ == "__main__":
    generate_fake_data()
