from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Base, Coach, Medecin, Abonnement, Membre

# ------------------------------
# Database Configuration & Session Setup
# ------------------------------
DATABASE_URL = "sqlite:///euro_fit.db"  # Using SQLite
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# ------------------------------
# Initialize Faker
# ------------------------------
fake = Faker('fr_FR') 

# ------------------------------
# Insert 4 Fake Coach Records
# ------------------------------
coaches = []
for _ in range(4):
    coach = Coach(
        nom=fake.last_name(),
        prenom=fake.first_name(),
        email=fake.unique.email()
    )
    session.add(coach)
    coaches.append(coach)
session.commit()

# ------------------------------
# Insert 4 Fake Medecin Records
# ------------------------------
medecins = []
for _ in range(4):
    medecin = Medecin(
        nom=fake.last_name(),
        prenom=fake.first_name(),
        email=fake.unique.email(),
        telephone=fake.phone_number()
    )
    session.add(medecin)
    medecins.append(medecin)
session.commit()

# ------------------------------
# Insert 4 Fake Abonnement Records
# ------------------------------
abonnements = []
for _ in range(4):
    abonnement = Abonnement(
        nom=fake.unique.word().capitalize(),
        description=fake.sentence(),
        tarif=fake.pydecimal(left_digits=3, right_digits=2, positive=True)
    )
    session.add(abonnement)
    abonnements.append(abonnement)
session.commit()

# ------------------------------
# Insert 4 Fake Membre Records
# ------------------------------
# For simplicity, we assign each Membre the i-th Coach and Medecin created above.
membres = []
for i in range(4):
    membre = Membre(
        nom=fake.last_name(),
        prenom=fake.first_name(),
        date_naissance=fake.date_of_birth(minimum_age=18, maximum_age=65),
        email=fake.unique.email(),
        telephone=fake.phone_number(),
        numero_licence=fake.unique.bothify(text='??-####'),
        id_medecin=medecins[i].id_medecin,
        id_coach=coaches[i].id_coach
    )
    session.add(membre)
    membres.append(membre)
session.commit()

print("Inserted 4 coaches, 4 medecins, 4 abonnements, and 4 membres successfully!")

