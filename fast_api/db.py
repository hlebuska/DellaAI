from sqlalchemy import Table, Column, Integer, String, MetaData, DateTime
from datetime import datetime
from databases import Database

DATABASE_URL = "sqlite:///./messages.db"

database = Database(DATABASE_URL)
metadata = MetaData()

messages = Table(
    "messages",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer),
    Column("text", String),
    Column("gpt_response", String),
    Column("timestamp", DateTime, default=datetime.utcnow),
)
