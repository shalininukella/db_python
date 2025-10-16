from sqlalchemy import MetaData, Column, Integer, Table, String, create_engine, text

engine = create_engine("sqlite:///:memory:")
metadata = MetaData()

users = Table(
    "users",
    metadata, 
    Column("id", Integer, primary_key=True), 
    Column("name", String),
    Column("email", String)
)

metadata.create_all(engine)