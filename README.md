<!--
File: README.md

Description: Documentação principal do projeto FilmDWiki, incluindo arquitetura Medallion, instruções de instalação,
configuração e uso.

Author: Diego Troiani

Year: 2025
-->

# FilmDWiki

Projeto de ETL para extração, transformação e carregamento de dados de filmes da API TMDB, utilizando arquitetura Medallion
(Bronze, Silver, Gold) com armazenamento em S3 e PostgreSQL.

## Arquitetura

- **Bronze**: Dados brutos da API, salvos no S3.
- **Silver**: Dados limpos e estruturados no PostgreSQL.
- **Gold**: Dados agregados para análise.

Em construção...
