from config.database import Base 
from sqlalchemy import Column, Integer, Float, String
class Movie(Base):
  __tablename__ = "movie"
  id = Column(Integer,  primary_key=True)
  title = Column(String)
  overview = Column(String)
  year = Column(Integer)
  rating = Column(Float)
  category = Column(String)
