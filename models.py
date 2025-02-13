from sqlalchemy import create_engine, Column, Integer, String, Numeric, ForeignKey, Date, DateTime, Text
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# ------------------------------
# Table: Coach
# ------------------------------
class Coach(Base):
    __tablename__ = 'coach'
    id_coach = Column(Integer, primary_key=True)
    nom = Column(String(50), nullable=False)
    prenom = Column(String(50), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    
    specialisations = relationship("Specialisation", back_populates="coach")
    membres = relationship("Membre", back_populates="coach")


# ------------------------------
# Table: Abonnement
# ------------------------------
class Abonnement(Base):
    __tablename__ = 'abonnement'
    id_abonnement = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False, unique=True)
    description = Column(Text)
    tarif = Column(Numeric(6, 2), nullable=False)
    
    souscriptions = relationship("Souscrit", back_populates="abonnement")


# ------------------------------
# Table: Medecin
# ------------------------------
class Medecin(Base):
    __tablename__ = 'medecin'
    id_medecin = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    prenom = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    telephone = Column(String(20), nullable=False)
    
    membres = relationship("Membre", back_populates="medecin")


# ------------------------------
# Table: Transaction
# ------------------------------
class Transaction(Base):
    __tablename__ = 'transaction'
    id_transaction = Column(Integer, primary_key=True)
    date_paiement = Column(DateTime, nullable=False)
    montant = Column(Numeric(8, 2), nullable=False)
    
    paiements = relationship("Paiement", back_populates="transaction")


# ------------------------------
# Table: Salle
# ------------------------------
class Salle(Base):
    __tablename__ = 'salle'
    id_salle = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    type_salle = Column(String(50), nullable=False)
    superficie_m = Column(Integer, nullable=False)
    
    machines = relationship("Machine", back_populates="salle")
    capteurs = relationship("Capteur", back_populates="salle")
    equipements = relationship("Equipement", back_populates="salle")
    activite_assoc = relationship("SalleActivite", back_populates="salle")
    clubs_assoc = relationship("Asso26", back_populates="salle")


# ------------------------------
# Table: Machine
# ------------------------------
class Machine(Base):
    __tablename__ = 'machine'
    id_machine = Column(Integer, primary_key=True)
    type_machine = Column(String(50), nullable=False)
    marque = Column(String(100), nullable=False)
    etat = Column(String(50), nullable=False)
    num_serie = Column(String(50), nullable=False)
    id_salle = Column(Integer, ForeignKey('salle.id_salle'), nullable=False)
    
    salle = relationship("Salle", back_populates="machines")
    utilisations = relationship("UtilisationMachine", back_populates="machine")


# ------------------------------
# Table: Capteur
# ------------------------------
class Capteur(Base):
    __tablename__ = 'capteur'
    id_capteur = Column(Integer, primary_key=True)
    type_capteur = Column(String(50), nullable=False)
    valeur = Column(Numeric(5, 2), nullable=False)
    date_mesure = Column(DateTime, nullable=False)
    id_salle = Column(Integer, ForeignKey('salle.id_salle'), nullable=False)
    
    salle = relationship("Salle", back_populates="capteurs")


# ------------------------------
# Table: Pays
# ------------------------------
class Pays(Base):
    __tablename__ = 'pays'
    id_pays = Column(Integer, primary_key=True)
    nom_pays = Column(String(50), nullable=False)
    
    villes = relationship("Ville", back_populates="pays")


# ------------------------------
# Table: Activite
# ------------------------------
class Activite(Base):
    __tablename__ = 'activite'
    id_activite = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False, unique=True)
    description = Column(Text, nullable=False)
    
    specialisations = relationship("Specialisation", back_populates="activite")
    pratiques = relationship("Pratique", back_populates="activite")
    salle_assoc = relationship("SalleActivite", back_populates="activite")


# ------------------------------
# Table: Equipement
# ------------------------------
class Equipement(Base):
    __tablename__ = 'equipement'
    id_equipement = Column(Integer, primary_key=True)
    type_equipement = Column(String(50), nullable=False)
    marque = Column(String(50), nullable=False)
    etat = Column(String(50), nullable=False)
    id_salle = Column(Integer, ForeignKey('salle.id_salle'), nullable=False)
    
    salle = relationship("Salle", back_populates="equipements")


