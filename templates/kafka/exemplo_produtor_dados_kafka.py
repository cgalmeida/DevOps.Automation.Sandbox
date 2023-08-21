from kafka import KafkaProducer
import json

server = 'IP:PORTA'  # Substitua pelo endereço IP e porta corretos do Apache Kafka
topic = 'nome-do-topico' # Substituia pelo nome do topico

# Criacao de produtor de dados
producer = KafkaProducer(bootstrap_servers=server, value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Criando um fluxo de dados
dado = {
            'Prontuario': 123456,
            'Nome': 'Maria da Silva',
            'DataNascimento': '01/01/1970',
            'PressaoArterial': '120/80',
            'Temperatura': 36.5,
            'Altura': 170.0,
            'Peso': 70.0,
            'BatimentosCardiacos': 80,
            'SaturacaoOxigenio': 98.5
        }

# Enviando dados para o topico
producer.send(topic, dado)

# Liberando o fluxo de dado para novas informacoes
producer.flush()