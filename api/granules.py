import requests

# Endpoint da API
url = 'https://cmr.earthdata.nasa.gov/search/granules'

# Parâmetros da requisição
params = {
    'collection_concept_id': 'C1234567890-EXAMPLE',  # Substitua pelo ID real da coleção
    'page_size': 10,
    'page_num': 1
}

# Fazendo a requisição GET
response = requests.get(url, params=params)
print(response.text)  # Imprimindo a resposta
