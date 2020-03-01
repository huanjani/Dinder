import json
from src.models.RawDataModel import RawDataModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask.cli import FlaskGroup

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

with open('./recipes.json') as json_file:

  for recipe in json_file:
    newRecipe = json.loads(recipe)
    row = RawDataModel(newRecipe)
    session.add(row)
  session.commit()
