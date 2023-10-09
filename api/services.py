import requests
import xml.etree.ElementTree as ET

# Endpoint da API
url = 'https://cmr.earthdata.nasa.gov/search/collections'

# Parâmetros da requisição
params = {
    'concept_id': 'C2231548569-CEOS_EXTRA',  # Substitua pelo ID real da coleção
    'page_size': 10,
    'page_num': 1
}

# Fazendo a requisição GET
response = requests.get(url, params=params)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    # Parseando a resposta XML
    root = ET.fromstring(response.content)
    # Encontrando e imprimindo os identificadores de serviço
    for service_id in root.findall('.//services/service_id'):
        print(service_id.text)
else:
    print(f'Erro na requisição: {response.status_code}')
