import json
import urllib.request
import urllib.error

def fetch_product_category(barcode_or_name):
    """
    Busca a categoria de um produto na API Open Food Facts.
    Se não encontrar ou der erro, retorna 'Desconhecido'.
    """
    # Se for apenas texto livre, a API de busca por nome é mais complexa,
    # então usamos o endpoint de busca geral formatado.
    query = urllib.parse.quote(barcode_or_name)
    url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={query}&search_simple=1&action=process&json=1"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'ValidadeApp/1.0 (Python CLI)'})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
            if data.get("products") and len(data["products"]) > 0:
                # Retorna a categoria principal ou a primeira da lista
                product = data["products"][0]
                return product.get("categories_tags", ["Sem Categoria"])[0].replace("en:", "").capitalize()
    except Exception:
        pass
    
    return "Outros"