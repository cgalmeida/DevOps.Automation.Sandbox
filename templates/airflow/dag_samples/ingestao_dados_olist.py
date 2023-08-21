# * CABEÇALHO
# * Nome do aluno:
# * Matrícula: 
# * Professor: 
# * Disciplina: 
# * Atividade: Ingestão de dados na plataforma Azure Storage Blob

import requests
import zipfile
from azure.storage.blob import BlobClient
import os

# DEFINIÇÃO DE VARIÁVEIS DE APOIO

url_dados_olist = ''
cadeia_conexao = ''

# MÉTODO PARA REALIZAR DOWNLOAD DE DADOS

requisicao = requests.get(url_dados_olist)
conteudo = requisicao.content
arquivo_olist = open('archive.zip', 'wb')
arquivo_olist.write(conteudo)
arquivo_olist.close()

# MÉTODO PARA DESCOMPACTAR ARQUIVOS

arquivo_olist_zip = zipfile.ZipFile('archive.zip')
arquivo_olist_zip.extractall("olist")

# MÉTODO PARA CARREGAR ARQUIVOS NO AZURE STORAGE BLOB

for arquivo in os.listdir("olist"):
  arquivo_blob = 'raw/olist/' + arquivo.replace('.csv', '/') + arquivo
  blob = BlobClient.from_connection_string(conn_str=cadeia_conexao, container_name="datalake-aulas", blob_name=arquivo_blob)
  with open("olist/" + arquivo, "rb") as data:
    blob.upload_blob(data, overwrite = True)
    os.remove("olist/" + arquivo)

os.rmdir("olist")