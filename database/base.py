from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

# Create connection to database.
engine = create_engine('postgresql+psycopg2://neo:1234@mnist_problem-db-1:5432/imagesdb', echo=True)

# Define a base table class.
Base = declarative_base()

# Create a database session.
Session = sessionmaker(bind=engine)
