"""
File: models.py

Description: Definições dos modelos/tabelas para a camada Silver no PostgreSQL, utilizando SQLAlchemy para representar
dados limpos de filmes.

Author: Diego Troiani

Year: 2025
"""

# from sqlalchemy import Column, Integer, String, Float, DateTime
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

# class RawMovie(Base):
#     __tablename__ = "raw_movies"

#     id = Column(Integer, primary_key=True, index=True)
#     movie_id = Column(Integer, unique=True)
#     title = Column(String)
#     overview = Column(String)
#     release_date = Column(DateTime)
#     vote_average = Column(Float)