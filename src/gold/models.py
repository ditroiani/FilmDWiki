"""
File: models.py

Description: Definições dos modelos/tabelas para a camada Gold no PostgreSQL, utilizando SQLAlchemy para representar
dados agregados e estatísticas de filmes.

Author: Diego Troiani

Year: 2025
"""

# from sqlalchemy import Column, Integer, Float
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

# class MovieStats(Base):
#     __tablename__ = "movie_stats"

#     id = Column(Integer, primary_key=True, index=True)
#     average_vote = Column(Float)