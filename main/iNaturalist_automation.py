# Autor: Erick Bryan Cubas
# Date: 2023-10-09
# Version: 0.1
# Description: Script para automatizar o carregamento de dados da iNaturalist



# Bibliotecas utilizadas
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Import the Service class
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import shutil
import time
import os
import pyperclip
import datetime
import pandas as pd


# Declarando as variáveis principais
user_path = os.environ['USERPROFILE']
file_path_inat = os.path.join(user_path, 'species_dataset', 'inaturalist')
species_list = os.path.join(file_path_inat, 'species_list.csv')

# Apagando os arquivos anteriores existentes
if os.path.exists(species_list):
    os.remove(species_list)

# Configurar as opções do navegador Chrome
options = Options()
options.add_argument("--disable-notifications")  # Desabilitar notificações, se necessário

# Inicializar o navegador Chrome com as opções configuradas e o ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)  # Updated line

# Maximizar a janela do navegador
driver.maximize_window()

# Acessar o site
driver.get('https://www.inaturalist.org/projects/nasa-bioscape?tab=species')

time.sleep(5)

driver.close()

