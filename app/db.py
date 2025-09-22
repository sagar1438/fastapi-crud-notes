# from app.api import models


# Mock Notes DB 
# notes_list:list[models.NoteDB] = []


from sqlalchemy import(
    Column, create_engine, MetaData, Table, String, Integer, Date, Boolean
)
from sqlalchemy.sql import func
from databases import Database

# creating Database url for PSQL

DB_USERNAME="postgres"
DB_PASSWORD="postgres"
DB_HOST="localhost"
DB_NAME= "Notes_FastAPI"
# url creation
DATABASE_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"


# engine creation
engine = create_engine(DATABASE_URL) # to communicate with DB
metadata = MetaData() # to create db schema

# DB table
notes = Table(
    "notes", metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(100)),
    Column("description", String(100)),
    Column("is_completed", Boolean, default=False),
    Column("created_at", Date, default=func.now(), nullable=False)
)

database = Database(DATABASE_URL) # database query builder