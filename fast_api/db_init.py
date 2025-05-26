from db import database, metadata
from sqlalchemy import create_engine

engine = create_engine("sqlite:///./messages.db")
metadata.create_all(engine)
