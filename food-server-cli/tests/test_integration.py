import unittest
from unittest.mock import patch, MagicMock
from api import fetch_product_category

class TestAPIIntegration(unittest.TestCase):

    @patch('urllib.request.urlopen')
    def test_fetch_product_category_success(self, mock_urlopen):
        """Valida se a aplicação processa corretamente o JSON retornado pela API externa"""
        # Simulando um JSON válido retornado pela Open Food Facts
        fake_json = '{"products": [{"categories_tags": ["en:dairy-products"]}]}'
        
        mock_response = MagicMock()
        mock_response.read.return_value = fake_json.encode('utf-8')
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        # Executa a função
        resultado = fetch_product_category("Leite")
        
        # Valida se tratou a string como esperado no código (en:dairy-products -> Dairy-products)
        self.assertEqual(resultado, "Dairy-products")

    @patch('urllib.request.urlopen')
    def test_fetch_product_category_failure(self, mock_urlopen):
        """Garante resiliência do sistema se a API externa cair"""
        mock_urlopen.side_effect = Exception("Erro de conexão com o servidor da API")
        
        resultado = fetch_product_category("Chocolate")
        
        # Deve retornar o Fallback padrão definido em vez de quebrar o programa
        self.assertEqual(resultado, "Outros")

if __name__ == '__main__':
    unittest.main()