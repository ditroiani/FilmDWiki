"""
File: utils.py

Description: Funções utilitárias compartilhadas, incluindo logging, validações de dados, helpers para upload/download no S3
e outras operações comuns ao projeto.

Author: Diego Troiani

Year: 2025
"""

import logging
import boto3
import locale
from botocore.exceptions import NoCredentialsError, ClientError
from datetime import datetime
from src.common.config import BUCKET_NAME

# Configura locale para português (pt_BR) - global para o projeto
try:
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
except locale.Error:
    try:
        locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil.1252')  # Windows
    except locale.Error:
        pass  # Fallback para inglês se não conseguir

# Configuração de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def upload_to_s3(file_path, s3_key):
    """Upload de arquivo para S3."""
    try:
        s3_client = boto3.client('s3')
        s3_client.upload_file(file_path, BUCKET_NAME, s3_key)
        logger.info(f"Arquivo {file_path} enviado para s3://{BUCKET_NAME}/{s3_key}")
    except NoCredentialsError:
        logger.error("Credenciais AWS não encontradas.")
    except Exception as e:
        logger.error(f"Erro ao enviar para S3: {str(e)}")

def check_file_exists_in_s3(s3_key):
    """Verifica se um arquivo existe no S3 e se foi uploaded no mês atual."""
    try:
        s3_client = boto3.client('s3') # S3 client
        response = s3_client.head_object(Bucket=BUCKET_NAME, Key=s3_key) # Cabeçalho do objeto
        
        # Verifica se o arquivo foi modificado no mês atual
        last_modified = response['LastModified']
        current_month = datetime.now().strftime('%Y-%m')
        file_month = last_modified.strftime('%Y-%m')
        if file_month == current_month:
            logger.info("Dados já foram gerados esse mês!")
            return True
        else:
            logger.info("Dados não existe porém, acabou de ser atualizado agora.")
            return False
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchKey':
            return False
        else:
            logger.error(f"Erro ao verificar arquivo no S3: {str(e)}")
            return False
    except Exception as e:
        logger.error(f"Erro inesperado ao verificar arquivo no S3: {str(e)}")
        return False

# def download_from_s3(s3_key, local_path):
#     """Download de arquivo do S3."""
#     try:
#         s3_client = boto3.client('s3')
#         s3_client.download_file(BUCKET_NAME, s3_key, local_path)
#         logger.info(f"Arquivo baixado de s3://{BUCKET_NAME}/{s3_key} para {local_path}")
#     except Exception as e:
#         logger.error(f"Erro ao baixar do S3: {str(e)}")

def validate_data(data):
    """Validação básica de dados (ex.: checar se não está vazio)."""
    if not data:
        raise ValueError("Dados vazios ou inválidos.")
    return True