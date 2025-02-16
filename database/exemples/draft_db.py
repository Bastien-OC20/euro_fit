from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Text, DateTime, Numeric
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()



# -----------------
# Table: Coach
# -----------------
class Coach(Base):
    __tablename__ = "Coach"

    id_coach = Column(Integer, primary_key=True)
    nom = Column(String(50), nullable=False)
    prenom = Column(String(50), nullable=False)
    email = Column(String(255), nullable=False, unique=True)

    # Relations One-to-Many
    membres = relationship("Membre", back_populates="coach")
    specialisations = relationship("Specialisation", back_populates="coach")

# -----------------
# Table: Abonnement
# -----------------
class Abonnement(Base):
    __tablename__ = "Abonnement"

    id_abonnement = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False, unique=True)
    description = Column(Text)
    tarif = Column(Numeric(6, 2), nullable=False)

    # Relation Many-to-Many via la table "souscrit"
    souscriptions = relationship("Souscrit", back_populates="abonnement")

# -----------------
# Table: Médecin
# -----------------
class Medecin(Base):
    __tablename__ = "Médecin"

    id_medecin = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    prenom = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    telephone = Column(String(20), nullable=False)

    # Relation One-to-Many vers Membre
    membres = relationship("Membre", back_populates="medecin")

# -----------------
# Table: Transaction
# -----------------
class Transaction(Base):
    __tablename__ = "Transaction"

    id_transaction = Column(Integer, primary_key=True)
    date_paiement = Column(DateTime, nullable=False)
    montant = Column(Numeric(8, 2), nullable=False)

    # Relation Many-to-Many via la table "Paiement"
    paiements = relationship("Paiement", back_populates="transaction")

# -----------------
# Table: Salle
# -----------------
class Salle(Base):
    __tablename__ = "Salle"

    id_salle = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    type_salle = Column(String(50), nullable=False)
    superficie_m_ = Column(Integer, nullable=False)

    # Relations One-to-Many
    machines = relationship("Machine", back_populates="salle")
    capteurs = relationship("Capteur", back_populates="salle")
    equipements = relationship("Equipement", back_populates="salle")

    # Relation Many-to-Many
    activites_salle = relationship("SalleActivite", back_populates="salle")

    # Relation Many-to-Many via Club_Salle
    clubs_salle = relationship("ClubSalle", back_populates="salle")

# -----------------
# Table: Machine
# -----------------
class Machine(Base):
    __tablename__ = "Machine"

    id_machine = Column(Integer, primary_key=True)
    type_machine = Column(String(50), nullable=False)
    marque = Column(String(100), nullable=False)
    etat = Column(String(50), nullable=False)
    num_serie = Column(String(50), nullable=False)
    id_salle = Column(Integer, ForeignKey("Salle.id_salle"), nullable=False)

    # Relation Many-to-One
    salle = relationship("Salle", back_populates="machines")

    # Relation One-to-Many (association) via UtilisationMachine
    utilisations_membres = relationship("UtilisationMachine", back_populates="machine")

# -----------------
# Table: Capteur
# -----------------
class Capteur(Base):
    __tablename__ = "Capteur"

    id_capteur = Column(Integer, primary_key=True)
    type_capteur = Column(String(50), nullable=False)
    valeur = Column(Numeric(5, 2), nullable=False)
    date_mesure = Column(DateTime, nullable=False)
    id_salle = Column(Integer, ForeignKey("Salle.id_salle"), nullable=False)

    # Relation Many-to-One
    salle = relationship("Salle", back_populates="capteurs")

# -----------------
# Table: Pays
# -----------------
class Pays(Base):
    __tablename__ = "Pays"

    id_pays = Column(Integer, primary_key=True)
    nom_pays = Column(String(50), nullable=False)

    # Relation One-to-Many via Ville
    villes = relationship("Ville", back_populates="pays")

# -----------------
# Table: Activité
# -----------------
class Activite(Base):
    __tablename__ = "Activité"

    id_activite = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False, unique=True)
    description = Column(Text, nullable=False)

    # Relations Many-to-Many
    specialisations = relationship("Specialisation", back_populates="activite")
    pratiques = relationship("Pratique", back_populates="activite")
    salles_activite = relationship("SalleActivite", back_populates="activite")

# -----------------
# Table: Équipement
# -----------------
class Equipement(Base):
    __tablename__ = "Équipement"

    id_equipement = Column(Integer, primary_key=True)
    type_equipement = Column(String(50), nullable=False)
    marque = Column(String(50), nullable=False)
    etat = Column(String(50), nullable=False)
    id_salle = Column(Integer, ForeignKey("Salle.id_salle"), nullable=False)

    # Relation Many-to-One
    salle = relationship("Salle", back_populates="equipements")

# -----------------
# Table: Ville
# -----------------
class Ville(Base):
    __tablename__ = "Ville"

    id_ville = Column(Integer, primary_key=True)
    nom_ville = Column(String(50))
    id_pays = Column(Integer, ForeignKey("Pays.id_pays"))

    # Relation Many-to-One
    pays = relationship("Pays", back_populates="villes")

    # Relation One-to-Many via CodePostal
    codes_postaux = relationship("CodePostal", back_populates="ville")

