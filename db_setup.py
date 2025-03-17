from sqlalchemy import create_engine
from models import Base

DATABASE_URL = "sqlite:///euro_fit.db"  # Using SQLite

engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(engine)

print("Database created successfully!")
