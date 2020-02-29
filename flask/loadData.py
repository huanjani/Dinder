import json
from src.models.RawDataModel import RawDataModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask.cli import FlaskGroup

engine = create_engine('postgresql://dinderpostgres:password@database-1.cvbo289m1v6g.us-west-2.rds.amazonaws.com:5432/postgres')
Session = sessionmaker(bind=engine)
session = Session()

with open('./recipes.json') as json_file:

  for recipe in json_file:
    newRecipe = json.loads(recipe)
    row = RawDataModel(newRecipe)
    session.add(row)
  session.commit()
