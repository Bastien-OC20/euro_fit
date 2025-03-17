from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session, sessionmaker
from typing import List
from pydantic import BaseModel
from models import Coach, Base  # Import the Coach model and Base from models.py
from db_setup import engine       # Import the database engine setup

# Create a session factory for managing database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Initialize the FastAPI application
app = FastAPI(title="CRUD API for Coach Model")

# Dependency to provide a database session for each request
def get_db():
    db = SessionLocal()  # Create a new session
    try:
        yield db  # Provide the session
    finally:
        db.close()  # Ensure the session is closed after the request

# ------------------------------
# Pydantic Schemas (Data Validation)
# ------------------------------

class CoachBase(BaseModel):
    """
    Defines the basic structure of a Coach object.
    """
    nom: str
    prenom: str
    email: str

class CoachCreate(CoachBase):
    """
    Schema for creating a new coach.
    Inherits from CoachBase.
    """
    pass  # No additional fields

class CoachResponse(CoachBase):
    """
    Schema for returning a coach, including the ID.
    """
    id_coach: int

    class Config:
        orm_mode = True  # Enables compatibility with SQLAlchemy models

# ------------------------------
# CRUD Endpoints
# ------------------------------

@app.get("/coaches", response_model=List[CoachResponse])
def read_coaches(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of coaches with optional pagination.
    """
    coaches = db.query(Coach).offset(skip).limit(limit).all()
    return coaches

@app.post("/coaches", response_model=CoachResponse)
def create_coach(coach: CoachCreate, db: Session = Depends(get_db)):
    """
    Create a new coach and store it in the database.
    """
    db_coach = Coach(nom=coach.nom, prenom=coach.prenom, email=coach.email)  # Create a new Coach object
    db.add(db_coach)  # Add to the session
    db.commit()  # Commit to save in the database
    db.refresh(db_coach)  # Refresh to get the latest data
    return db_coach

@app.put("/coaches/{coach_id}", response_model=CoachResponse)
def update_coach(coach_id: int, coach: CoachCreate, db: Session = Depends(get_db)):
    """
    Update an existing coach's information by ID.
    """
    db_coach = db.query(Coach).filter(Coach.id_coach == coach_id).first()  # Find the coach
    if db_coach is None:
        raise HTTPException(status_code=404, detail="Coach not found")  # Return 404 if not found
    # Update coach details
    db_coach.nom = coach.nom
    db_coach.prenom = coach.prenom
    db_coach.email = coach.email
    db.commit()  # Save changes
    db.refresh(db_coach)  # Refresh updated data
    return db_coach

@app.delete("/coaches/{coach_id}")
def delete_coach(coach_id: int, db: Session = Depends(get_db)):
    """
    Delete a coach from the database by ID.
    """
    db_coach = db.query(Coach).filter(Coach.id_coach == coach_id).first()  # Find the coach
    if db_coach is None:
        raise HTTPException(status_code=404, detail="Coach not found")  # Return 404 if not found
    db.delete(db_coach)  # Delete the coach
    db.commit()  # Save the deletion
    return {"detail": "Coach deleted successfully"}  # Return