# ------------------------------
# Table: Ville
# ------------------------------
class Ville(Base):
    __tablename__ = 'ville'
    id_ville = Column(Integer, primary_key=True)
    nom_ville = Column(String(50))
    id_pays = Column(Integer, ForeignKey('pays.id_pays'))
    
    pays = relationship("Pays", back_populates="villes")
    codes_postaux = relationship("CodePostal", back_populates="ville")


# ------------------------------
# Table: Membre
# ------------------------------
class Membre(Base):
    __tablename__ = 'membre'
    id_membre = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    prenom = Column(String(100), nullable=False)
    date_naissance = Column(Date, nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    telephone = Column(String(20), nullable=False)
    numero_licence = Column(String(50), nullable=False, unique=True)
    id_medecin = Column(Integer, ForeignKey('medecin.id_medecin'), nullable=False)
    id_coach = Column(Integer, ForeignKey('coach.id_coach'), nullable=False)
    
    medecin = relationship("Medecin", back_populates="membres")
    coach = relationship("Coach", back_populates="membres")
    analyses = relationship("AnalyseCorporelle", back_populates="membre")
    adresses = relationship("Adresse", back_populates="membre")
    paiements = relationship("Paiement", back_populates="membre")
    pratiques = relationship("Pratique", back_populates="membre")
    souscriptions = relationship("Souscrit", back_populates="membre")
    utilisations = relationship("UtilisationMachine", back_populates="membre")


# ------------------------------
# Table: AnalyseCorporelle
# ------------------------------
class AnalyseCorporelle(Base):
    __tablename__ = 'analyse_corporelle'
    id_analyse = Column(Integer, primary_key=True)
    date_analyse = Column(Date, nullable=False)
    IMC = Column(Numeric(5, 2), nullable=False)
    metabolisme_base = Column(Numeric(5, 2), nullable=False)
    masse_grasse = Column(Numeric(5, 2), nullable=False)
    masse_musculaire = Column(Numeric(5, 2), nullable=False)
    id_membre = Column(Integer, ForeignKey('membre.id_membre'), nullable=False)
    
    membre = relationship("Membre", back_populates="analyses")


# ------------------------------
# Table: CodePostal
# ------------------------------
class CodePostal(Base):
    __tablename__ = 'code_postal'
    id_code_postal = Column(Integer, primary_key=True)
    code_postal = Column(String(20), nullable=False)  
    id_ville = Column(Integer, ForeignKey('ville.id_ville'), nullable=False)
    
    ville = relationship("Ville", back_populates="codes_postaux")
    adresses = relationship("Adresse", back_populates="code_postal")


# ------------------------------
# Table: Adresse
# ------------------------------
class Adresse(Base):
    __tablename__ = 'adresse'
    id_adresse = Column(Integer, primary_key=True)
    numero_rue = Column(Integer)
    nom_rue = Column(String(50))
    id_membre = Column(Integer, ForeignKey('membre.id_membre'))
    id_code_postal = Column(Integer, ForeignKey('code_postal.id_code_postal'))
    
    membre = relationship("Membre", back_populates="adresses")
    code_postal = relationship("CodePostal", back_populates="adresses")
    assurances = relationship("Assurance", back_populates="adresse")
    clubs = relationship("Club", back_populates="adresse")


# ------------------------------
# Table: Assurance
# ------------------------------
class Assurance(Base):
    __tablename__ = 'assurance'
    id_assurance = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    telephone = Column(String(20), nullable=False)
    id_adresse = Column(Integer, ForeignKey('adresse.id_adresse'))
    
    adresse = relationship("Adresse", back_populates="assurances")
    clubs = relationship("Club", back_populates="assurance")


# ------------------------------
# Table: Club
# ------------------------------
class Club(Base):
    __tablename__ = 'club'
    id_club = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False, unique=True)
    surface_m = Column(Integer, nullable=False)
    nb_salles = Column(Integer, nullable=False)
    nb_machines = Column(Integer, nullable=False)
    id_adresse = Column(Integer, ForeignKey('adresse.id_adresse'), nullable=False)
    id_assurance = Column(Integer, ForeignKey('assurance.id_assurance'), nullable=False)
    
    adresse = relationship("Adresse", back_populates="clubs")
    assurance = relationship("Assurance", back_populates="clubs")
    agents_securite = relationship("AgentSecurite", back_populates="club")
    agents_nettoyage = relationship("AgentNettoyage", back_populates="club")
    souscriptions = relationship("Souscrit", back_populates="club")
    clubs_assoc = relationship("Asso26", back_populates="club")