# -----------------
# Table: Membre
# -----------------
class Membre(Base):
    __tablename__ = "Membre"

    id_membre = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    prenom = Column(String(100), nullable=False)
    date_naissance = Column(Date, nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    telephone = Column(String(20), nullable=False)
    numero_licence = Column(String(50), nullable=False, unique=True)
    id_medecin = Column(Integer, ForeignKey("Médecin.id_medecin"), nullable=False)
    id_coach = Column(Integer, ForeignKey("Coach.id_coach"), nullable=False)

    # Relations Many-to-One
    medecin = relationship("Medecin", back_populates="membres")
    coach = relationship("Coach", back_populates="membres")

    # Relations One-to-Many
    analyses = relationship("AnalyseCorporelle", back_populates="membre")
    adresses = relationship("Adresse", back_populates="membre")

    # Relation Many-to-Many via Paiement
    paiements = relationship("Paiement", back_populates="membre")

    # Relation Many-to-Many via Pratique
    pratiques = relationship("Pratique", back_populates="membre")

    # Relation Many-to-Many via UtilisationMachine
    utilisations_machines = relationship("UtilisationMachine", back_populates="membre")

    # Relation Many-to-Many via souscrit
    souscriptions = relationship("Souscrit", back_populates="membre")

# -----------------
# Table: Analyse_Corporelle
# -----------------
class AnalyseCorporelle(Base):
    __tablename__ = "Analyse_Corporelle"

    id_analyse = Column(Integer, primary_key=True)
    date_analyse = Column(Date, nullable=False)
    IMC = Column(Numeric(5, 2), nullable=False)
    metabolisme_base = Column(Numeric(5, 2), nullable=False)
    masse_grasse = Column(Numeric(5, 2), nullable=False)
    masse_musculaire = Column(Numeric(5, 2), nullable=False)
    id_membre = Column(Integer, ForeignKey("Membre.id_membre"), nullable=False)

    # Relation Many-to-One
    membre = relationship("Membre", back_populates="analyses")

# -----------------
# Table: Code_postal
# -----------------
class CodePostal(Base):
    __tablename__ = "Code_postal"

    id_code_postal = Column(Integer, primary_key=True)
    code_postal = Column(String(11), nullable=False)
    id_ville = Column(Integer, ForeignKey("Ville.id_ville"))

    # Relation Many-to-One
    ville = relationship("Ville", back_populates="codes_postaux")

    # Relation One-to-Many
    adresses = relationship("Adresse", back_populates="code_postal")

# -----------------
# Table: Adresse
# -----------------
class Adresse(Base):
    __tablename__ = "Adresse"

    id_adresse = Column(Integer, primary_key=True)
    numero_rue = Column(Integer)
    nom_rue = Column(String(50))
    id_membre = Column(Integer, ForeignKey("Membre.id_membre"))
    id_code_postal = Column(Integer, ForeignKey("Code_postal.id_code_postal"))

    # Relations Many-to-One
    membre = relationship("Membre", back_populates="adresses")
    code_postal = relationship("CodePostal", back_populates="adresses")

    # Relation One-to-Many
    assurances = relationship("Assurance", back_populates="adresse")
    clubs = relationship("Club", back_populates="adresse")

# -----------------
# Table: Assurance
# -----------------
class Assurance(Base):
    __tablename__ = "Assurance"

    id_assurance = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    telephone = Column(String(20), nullable=False)
    id_adresse = Column(Integer, ForeignKey("Adresse.id_adresse"))

    # Relation Many-to-One
    adresse = relationship("Adresse", back_populates="assurances")

    # Relation One-to-Many
    clubs = relationship("Club", back_populates="assurance")

# -----------------
# Table: Club
# -----------------
class Club(Base):
    __tablename__ = "Club"

    id_club = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False, unique=True)
    surface_m_ = Column(Integer, nullable=False)
    nb_salles = Column(Integer, nullable=False)
    nb_machines = Column(Integer, nullable=False)
    id_adresse = Column(Integer, ForeignKey("Adresse.id_adresse"), nullable=False)
    id_assurance = Column(Integer, ForeignKey("Assurance.id_assurance"), nullable=False)

    # Relations Many-to-One
    adresse = relationship("Adresse", back_populates="clubs")
    assurance = relationship("Assurance", back_populates="clubs")

    # Relations One-to-Many
    agents_securite = relationship("AgentSecurite", back_populates="club")
    agents_nettoyage = relationship("AgentNettoyage", back_populates="club")

    # Relation Many-to-Many via Club_Salle (anciennement Asso_26)
    salles_club = relationship("ClubSalle", back_populates="club")

    # Relation Many-to-Many via souscrit
    souscriptions_club = relationship("Souscrit", back_populates="club")

