"""
File: config.py

Description: Configurações globais compartilhadas pelo projeto, incluindo URLs da API TMDB, headers de autenticação,
caminhos do S3 e constantes para buckets e paths das camadas Bronze, Silver e Gold.

Author: Diego Troiani

Year: 2025
"""

import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configurações da API TMDB
TMDB_API_URL = os.getenv("TMDB_API_URL")
TMDB_TOKEN = os.getenv("TMDB_TOKEN")
HEADERS = {
    "accept": "application/json",
    "Authorization": f"Bearer {TMDB_TOKEN}"
}

# Configurações do S3
BUCKET_NAME = os.getenv("BUCKET_NAME")
BRONZE_PATH = "bronze/tmdb_api/movies/"
SILVER_PATH = "silver/tmdb_api/movies/"
GOLD_PATH = "gold/tmdb_api/movies/"

# Outras constantes
MAX_PAGES = 50  # Número máximo de páginas a extrair da API
FILE_PREFIX = os.getenv("FILE_PREFIX")  # Prefixo para nome do arquivo de dados