FROM python:3
ENV FLASK_ENV development
ENV DATABASE_URL postgresql://dinderpostgres:password@database-1.cvbo289m1v6g.us-west-2.rds.amazonaws.com:5432/postgres
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
COPY . /app
WORKDIR /app
RUN pip install numpy
RUN pip install pandas
RUN pip install -r requirements.txt
RUN python -m textblob.download_corpora

EXPOSE 5000 
# uncomment below to populate database in first deployment
# RUN python manage.py create_db
# RUN python loadData.py
# RUN python cleanText.py
# RUN python src/connectPandas.py

CMD [ "python", "run.py" ]