from kafka import KafkaConsumer
import json

# Configuracoes do Kafka
server = 'IP:PORTA'  # Substitua pelo endereço IP e porta corretos do Apache Kafka
topic = 'nome-do-topico' # Substituia pelo nome do topico

# Conexao com o Kafka
consumer = KafkaConsumer(
    topic,
    bootstrap_servers=server,
    value_deserializer=lambda x: x.decode('utf-8'),
    auto_offset_reset='earliest',
    max_poll_records=100  # Define o numero maximo de registros a serem buscados em cada poll
)

# Consumindo os dados do topico
while True:
    batch = consumer.poll(timeout_ms=1000)  # Tempo limite para aguardar novas mensagens (em milissegundos)
    
    if len(batch) == 0:  # Nenhuma nova mensagem encontrada
        break

    for _, messages in batch.items():
        for message in messages:
            data = message.value
            try:
                json_data = json.loads(data)
                print(json_data)  # Faça o processamento dos dados conforme necessario
            except (json.JSONDecodeError, TypeError):
                print("O dado trafegado não está em formato JSON ou mal-formatado. Exibindo como texto:")
                print(data)

# Encerrar o consumidor
consumer.close()