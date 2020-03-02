# dinder
Ingredient Matchmaker (Capstone Project)

To set up deployment with ECS-CLI-v2:
-in terminal run
  aws configure
  ecs-preview init
  specify names, load balanced web app, Dockerfiles for each app, frontend and backend
-from aws console (alternatively can use CDK)
  choose RDS from services menu
  click 'create database'
  choose 'standard create', not 'easy create' because need to specify VPC
  choose Postgres
  choose free tier
  choose DB instance name, username, pw, db name [note difference between DB instance name and db name!]
  copy the DB URL (postgres://[user]:[password]@[hostname]:[port]/[dbname])
  specify the VPC that the frontend and backend apps are in for this RDS instance
-go to the manifests that were generated (ymls within 'ecs-project' directory)
  change ports to 5000 (Flask) and 3000 (React)
  change one of the paths so they're not both (*); in this case I changed the flask path to '/api/*'
  <!-- add DATABASE_URL env var under "variables" in Flask/back-end (api-app) manifest -->
-change React/front-end (webapp) base_url to '/api' in App.js
-go to the AWS console again
  choose ECS from the services menu
  choose the correct cluster
  choose the frontend (webapp) service
  click the blue Update button
  on the second page, change the 'Health check grace period' to 180
  click through and save by clicking the Update Service button.
  [maybe try this for the backend service as well if it keeps flapping]
-populate db:
  add below commands to the Flask Dockerfile, then comment them out after populating the db the one time. 
  # RUN python manage.py create_db
  # RUN python loadData.py
  # RUN python cleanText.py
  # RUN python src/connectPandas.py
-run ecs-preview app deploy to deploy changes in test environment


To deploy locally with Docker:
  docker-compose up -d --build
  docker-compose exec api python manage.py create_db
  docker-compose exec api python loadData.py
  docker-compose exec api python cleanText.py
  docker-compose exec api python src/connectPandas.py
  localhost:5000
  for psql: docker-compose exec postgres psql --username=user --dbname=pgdb
  DATABASE_URL=postgresql://user:password@postgres:5432/pgdb

To run locally: 
  Pipenv install: Flask, CORS, text, json, pandas, squareform, pdist, numpy, psycopg2, sqlachemy, sqlalcehmy.orm, sqlachemy.types, textblob, re
  Toggle server in run.py  
  FLASK_ENV=development DATABASE_URL=postgres://janicehuang:localhost/dinder python run.py  

Background:
  173,278 recipes  
  44,197 ingredients  
  876,434 ingredient-recipe pairs  
  Jaccard Index  
  Limited to ingredients with over 1,000 recipes, limited those to 40,000 ingredient-recipe pairs  
  18,769 similarities  
  call those over .01 (or greater depending on slider)  
