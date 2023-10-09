import requests
import xml.etree.ElementTree as ET

# Endpoint da API
url = 'https://cmr.earthdata.nasa.gov/search/collections'

# Parâmetros da requisição
params = {
    'keyword': 'MODIS',  
    'page_size': 100,    
    'page_num': 1       
}

# Fazendo a requisição GET
response = requests.get(url, params=params)

# Checando se a requisição foi bem-sucedida
if response.status_code == 200:
    # Parseando a resposta XML
    root = ET.fromstring(response.content)
    # Iterando através dos elementos XML e imprimindo os nomes e IDs das coleções
    for reference in root.findall('.//reference'):
        name = reference.find('name').text
        collection_id = reference.find('id').text
        print(f'Nome: {name}, ID: {collection_id}')
else:
    print(f'Erro na requisição: {response.status_code}')
