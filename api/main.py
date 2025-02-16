from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List, Optional
import datetime
from pydantic import BaseModel

# Import des fonctions CRUD et des modèles
from .crud import (
    get_coach, create_coach, update_coach, delete_coach,
    get_membre, create_membre, update_membre, delete_membre, get_all
)
from .models import Coach, Membre
from .database import SessionLocal
from .schemas import CoachCreate, CoachUpdate, CoachOut, MembreCreate, MembreUpdate, MembreOut

app = FastAPI(title="Euro Fit API", version="1.0")

# Dépendance pour la session de base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoints pour la racine
@app.get("/")  # GET /
def read_root():
    return {"message": "Bienvenue sur l'API Euro Fit"}


# Endpoints pour Coach
@app.get("/coaches/", response_model=List[CoachOut])
def read_coaches(db: Session = Depends(get_db)):
    coaches = get_all(db, Coach)
    return coaches

@app.get("/coaches/{coach_id}", response_model=CoachOut)
def read_coach(coach_id: int, db: Session = Depends(get_db)):
    coach = get_coach(db, coach_id)
    if not coach:
        raise HTTPException(status_code=404, detail="Coach non trouvé")
    return coach

@app.post("/coaches/", response_model=CoachOut)
def create_new_coach(coach: CoachCreate, db: Session = Depends(get_db)):
    new_coach = create_coach(db, coach.nom, coach.prenom, coach.email)
    return new_coach

@app.put("/coaches/{coach_id}", response_model=CoachOut)
def update_existing_coach(coach_id: int, coach_update: CoachUpdate, db: Session = Depends(get_db)):
    updated_coach = update_coach(db, coach_id, **coach_update.dict(exclude_unset=True))
    if not updated_coach:
        raise HTTPException(status_code=404, detail="Coach non trouvé")
    return updated_coach

@app.delete("/coaches/{coach_id}", response_model=CoachOut)
def delete_existing_coach(coach_id: int, db: Session = Depends(get_db)):
    deleted_coach = delete_coach(db, coach_id)
    if not deleted_coach:
        raise HTTPException(status_code=404, detail="Coach non trouvé")
    return deleted_coach

# Endpoints pour Membre
@app.get("/membres/", response_model=List[MembreOut])
def read_membres(db: Session = Depends(get_db)):
    membres = get_all(db, Membre)
    return membres

@app.get("/membres/{membre_id}", response_model=MembreOut)
def read_membre(membre_id: int, db: Session = Depends(get_db)):
    membre = get_membre(db, membre_id)
    if not membre:
        raise HTTPException(status_code=404, detail="Membre non trouvé")
    return membre

@app.post("/membres/", response_model=MembreOut)
def create_new_membre(membre: MembreCreate, db: Session = Depends(get_db)):
    new_membre = create_membre(db, membre.nom, membre.prenom, membre.date_naissance, membre.email,
                               membre.telephone, membre.numero_licence, membre.id_medecin, membre.id_coach)
    return new_membre

@app.put("/membres/{membre_id}", response_model=MembreOut)
def update_existing_membre(membre_id: int, membre_update: MembreUpdate, db: Session = Depends(get_db)):
    updated_membre = update_membre(db, membre_id, **membre_update.dict(exclude_unset=True))
    if not updated_membre:
        raise HTTPException(status_code=404, detail="Membre non trouvé")
    return updated_membre

@app.delete("/membres/{membre_id}", response_model=MembreOut)
def delete_existing_membre(membre_id: int, db: Session = Depends(get_db)):
    deleted_membre = delete_membre(db, membre_id)
    if not deleted_membre:
        raise HTTPException(status_code=404, detail="Membre non trouvé")
    return deleted_membre