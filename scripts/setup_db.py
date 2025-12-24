"""
File: setup_db.py

Description: Script para configurar e criar tabelas no PostgreSQL para as camadas Silver e Gold. Deve ser executado
uma vez para inicializar o banco de dados.

Author: Diego Troiani

Year: 2025
"""

# from src.common.database import engine
# from src.silver.models import Base as SilverBase
# from src.gold.models import Base as GoldBase

# def setup_database():
#     """Cria todas as tabelas definidas nos modelos."""
#     SilverBase.metadata.create_all(bind=engine)
#     GoldBase.metadata.create_all(bind=engine)
#     print("Tabelas criadas com sucesso.")

# if __name__ == "__main__":
#     setup_database()