from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import date, datetime

# -----------------
# Modèle: Coach
# -----------------
class Coach(BaseModel):
    id_coach: int
    nom: str
    prenom: str
    email: EmailStr

    class Config:
        from_attributes = True

# -----------------
# Modèle: Abonnement
# -----------------
class Abonnement(BaseModel):
    id_abonnement: int
    nom: str
    description: Optional[str] = None
    tarif: float

    class Config:
        from_attributes = True

# -----------------
# Modèle: Médecin
# -----------------
class Medecin(BaseModel):
    id_medecin: int
    nom: str
    prenom: str
    email: EmailStr
    telephone: str

    class Config:
        from_attributes = True

# -----------------
# Modèle: Transaction
# -----------------
class Transaction(BaseModel):
    id_transaction: int
    date_paiement: datetime
    montant: float

    class Config:
        from_attributes = True

# -----------------
# Modèle: Salle
# -----------------
class Salle(BaseModel):
    id_salle: int
    nom: str
    type_salle: str
    superficie_m_: int

    class Config:
        from_attributes = True

# -----------------
# Modèle: Machine
# -----------------
class Machine(BaseModel):
    id_machine: int
    type_machine: str
    marque: str
    etat: str
    num_serie: str
    id_salle: int

    class Config:
        from_attributes = True

# -----------------
# Modèle: Capteur
# -----------------
class Capteur(BaseModel):
    id_capteur: int
    type_capteur: str
    valeur: float
    date_mesure: datetime
    id_salle: int

    class Config:
        from_attributes = True

# -----------------
# Modèle: Pays
# -----------------
class Pays(BaseModel):
    id_pays: int
    nom_pays: str

    class Config:
        from_attributes = True

# -----------------
# Modèle: Activité
# -----------------
class Activite(BaseModel):
    id_activite: int
    nom: str
    description: str

    class Config:
        from_attributes = True

# -----------------
# Modèle: Équipement
# -----------------
class Equipement(BaseModel):
    id_equipement: int
    type_equipement: str
    marque: str
    etat: str
    id_salle: int

    class Config:
        from_attributes = True

# -----------------
# Modèle: Ville
# -----------------
class Ville(BaseModel):
    id_ville: int
    nom_ville: str
    id_pays: int

    class Config:
        from_attributes = True

# -----------------
# Modèle: Membre
# -----------------
class Membre(BaseModel):
    id_membre: int
    nom: str
    prenom: str
    date_naissance: date
    email: EmailStr
    telephone: str
    numero_licence: str
    id_medecin: int
    id_coach: int

    class Config:
        from_attributes = True

# -----------------
# Modèle: Analyse Corporelle
# -----------------
class AnalyseCorporelle(BaseModel):
    id_analyse: int
    date_analyse: date
    IMC: float
    metabolisme_base: float
    masse_grasse: float
    masse_musculaire: float
    id_membre: int

    class Config:
        from_attributes = True

# -----------------
# Modèle: Code Postal
# -----------------
class CodePostal(BaseModel):
    id_code_postal: int
    code_postal: str
    id_ville: int

    class Config:
        from_attributes = True

# -----------------
# Modèle: Adresse
# -----------------
class Adresse(BaseModel):
    id_adresse: int
    numero_rue: Optional[int] = None
    nom_rue: Optional[str] = None
    id_membre: Optional[int] = None
    id_code_postal: Optional[int] = None

    class Config:
        from_attributes = True

# -----------------
# Modèle: Assurance
# -----------------
class Assurance(BaseModel):
    id_assurance: int
    nom: str
    telephone: str
    id_adresse: int

    class Config:
        from_attributes = True
