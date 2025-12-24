"""
File: load.py

Description: Responsável pelo carregamento e agregação final na camada Gold. Consulta dados da Silver no PostgreSQL,
realiza agregações (ex.: estatísticas por gênero) e salva os resultados no PostgreSQL ou S3.

Author: Diego Troiani

Year: 2025
"""

# from sqlalchemy import func
# from src.common.database import SessionLocal
# from src.silver.models import RawMovie
# from src.gold.models import MovieStats
# from src.common.utils import upload_to_s3
# import json

# def aggregate_movie_stats():
#     """Agrega estatísticas de filmes (ex.: média de votos)."""
#     db = SessionLocal()
#     try:
#         # Exemplo: média de vote_average
#         avg_vote = db.query(func.avg(RawMovie.vote_average)).scalar()
#         stats = {"average_vote": avg_vote}
#         return stats
#     finally:
#         db.close()

# def save_gold_data(stats):
#     """Salva dados agregados no PostgreSQL."""
#     db = SessionLocal()
#     try:
#         gold_entry = MovieStats(average_vote=stats['average_vote'])
#         db.add(gold_entry)
#         db.commit()
#         # Opcional: salvar também no S3
#         file_name = "aggregated_stats.json"
#         with open(file_name, 'w') as f:
#             json.dump(stats, f)
#         upload_to_s3(file_name, "gold/tmdb_api/movies/aggregated_stats.json")
#     except Exception as e:
#         db.rollback()
#         print(f"Erro ao salvar Gold: {str(e)}")
#     finally:
#         db.close()