# -----------------
# Table: Agent_Sécurité
# -----------------
class AgentSecurite(Base):
    __tablename__ = "Agent_Sécurité"

    id_agent_secu = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    prenom = Column(String(100), nullable=False)
    telephone = Column(String(20), nullable=False)
    id_club = Column(Integer, ForeignKey("Club.id_club"), nullable=False)

    # Relation Many-to-One
    club = relationship("Club", back_populates="agents_securite")

# -----------------
# Table: Agent_Nettoyage
# -----------------
class AgentNettoyage(Base):
    __tablename__ = "Agent_Nettoyage"

    id_agent_nettoyage = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    prenom = Column(String(100), nullable=False)
    telephone = Column(String(20), nullable=False)
    id_club = Column(Integer, ForeignKey("Club.id_club"), nullable=False)

    # Relation Many-to-One
    club = relationship("Club", back_populates="agents_nettoyage")

# -----------------
# Table de liaison: Utilisation_Machine
# (Many-to-Many entre Membre et Machine, avec champs supplémentaires)
# -----------------
class UtilisationMachine(Base):
    __tablename__ = "Utilisation_Machine"

    id_membre = Column(Integer, ForeignKey("Membre.id_membre"), primary_key=True)
    id_machine = Column(Integer, ForeignKey("Machine.id_machine"), primary_key=True)
    date_utilisation = Column(DateTime, nullable=False)
    duree_minute = Column(Integer, nullable=False)

    # Relations Many-to-One
    membre = relationship("Membre", back_populates="utilisations_machines")
    machine = relationship("Machine", back_populates="utilisations_membres")

# -----------------
# Table de liaison: Paiement
# (Many-to-Many entre Membre et Transaction)
# -----------------
class Paiement(Base):
    __tablename__ = "Paiement"

    id_membre = Column(Integer, ForeignKey("Membre.id_membre"), primary_key=True)
    id_transaction = Column(Integer, ForeignKey("Transaction.id_transaction"), primary_key=True)

    # Relations Many-to-One
    membre = relationship("Membre", back_populates="paiements")
    transaction = relationship("Transaction", back_populates="paiements")

# -----------------
# Table de liaison: Spécialisation
# (Many-to-Many entre Coach et Activité)
# -----------------
class Specialisation(Base):
    __tablename__ = "Spécialisation"

    id_coach = Column(Integer, ForeignKey("Coach.id_coach"), primary_key=True)
    id_activite = Column(Integer, ForeignKey("Activité.id_activite"), primary_key=True)

    # Relations Many-to-One
    coach = relationship("Coach", back_populates="specialisations")
    activite = relationship("Activite", back_populates="specialisations")

# -----------------
# Table de liaison: Pratique
# (Many-to-Many entre Membre et Activité)
# -----------------
class Pratique(Base):
    __tablename__ = "Pratique"

    id_membre = Column(Integer, ForeignKey("Membre.id_membre"), primary_key=True)
    id_activite = Column(Integer, ForeignKey("Activité.id_activite"), primary_key=True)

    # Relations Many-to-One
    membre = relationship("Membre", back_populates="pratiques")
    activite = relationship("Activite", back_populates="pratiques")

# -----------------
# Table de liaison: Salle_Activité
# (Many-to-Many entre Salle et Activité)
# -----------------
class SalleActivite(Base):
    __tablename__ = "Salle_Activité"

    id_salle = Column(Integer, ForeignKey("Salle.id_salle"), primary_key=True)
    id_activite = Column(Integer, ForeignKey("Activité.id_activite"), primary_key=True)

    # Relations Many-to-One
    salle = relationship("Salle", back_populates="activites_salle")
    activite = relationship("Activite", back_populates="salles_activite")

# -----------------
# Table de liaison renommée: Club_Salle
# (Many-to-Many entre Club et Salle) 
# (anciennement Asso_26)
# -----------------
class ClubSalle(Base):
    __tablename__ = "Club_Salle"

    id_club = Column(Integer, ForeignKey("Club.id_club"), primary_key=True)
    id_salle = Column(Integer, ForeignKey("Salle.id_salle"), primary_key=True)

    # Relations Many-to-One
    club = relationship("Club", back_populates="salles_club")
    salle = relationship("Salle", back_populates="clubs_salle")

# -----------------
# Table de liaison: souscrit
# (Many-to-Many entre Membre, Abonnement, Club avec champs supplémentaires)
# -----------------
class Souscrit(Base):
    __tablename__ = "souscrit"

    id_membre = Column(Integer, ForeignKey("Membre.id_membre"), primary_key=True)
    id_abonnement = Column(Integer, ForeignKey("Abonnement.id_abonnement"), primary_key=True)
    id_club = Column(Integer, ForeignKey("Club.id_club"), primary_key=True)
    duree_mois = Column(Numeric(15, 2), nullable=False)
    date_inscription = Column(Date, nullable=False)

    # Relations Many-to-One
    membre = relationship("Membre", back_populates="souscriptions")
    abonnement = relationship("Abonnement", back_populates="souscriptions")
    club = relationship("Club", back_populates="souscriptions_club")


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

