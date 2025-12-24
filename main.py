"""
File: main.py

Description: Orquestrador principal do projeto FilmDWiki. Coordena o fluxo ETL através das camadas Bronze, Silver e Gold,
integrando extração de dados da API TMDB, limpeza, transformação e carregamento no PostgreSQL e S3.

Author: Diego Troiani

Year: 2025
"""

import asyncio
from src.bronze.extract import get_raw_data
# from src.silver.transform import clean_movie_data, save_cleaned_data
# from src.gold.load import aggregate_movie_stats, save_gold_data
from dotenv import load_dotenv

# Load environment variables
load_dotenv()  

# Aplicação do ETL completo
if __name__ == "__main__":
    # Fluxo ETL: Bronze -> Silver -> Gold
    
    # Bronze
    print("Iniciando ETL...")
    try:
        raw_data = asyncio.run(get_raw_data())  # Bronze
        print("Dados brutos extraídos.")
    except Exception as e:
        print(f"Erro durante a extração de dados: {str(e)}")
        exit(1)  # Sai com código de erro
    
    # cleaned_df = clean_movie_data()  # Silver
    # save_cleaned_data(cleaned_df)
    # print("Dados limpos salvos no PostgreSQL.")
    
    # stats = aggregate_movie_stats()  # Gold
    # save_gold_data(stats)
    # print("Dados agregados salvos.")
    
    # print("ETL concluído!")