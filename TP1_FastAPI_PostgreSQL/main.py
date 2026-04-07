from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = "postgresql://user:password@localhost/dbname"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

class ItemSchema(BaseModel):
    name: str
    description: str


Base.metadata.create_all(bind=engine)

app = FastAPI(title="TP1 - FastAPI with PostgreSQL")

@app.get("/")
def root():
    return {"message": "TP1: FastAPI with PostgreSQL is running!"}

@app.post("/items/")
def create_item(item: ItemSchema):
    db_item = Item(name=item.name, description=item.description)
    db = SessionLocal()
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    db.close()
    return {"id": db_item.id, "name": db_item.name}

@app.get("/items/")
def get_items():
    db = SessionLocal()
    items = db.query(Item).all()
    db.close()
    return items