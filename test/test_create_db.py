import os
import sys
import time
import pytest
from sqlalchemy import create_engine, inspect

# Ajouter le dossier parent pour que le package "database" soit trouvé
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from database.create_db import init_db

DATABASE_PATH = "./database/db/euro_fit.db"
DATABASE_URL = "sqlite:///./database/db/euro_fit.db"

@pytest.fixture(scope="module", autouse=True)
def setup_db():
    # Si le fichier existe, tenter de le supprimer avec plusieurs essais
    if os.path.exists(DATABASE_PATH):
        for _ in range(10):
            try:
                os.remove(DATABASE_PATH)
                break
            except PermissionError:
                engine = create_engine(DATABASE_URL)
                engine.dispose()
                time.sleep(0.5)
        else:
            pytest.skip("Impossible de supprimer le fichier de base de données verrouillé.")
    # Initialiser la base de données
    session = init_db()
    yield session
    session.close()

def test_database_file_created():
    """Test que le fichier de base de données a bien été créé."""
    assert os.path.exists(DATABASE_PATH), "Le fichier de base de données n'a pas été créé."

def test_tables_created():
    """Test que toutes les tables attendues ont été créées."""
    engine = create_engine(DATABASE_URL)
    inspector = inspect(engine)
    expected_tables = [
        "Coach",
        "Abonnement",
        "Médecin",
        "Transaction",
        "Salle",
        "Machine",
        "Capteur",
        "Pays",
        "Activité",
        "Équipement",
        "Ville",
        "Membre",
        "Analyse_Corporelle",
        "Code_postal",
        "Adresse",
        "Assurance",
        "Club",
        "Agent_Sécurité",
        "Agent_Nettoyage",
        "Utilisation_Machine",
        "Paiement",
        "Spécialisation",
        "Pratique",
        "Salle_Activité",
        "Club_Salle",
        "souscrit"
    ]
    actual_tables = inspector.get_table_names()
    for table in expected_tables:
        assert table in actual_tables, f"La table '{table}' n'a pas été trouvée. Tables présentes: {actual_tables}"