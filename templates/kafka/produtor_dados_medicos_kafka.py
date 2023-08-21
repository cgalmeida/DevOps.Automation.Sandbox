from kafka import KafkaProducer
import json
from faker import Faker

server = 'IP:PORTA'  # Substitua pelo endereço IP e porta corretos do Apache Kafka
topic = 'nome-do-topico' # Substituia pelo nome do topico

def gerar_dados_fake():
    # Função para gerar dados médicos fake usando a biblioteca Faker

    fake = Faker('pt_BR')

    dados_fake = []
    for _ in range(100):
        dado_fake = {
            'PRONTUARIO': fake.random_int(min=100000, max=999999),
            'NOME': fake.name(),
            'IDADE': fake.random_int(min=1, max=100),
            'DATANASCIMENTO': fake.date_of_birth().strftime('%d/%m/%Y'),
            'PRESSAOARTERIAL': fake.random_element(elements=('120/80', '130/90', '140/90', '150/100')),
            'TEMPERATURA': fake.pyfloat(min_value=35.0, max_value=37.5, right_digits=1),
            'ALTURA': fake.pyfloat(min_value=140.0, max_value=200.0, right_digits=1),
            'PESO': fake.pyfloat(min_value=40.0, max_value=150.0, right_digits=1),
            'BATIMENTOSCARDIACOS': fake.random_int(min=60, max=100),
            'SATURACAOOXIGENIO': fake.pyfloat(min_value=95.0, max_value=100.0, right_digits=1)
        }
        dados_fake.append(dado_fake)
    
    return dados_fake

def enviar_dados_kafka(dados):
    producer = KafkaProducer(bootstrap_servers=server, value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    
    for dado in dados:
        producer.send(topic, dado)
    
    producer.flush()

dados_fake = gerar_dados_fake()
enviar_dados_kafka(dados_fake)
