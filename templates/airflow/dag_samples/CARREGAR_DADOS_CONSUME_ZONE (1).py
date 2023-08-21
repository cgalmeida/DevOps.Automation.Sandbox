# IMPORTACA DAS BIBLIOTECAS
from azure.storage.blob import BlobClient

# VARIAVEIS DE APOIO
arquivo = '/usr/local/datasets/DADOS_EXAMES.csv'
cadeia_conexao = ''

# METODO PARA FAZER UPLOAD DE ARQUIVOS
caminho_df_unidades_local = '/usr/local/datasets/df_unidades'
caminho_df_unidades_datalake = 'consume/DW_Exames/Dim_Unidade/dim_unidade.csv'
for item in caminho_df_unidades_local:
  if item.endswith(".csv"):
    blob = BlobClient.from_connection_string(conn_str=cadeia_conexao, container_name="datalake-aulas", blob_name=caminho_df_unidades_datalake)
    with open(item.key, "rb") as data:
      blob.upload_blob(data, overwrite = True)

caminho_df_exames_local = '/usr/local/datasets/df_exames'
caminho_df_exames_datalake = 'consume/DW_Exames/Dim_Exame/dim_exame.csv'
for item in caminho_df_exames_local:
  if item.endswith(".csv"):
    blob = BlobClient.from_connection_string(conn_str=cadeia_conexao, container_name="datalake-aulas", blob_name=caminho_df_exames_datalake)
    with open(item.key, "rb") as data:
      blob.upload_blob(data, overwrite = True)

caminho_fato_exames_local = '/usr/local/datasets/fato_exames'
caminho_fato_exames_datalake = 'consume/DW_Exames/Fato_Exame/fato_exame.csv'
for item in caminho_fato_exames_local:
  if item.endswith(".csv"):
    blob = BlobClient.from_connection_string(conn_str=cadeia_conexao, container_name="datalake-aulas", blob_name=caminho_fato_exames_datalake)
    with open(item.key, "rb") as data:
      blob.upload_blob(data, overwrite = True)