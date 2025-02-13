from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, DECIMAL, Enum, Text, CheckConstraint, DateTime
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
# from datetime import datetime, date

Base = declarative_base()

class Membre(Base):
    __tablename__ = "membre"
    id_membre = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    prenom = Column(String(100), nullable=False)
    date_naissance = Column(Date, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    telephone = Column(String(20), nullable=False)
    adresse = Column(String, nullable=False)
    id_abonnement = Column(Integer, ForeignKey("abonnement.id_abonnement"))
    id_medecin = Column(Integer, ForeignKey("medecin.id_medecin"))
    id_coach = Column(Integer, ForeignKey("coach.id_coach"))
    date_inscription = Column(Date, nullable=False)
    numero_licence = Column(String(50), unique=True, nullable=False)

class Frequente(Base):
    __tablename__ = "frequente"
    id_membre = Column(Integer, ForeignKey("membre.id_membre"), primary_key=True)
    id_club = Column(Integer, ForeignKey("club.id_club"), primary_key=True)
    membre = relationship("Membre")
    club = relationship("Club")

class Club(Base):
    __tablename__ = "club"
    id_club = Column(Integer, primary_key=True)
    nom = Column(String(100), unique=True, nullable=False)
    adresse = Column(String, nullable=False)
    ville = Column(String(100), nullable=False)
    id_pays = Column(Integer, ForeignKey("pays.id_pays"), nullable=False)
    id_assurance = Column(Integer, ForeignKey("assurance.id_assurance"))
    surface_m2 = Column(Integer, nullable=False)
    nb_salles = Column(Integer, nullable=False)
    nb_machines = Column(Integer, nullable=False)
    id_agent_securite = Column(Integer, ForeignKey("agent_securite.id_agent_securite"))
    id_agent_nettoyage = Column(Integer, ForeignKey("agent_nettoyage.id_agent_nettoyage"))
    pays = relationship("Pays")
    assurance = relationship("Assurance")
    agent_securite = relationship("AgentSecurite")
    agent_nettoyage = relationship("AgentNettoyage")

class Pays(Base):
    __tablename__ = "pays"
    id_pays = Column(Integer, primary_key=True)
    nom = Column(String(100), unique=True, nullable=False)
    club = relationship("Club")

class Assurance(Base):
    __tablename__ = "assurance"
    id_assurance = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    adresse = Column(String, nullable=False)
    ville = Column(String(100), nullable=False)
    id_pays = Column(Integer, ForeignKey("pays.id_pays"), nullable=False)
    telephone = Column(String(20), nullable=False)
    pays = relationship("Pays")

class AgentSecurite(Base):
    __tablename__ = "agent_securite"
    id_agent_securite = Column(Integer, primary_key=True)
    nom = Column(String(100), unique=True, nullable=False)
    prenom = Column(String(100), nullable=False)
    telephone = Column(String(20), nullable=False)
    id_club = Column(Integer, ForeignKey("club.id_club"), nullable=False)
    club = relationship("Club")

class AgentNettoyage(Base):
    __tablename__ = "agent_nettoyage"
    id_agent_nettoyage = Column(Integer, primary_key=True)
    nom = Column(String(100), unique=True, nullable=False)
    prenom = Column(String(100), nullable=False)
    telephone = Column(String(20), nullable=False)
    id_club = Column(Integer, ForeignKey("club.id_club"), nullable=False)
    club = relationship("Club")

class AnalyseCorporelle(Base):
    __tablename__ = "analyse_corporelle"
    id_analyse = Column(Integer, primary_key=True, autoincrement=True)
    id_membre = Column(Integer, ForeignKey("membre.id_membre"), nullable=False)
    date_analyse = Column(Date, nullable=False)
    IMC = Column(DECIMAL(5,2), nullable=False)
    metabolisme_base = Column(DECIMAL(5,2), nullable=False)
    masse_grasse = Column(DECIMAL(5,2), nullable=False)
    masse_musculaire = Column(DECIMAL(5,2), nullable=False)
    membre = relationship("Membre")

class Abonnement(Base):
    __tablename__ = "abonnement"
    id_abonnement = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
    tarif = Column(DECIMAL(6,2), nullable=False)
    duree_mois = Column(Integer, nullable=False)
    membre = relationship("Membre")

class Paiement(Base):
    __tablename__ = "paiement"
    id_membre = Column(Integer, ForeignKey("membre.id_membre"), primary_key=True)
    id_transaction = Column(Integer, ForeignKey("transaction.id_transaction"), primary_key=True)
    membre = relationship("Membre")
    transaction = relationship("Transaction")

class Transaction(Base):
    __tablename__ = "transaction"
    id_transaction = Column(Integer, primary_key=True, autoincrement=True)
    id_membre = Column(Integer, ForeignKey("membre.id_membre"), nullable=False)
    date_paiement = Column(DateTime, nullable=False)
    montant = Column(DECIMAL(8,2), CheckConstraint("montant > 0"), nullable=False)
    membre = relationship("Membre")

class Medecin(Base):
    __tablename__ = "medecin"
    id_medecin = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String(100), nullable=False)
    prenom = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    telephone = Column(String(20), nullable=False)
    membre = relationship("Membre")

