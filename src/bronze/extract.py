"""
File: extract.py

Description: Responsável pela extração de dados brutos (50 páginas) da API TMDB. Coleta informações de filmes das páginas mais bem avaliadas
e faz upload dos dados crus em .json para a camada Bronze no S3, sem transformações.

Author: Diego Troiani

Year: 2025
"""

import asyncio
import aiohttp
from src.common.config import TMDB_API_URL, HEADERS, MAX_PAGES, BRONZE_PATH, FILE_PREFIX
from src.common.utils import upload_to_s3, check_file_exists_in_s3
from datetime import datetime
import json

async def fetch_page(session, page, base_url):
    """
    Função auxiliar assíncrona para buscar uma página específica da API TMDB.
    
    Args:
        session: Sessão aiohttp para reutilizar conexões.
        page: Número da página a ser buscada.
        base_url: URL base da API.
    
    Returns:
        Dados JSON da página ou None se erro.
    """
    url = f"{base_url}{page}"
    
    try:
        # Realiza a requisição assíncrona e retorna o JSON de cada página
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                print(f"Erro na página {page}: Status HTTP {response.status}")
                return None
    except asyncio.TimeoutError:
        print(f"Timeout ao buscar página {page}")
        return None
    except aiohttp.ClientError as e:
        print(f"Erro de cliente ao buscar página {page}: {str(e)}")
        return None
    except Exception as e:
        # Trata exceções como problemas de conexão, timeout, etc.
        print(f"Erro ao buscar página {page}: {str(e)}")
        return None

async def get_raw_data():
    """
    Extrai dados brutos da API TMDB de forma assíncrona e salva na camada Bronze.
    
    Utiliza asyncio e aiohttp para fazer múltiplas requisições simultaneamente.
    """
    base_url = f"{TMDB_API_URL}/movie/top_rated?page="
    all_data = []
    
    # Cria uma sessão aiohttp com headers reutilizáveis
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        # Cria tarefas assíncronas para todas as páginas
        tasks = [fetch_page(session, page, base_url) for page in range(1, MAX_PAGES + 1)]
        
        # Executa todas as tarefas simultaneamente e aguarda os resultados
        try:
            results = await asyncio.gather(*tasks)
        except Exception as e:
            print(f"Erro durante a execução das tarefas assíncronas (tasks): {str(e)}")
            all_data = None
            return all_data
        
        # Filtra resultados válidos (remove Nones se houver erros)
        all_data = [data for data in results if data is not None]
        
        # Se alguma página falhou, considera a extração como falha (similar ao código anterior)
        if len(all_data) != MAX_PAGES:
            print(f"Atenção: Apenas {len(all_data)} de {MAX_PAGES} páginas foram extraídas com sucesso.")
            all_data = None
    
    # Verifica se a extração foi bem-sucedida antes de fazer upload
    if all_data is not None:
        # Cria nome de arquivo mensal (ex.: movie_rateds_202512.json)
        current_month = datetime.now().strftime('%Y%m')
        file_name = f"{FILE_PREFIX}_{current_month}.json"
        s3_key = f"{BRONZE_PATH}{file_name}"

        # Verifica se o arquivo mensal já existe no S3
        if check_file_exists_in_s3(s3_key):
            month_name = datetime.now().strftime('%B de %Y')  # Ex.: "December 2025"
            print(f"Dados do mês {month_name} já existem no S3. Pulando upload.")
            return all_data  # Retorna os dados sem upload

        local_path = f"temp_{file_name}"

        # Salva localmente e faz upload para S3
        try:
            with open(local_path, 'w') as f:
                json.dump(all_data, f)
            upload_to_s3(local_path, s3_key)
        except Exception as e:
            print(f"Erro ao salvar ou fazer upload: {str(e)}")
            all_data = None 
    return all_data