# ------------------------------
# Table: AgentSecurite
# ------------------------------
class AgentSecurite(Base):
    __tablename__ = 'agent_securite'
    id_agent_secu = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    prenom = Column(String(100), nullable=False)
    telephone = Column(String(20), nullable=False)
    id_club = Column(Integer, ForeignKey('club.id_club'), nullable=False)
    
    club = relationship("Club", back_populates="agents_securite")


# ------------------------------
# Table: AgentNettoyage
# ------------------------------
class AgentNettoyage(Base):
    __tablename__ = 'agent_nettoyage'
    id_agent_nettoyage = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    prenom = Column(String(100), nullable=False)
    telephone = Column(String(20), nullable=False)
    id_club = Column(Integer, ForeignKey('club.id_club'), nullable=False)
    
    club = relationship("Club", back_populates="agents_nettoyage")


# ------------------------------
# Table: UtilisationMachine
# ------------------------------
class UtilisationMachine(Base):
    __tablename__ = 'utilisation_machine'
    id_membre = Column(Integer, ForeignKey('membre.id_membre'), primary_key=True)
    id_machine = Column(Integer, ForeignKey('machine.id_machine'), primary_key=True)
    date_utilisation = Column(DateTime, nullable=False)
    duree_minute = Column(Integer, nullable=False)
    
    membre = relationship("Membre", back_populates="utilisations")
    machine = relationship("Machine", back_populates="utilisations")


# ------------------------------
# Table: Paiement
# ------------------------------
class Paiement(Base):
    __tablename__ = 'paiement'
    id_membre = Column(Integer, ForeignKey('membre.id_membre'), primary_key=True)
    id_transaction = Column(Integer, ForeignKey('transaction.id_transaction'), primary_key=True)
    
    membre = relationship("Membre", back_populates="paiements")
    transaction = relationship("Transaction", back_populates="paiements")


# ------------------------------
# Table: Specialisation
# ------------------------------
class Specialisation(Base):
    __tablename__ = 'specialisation'
    id_coach = Column(Integer, ForeignKey('coach.id_coach'), primary_key=True)
    id_activite = Column(Integer, ForeignKey('activite.id_activite'), primary_key=True)
    
    coach = relationship("Coach", back_populates="specialisations")
    activite = relationship("Activite", back_populates="specialisations")


# ------------------------------
# Table: Pratique
# ------------------------------
class Pratique(Base):
    __tablename__ = 'pratique'
    id_membre = Column(Integer, ForeignKey('membre.id_membre'), primary_key=True)
    id_activite = Column(Integer, ForeignKey('activite.id_activite'), primary_key=True)
    
    membre = relationship("Membre", back_populates="pratiques")
    activite = relationship("Activite", back_populates="pratiques")


# ------------------------------
# Table: SalleActivite
# ------------------------------
class SalleActivite(Base):
    __tablename__ = 'salle_activite'
    id_salle = Column(Integer, ForeignKey('salle.id_salle'), primary_key=True)
    id_activite = Column(Integer, ForeignKey('activite.id_activite'), primary_key=True)
    
    salle = relationship("Salle", back_populates="activite_assoc")
    activite = relationship("Activite", back_populates="salle_assoc")


# ------------------------------
# Table: Asso26
# ------------------------------
class Asso26(Base):
    __tablename__ = 'asso26'
    id_club = Column(Integer, ForeignKey('club.id_club'), primary_key=True)
    id_salle = Column(Integer, ForeignKey('salle.id_salle'), primary_key=True)
    
    club = relationship("Club", back_populates="clubs_assoc")
    salle = relationship("Salle", back_populates="clubs_assoc")


# ------------------------------
# Table: Souscrit
# ------------------------------
class Souscrit(Base):
    __tablename__ = 'souscrit'
    id_membre = Column(Integer, ForeignKey('membre.id_membre'), primary_key=True)
    id_abonnement = Column(Integer, ForeignKey('abonnement.id_abonnement'), primary_key=True)
    id_club = Column(Integer, ForeignKey('club.id_club'), primary_key=True)
    duree_mois = Column(Numeric(15, 2), nullable=False)
    date_inscription = Column(Date, nullable=False)
    
    membre = relationship("Membre", back_populates="souscriptions")
    abonnement = relationship("Abonnement", back_populates="souscriptions")
    club = relationship("Club", back_populates="souscriptions")


# ------------------------------
# Database Configuration & Creation
# ------------------------------
DATABASE_URL = "mysql+pymysql://user:password@localhost/euro_fit"  # Update with your credentials
engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(engine)

print("Base de données créée avec succès !")
