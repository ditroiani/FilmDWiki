"""
File: database.py

Description: Utilitários para conexão e interação com o banco de dados PostgreSQL, incluindo configuração do engine SQLAlchemy
e funções auxiliares para queries e inserções nas camadas Silver e Gold.

Author: Diego Troiani

Year: 2025
"""

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# import os

# # Configuração da conexão PostgreSQL
# DB_HOST = os.getenv("DB_HOST")
# DB_PORT = os.getenv("DB_PORT", "5432")
# DB_NAME = os.getenv("DB_NAME")
# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD = os.getenv("DB_PASSWORD")

# DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# # Engine e Session
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# def get_db():
#     """Retorna uma sessão de banco de dados."""
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()