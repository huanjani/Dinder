FROM python:3
ENV FLASK_ENV development

# Is it terrible to have this db url here? How do I keep env variables like this out of the public eye with when including them for Docker? (It is also in the .env file.) Do I use .gitignore?

ENV DATABASE_URL postgresql://user:password@postgres:5432/pgdb
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
COPY . /app
WORKDIR /app
RUN pip install numpy
RUN pip install pandas
RUN pip install -r requirements.txt
RUN python -m textblob.download_corpora
EXPOSE 5000 

CMD [ "python", "run.py" ]