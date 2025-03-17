# tests/test_crud.py

from models import Coach

def test_create_coach(session):
    # Create a new coach record
    coach = Coach(nom="Dupont", prenom="Jean", email="jean.dupont@example.com")
    session.add(coach)
    session.commit()
    
    # Retrieve the coach and verify the values
    retrieved = session.query(Coach).filter_by(email="jean.dupont@example.com").first()
    assert retrieved is not None
    assert retrieved.nom == "Dupont"
    assert retrieved.prenom == "Jean"

def test_update_coach(session):
    # Create a new coach record
    coach = Coach(nom="Martin", prenom="Luc", email="luc.martin@example.com")
    session.add(coach)
    session.commit()

    # Update the coach's name
    coach.nom = "UpdatedMartin"
    session.commit()

    # Retrieve the coach and verify the updated name
    updated = session.query(Coach).filter_by(email="luc.martin@example.com").first()
    assert updated.nom == "UpdatedMartin"

def test_delete_coach(session):
    # Create a new coach record
    coach = Coach(nom="Smith", prenom="John", email="john.smith@example.com")
    session.add(coach)
    session.commit()

    # Delete the coach record
    session.delete(coach)
    session.commit()

    # Verify that the record is deleted
    deleted = session.query(Coach).filter_by(email="john.smith@example.com").first()
    assert deleted is None