class Salle(Base):
    __tablename__ = "salle"
    id_salle = Column(Integer, primary_key=True)
    id_club = Column(Integer, ForeignKey("club.id_club"), nullable=False)
    nom = Column(String(100), nullable=False)
    type_salle = Column(String(50), nullable=False)
    superficie_m2 = Column(Integer, nullable=False)
    club = relationship("Club")

class Equipement(Base):
    __tablename__ = "equipement"
    id_equipement = Column(Integer, primary_key=True)
    id_salle = Column(Integer, ForeignKey("salle.id_salle"), nullable=False)
    type_equipement = Column(Enum("climatiseur", "purificateur_air"), nullable=False)
    marque = Column(String(100), nullable=False)
    etat = Column(Enum("fonctionnel", "en panne"), nullable=False)
    salle = relationship("Salle")

class Machine(Base):
    __tablename__ = "machine"
    id_machine = Column(Integer, primary_key=True, autoincrement=True)
    id_salle = Column(Integer, ForeignKey("salle.id_salle"), nullable=False)
    type_machine = Column(String(50), nullable=False)
    marque = Column(String(100), nullable=False)
    etat = Column(String(50), nullable=False)
    salle = relationship("Salle")

class UtilisationMachine(Base):
    __tablename__ = "utilisation_machine"
    id_utilisation = Column(Integer, primary_key=True)
    id_membre = Column(Integer, ForeignKey("membre.id_membre"), nullable=False)
    id_machine = Column(Integer, ForeignKey("machine.id_machine"), nullable=False)
    date_utilisation = Column(Date, nullable=False)
    duree_minute = Column(Integer, nullable=False)
    membre = relationship("Membre")
    machine = relationship("Machine")

class Activite(Base):
    __tablename__ = "activite"
    id_activite = Column(Integer, primary_key=True)
    nom = Column(String(100), unique=True, nullable=False)
    description = Column(String, nullable=False)
    pratique = relationship("Pratique")
    salle_activite = relationship("SalleActivite")
    specialisation = relationship("Specialisation")

class SalleActivite(Base):
    __tablename__ = "salle_activite"
    id_salle = Column(Integer, ForeignKey("salle.id_salle"), primary_key=True)
    id_activite = Column(Integer, ForeignKey("activite.id_activite"), primary_key=True)
    salle = relationship("Salle")
    activite = relationship("Activite")

class Pratique(Base):
    __tablename__ = "pratique"
    id_membre = Column(Integer, ForeignKey("membre.id_membre"), primary_key=True)
    id_activite = Column(Integer, ForeignKey("activite.id_activite"), primary_key=True)
    membre = relationship("Membre")
    activite = relationship("Activite")

class Specialisation(Base):
    __tablename__ = "specialisation"
    id_coach = Column(Integer, ForeignKey("coach.id_coach"), primary_key=True)
    id_activite = Column(Integer, ForeignKey("activite.id_activite"), primary_key=True)
    activite = relationship("Activite")
    coach = relationship("Coach")

class Capteur(Base):
    __tablename__ = "capteur"
    id_capteur = Column(Integer, primary_key=True, autoincrement=True)
    id_salle = Column(Integer, ForeignKey("salle.id_salle"), nullable=False)
    type_capteur = Column(String(50), nullable=False)
    valeur = Column(DECIMAL(5,2), nullable=False)
    date_mesure = Column(DateTime, nullable=False)
    salle = relationship("Salle")

class Coach(Base):
    __tablename__ = "coach"
    id_coach = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String(100), nullable=False)
    prenom = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    membre = relationship("Membre")
    specialisation = relationship("Specialisation")

# Connexion à la base de données
def init_db():
    DATABASE_URL = "sqlite:///euro_fit_and_sweat.db"
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

if __name__ == "__main__":
    session = init_db()
    #session.close()

