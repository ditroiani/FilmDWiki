"""
File: test_bronze.py

Description: Testes unitários para a camada Bronze, focando na extração de dados da API TMDB e upload para S3.

Author: Diego Troiani

Year: 2025
"""

# import unittest
# from unittest.mock import patch
# from src.bronze.extract import get_raw_data

# class TestBronze(unittest.TestCase):
#     @patch('src.bronze.extract.requests.get')
#     def test_get_raw_data(self, mock_get):
#         # Mock da resposta da API
#         mock_get.return_value.status_code = 200
#         mock_get.return_value.json.return_value = {"results": [{"id": 1, "title": "Test Movie"}]}

#         data = get_raw_data()
#         self.assertIsInstance(data, list)
#         self.assertGreater(len(data), 0)

# if __name__ == "__main__":
#     unittest.main()