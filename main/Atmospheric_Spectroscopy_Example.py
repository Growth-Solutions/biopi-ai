from netCDF4 import Dataset
import os

user = os.environ['USERPROFILE']

# Define o caminho do arquivo
file_path = os.path.join(user, 'Documentos', 'emit', 'EMIT_L2A_RFL_001_20230119T114235_2301907_004.nc')

# Abre o arquivo nc para leitura
nc_file = Dataset(file_path, 'r')  # 'r' significa que o arquivo será aberto no modo de leitura

# Mostra informações sobre o arquivo
print("Informações sobre o arquivo:", nc_file)

# Lista todos os nomes de variáveis
print("Nomes das variáveis:", nc_file.variables.keys())

# Lista todas as dimensões do arquivo
print("Dimensões do arquivo:", nc_file.dimensions.keys())

# Lista os atributos globais do arquivo
print("Atributos globais do arquivo:", nc_file.ncattrs())


# Fecha o arquivo
nc_file.close()
