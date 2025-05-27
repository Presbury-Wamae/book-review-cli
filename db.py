# db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///book_reviews.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
