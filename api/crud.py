from sqlalchemy.orm import Session
from .models import (
    Coach, Membre, Abonnement, Medecin, Transaction, Salle, Machine, Capteur,
    Pays, Activite, Equipement, Ville, AnalyseCorporelle, CodePostal, Adresse,
    Assurance, Club, AgentSecurite, AgentNettoyage, UtilisationMachine, Paiement,
    Specialisation, Pratique, SalleActivite, ClubSalle, Souscrit
)

# ===== CRUD pour Coach =====
def get_coach(db: Session, coach_id: int):
    return db.query(Coach).filter(Coach.id_coach == coach_id).first()

def create_coach(db: Session, nom: str, prenom: str, email: str):
    coach = Coach(nom=nom, prenom=prenom, email=email)
    db.add(coach)
    db.commit()
    db.refresh(coach)
    return coach

def update_coach(db: Session, coach_id: int, **kwargs):
    coach = get_coach(db, coach_id)
    if coach:
        for key, value in kwargs.items():
            setattr(coach, key, value)
        db.commit()
        db.refresh(coach)
    return coach

def delete_coach(db: Session, coach_id: int):
    coach = get_coach(db, coach_id)
    if coach:
        db.delete(coach)
        db.commit()
    return coach

# ===== CRUD pour Membre =====
def get_membre(db: Session, membre_id: int):
    return db.query(Membre).filter(Membre.id_membre == membre_id).first()

def create_membre(db: Session, nom: str, prenom: str, date_naissance, email: str, telephone: str,
                  numero_licence: str, id_medecin: int, id_coach: int):
    membre = Membre(
        nom=nom,
        prenom=prenom,
        date_naissance=date_naissance,
        email=email,
        telephone=telephone,
        numero_licence=numero_licence,
        id_medecin=id_medecin,
        id_coach=id_coach
    )
    db.add(membre)
    db.commit()
    db.refresh(membre)
    return membre

def update_membre(db: Session, membre_id: int, **kwargs):
    membre = get_membre(db, membre_id)
    if membre:
        for key, value in kwargs.items():
            setattr(membre, key, value)
        db.commit()
        db.refresh(membre)
    return membre

def delete_membre(db: Session, membre_id: int):
    membre = get_membre(db, membre_id)
    if membre:
        db.delete(membre)
        db.commit()
    return membre

# ===== CRUD pour Abonnement =====
def get_abonnement(db: Session, abonnement_id: int):
    return db.query(Abonnement).filter(Abonnement.id_abonnement == abonnement_id).first()

def create_abonnement(db: Session, nom: str, description: str, tarif):
    abonnement = Abonnement(nom=nom, description=description, tarif=tarif)
    db.add(abonnement)
    db.commit()
    db.refresh(abonnement)
    return abonnement

def update_abonnement(db: Session, abonnement_id: int, **kwargs):
    abonnement = get_abonnement(db, abonnement_id)
    if abonnement:
        for key, value in kwargs.items():
            setattr(abonnement, key, value)
        db.commit()
        db.refresh(abonnement)
    return abonnement

def delete_abonnement(db: Session, abonnement_id: int):
    abonnement = get_abonnement(db, abonnement_id)
    if abonnement:
        db.delete(abonnement)
        db.commit()
    return abonnement

# ===== CRUD pour Medecin =====
def get_medecin(db: Session, medecin_id: int):
    return db.query(Medecin).filter(Medecin.id_medecin == medecin_id).first()

def create_medecin(db: Session, nom: str, prenom: str, email: str, telephone: str):
    medecin = Medecin(nom=nom, prenom=prenom, email=email, telephone=telephone)
    db.add(medecin)
    db.commit()
    db.refresh(medecin)
    return medecin

def update_medecin(db: Session, medecin_id: int, **kwargs):
    medecin = get_medecin(db, medecin_id)
    if medecin:
        for key, value in kwargs.items():
            setattr(medecin, key, value)
        db.commit()
        db.refresh(medecin)
    return medecin

def delete_medecin(db: Session, medecin_id: int):
    medecin = get_medecin(db, medecin_id)
    if medecin:
        db.delete(medecin)
        db.commit()
    return medecin

# ===== CRUD pour Transaction =====
def get_transaction(db: Session, transaction_id: int):
    return db.query(Transaction).filter(Transaction.id_transaction == transaction_id).first()

def create_transaction(db: Session, date_paiement, montant):
    transaction = Transaction(date_paiement=date_paiement, montant=montant)
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction

def update_transaction(db: Session, transaction_id: int, **kwargs):
    transaction = get_transaction(db, transaction_id)
    if transaction:
        for key, value in kwargs.items():
            setattr(transaction, key, value)
        db.commit()
        db.refresh(transaction)
    return transaction

def delete_transaction(db: Session, transaction_id: int):
    transaction = get_transaction(db, transaction_id)
    if transaction:
        db.delete(transaction)
        db.commit()
    return transaction

# ===== Fonctions génériques =====
def get_all(db: Session, model):
    """
    Récupère tous les enregistrements d'un modèle donné.
    """
    return db.query(model).all()