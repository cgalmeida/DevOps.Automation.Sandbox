# IMPORTACA DAS BIBLIOTECAS

from pyspark.sql import SparkSession, SQLContext
from pyspark.sql.functions import regexp_replace

# CRIACAO DA APLICACAO SPARK

spark = SparkSession.builder.appName("ATIVIDADE_4_B").getOrCreate()
sqlcontext = SQLContext(spark)

# VARIAVEIS DE APOIO

arquivo = '/usr/local/datasets/DADOS_EXAMES.csv'

# LEITURA DOS DATAFRAMES

df_dados_exames = spark.read.format("csv").options(header=True, inferSchema=True, delimiter=";").load(arquivo)
df_dados_exames.createOrReplaceTempView("dados_exames")

# NORMALIZAR OS DADOS

df_unidade_atendimento = sqlcontext.sql("""
SELECT  DISTINCT  IdUnidadeAtendimento,
                  Cidade,
                  Estado,
                  Bairro
FROM dados_exames
""")

df_unidade_atendimento.coalesce(1).write.format("csv").options(header=True, inferSchema=True).save("/usr/local/datasets/df_unidades")

df_exame = sqlcontext.sql("""
SELECT  DISTINCT  IdExame,
                  Exame,
                  SiglaExame,
                  Material,
                  SetorExame
FROM dados_exames
""")

df_exame.coalesce(1).write.format("csv").options(header=True, inferSchema=True).save("/usr/local/datasets/df_exames")

fato_exame = sqlcontext.sql("""
SELECT  DISTINCT  IdUnidadeAtendimento,
                  NumPedidoMedico,
                  IdExame,
                  QtdAmostrasColhidas,
                  QtdExames,
                  CAST(regexp_replace(PrecoExame, ',', '.') AS FLOAT) AS PrecoExame,
                  DataPrevistaResultado,
                  DataLiberacaoResultado
FROM dados_exames
""")

fato_exame.coalesce(1).write.format("csv").options(header=True, inferSchema=True).save("/usr/local/datasets/fato_exame")