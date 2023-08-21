# IMPORTACA DAS BIBLIOTECAS
from azure.storage.blob import BlobClient

# VARIAVEIS DE APOIO
arquivo = '/usr/local/datasets/DADOS_EXAMES.csv'
cadeia_conexao = ''

# METODO PARA FAZER UPLOAD DE ARQUIVOS
arquivo_exames = 'raw/DADOS_EXAMES/dados_exames.csv'
blob = BlobClient.from_connection_string(conn_str=cadeia_conexao, container_name="datalake-aulas", blob_name=arquivo_exames)
with open(arquivo, "rb") as data:
  blob.upload_blob(data, overwrite = True)