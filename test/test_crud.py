import pytest
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.models import Base, Coach, Membre
from api.crud import (
    create_coach, get_coach, update_coach, delete_coach,
    create_membre, get_membre, update_membre, delete_membre,
    create_medecin, delete_medecin
)

# URL de la base de données de test (SQLite)
DATABASE_URL = "sqlite:///./database/db/test_euro_fit.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def db():
    # Création des tables de test
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)

def test_create_read_update_delete_coach(db):
    # Création d'un coach
    coach = create_coach(db, "TestNom", "TestPrenom", "test@example.com")
    assert coach.id_coach is not None

    # Lecture du coach
    coach_read = get_coach(db, coach.id_coach)
    assert coach_read.email == "test@example.com"

    # Mise à jour du coach
    coach_updated = update_coach(db, coach.id_coach, email="new@example.com")
    assert coach_updated.email == "new@example.com"

    # Suppression du coach
    deleted_coach = delete_coach(db, coach.id_coach)
    assert deleted_coach is not None

    # Vérification de la suppression
    assert get_coach(db, coach.id_coach) is None

def test_create_read_update_delete_membre(db):
    # Pour créer un membre, on a besoin d'un medecin et d'un coach (clés étrangères)
    medecin = create_medecin(db, "MedecinNom", "MedecinPrenom", "med@example.com", "0123456789")
    coach = create_coach(db, "CoachNom", "CoachPrenom", "coach@example.com")

    # Création d'un membre
    date_naissance = datetime.date(1990, 1, 1)
    membre = create_membre(
        db,
        "MembreNom",
        "MembrePrenom",
        date_naissance,
        "membre@example.com",
        "0987654321",
        "LIC123",
        medecin.id_medecin,
        coach.id_coach
    )
    assert membre.id_membre is not None

    # Lecture du membre
    membre_read = get_membre(db, membre.id_membre)
    assert membre_read.email == "membre@example.com"

    # Mise à jour du membre
    membre_updated = update_membre(db, membre.id_membre, email="membre_new@example.com")
    assert membre_updated.email == "membre_new@example.com"

    # Suppression du membre
    deleted_membre = delete_membre(db, membre.id_membre)
    assert deleted_membre is not None
    assert get_membre(db, membre.id_membre) is None

    # Nettoyage : suppression du medecin et du coach créés pour le test
    delete_medecin(db, medecin.id_medecin)
    delete_coach(db, coach.id_coach)