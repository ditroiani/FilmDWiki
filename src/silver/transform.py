"""
File: transform.py

Description: Responsável pela transformação e limpeza dos dados da camada Bronze. Baixa dados do S3, processa com Pandas
(removendo duplicatas, padronizando formatos) e insere os dados limpos no PostgreSQL para a camada Silver.

Author: Diego Troiani

Year: 2025
"""

# import pandas as pd
# from src.common.database import SessionLocal
# from src.common.utils import download_from_s3
# from src.common.config import BRONZE_PATH, MAX_PAGES
# from src.silver.models import RawMovie  # Importar modelo da Silver
# import json

# def clean_movie_data():
#     """Baixa e limpa dados da Bronze, retornando DataFrame limpo."""
#     all_movies = []

#     for page in range(1, MAX_PAGES + 1):
#         s3_key = f"{BRONZE_PATH}raw_page_{page}.json"
#         local_path = f"temp_raw_{page}.json"
#         download_from_s3(s3_key, local_path)

#         with open(local_path, 'r') as f:
#             data = json.load(f)
#             if 'results' in data:
#                 all_movies.extend(data['results'])

#     df = pd.DataFrame(all_movies)
#     # Limpeza: remover duplicatas, tratar nulos
#     df = df.drop_duplicates(subset=['id'])
#     df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
#     return df

# def save_cleaned_data(df):
#     """Salva dados limpos no PostgreSQL."""
#     db = SessionLocal()
#     try:
#         for _, row in df.iterrows():
#             movie = RawMovie(
#                 movie_id=row['id'],
#                 title=row['title'],
#                 overview=row['overview'],
#                 release_date=row['release_date'],
#                 vote_average=row['vote_average']
#             )
#             db.add(movie)
#         db.commit()
#     except Exception as e:
#         db.rollback()
#         print(f"Erro ao salvar: {str(e)}")
#     finally:
#         db.close()