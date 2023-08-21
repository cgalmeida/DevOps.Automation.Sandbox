from kafka import KafkaConsumer, TopicPartition
import json
import os

# Configuracoes do Kafka
server = 'IP:PORTA'  # Substitua pelo endereço IP e porta corretos do Apache Kafka
topic = 'nome-topico' # Substituia pelo nome do topico
offset_file = '/usr/local/datasets/kafka_control_topic_offset.txt'

# Função para obter o último offset lido a partir de um arquivo
def get_last_offset():
    try:
        with open(offset_file, 'r') as file:
            last_offset = int(file.read())
    except FileNotFoundError:
        last_offset = -1

    return last_offset

# Função para atualizar o último offset lido em um arquivo
def update_last_offset(offset):
    with open(offset_file, 'w') as file:
        file.write(str(offset))

# Criação do consumidor
consumer = KafkaConsumer(
    bootstrap_servers=server,
    value_deserializer=lambda x: x.decode('utf-8'),
    auto_offset_reset='earliest'
)

# Parametro de data para encerrar o loop se novas mensagens não forem visualizadas
last_message_time = time.time()

# Consumindo os dados do topico
while True:
    # Atribui o consumidor ao tópico
    consumer.subscribe([topic])
    # Obtém as partições do tópico
    partitions = consumer.partitions_for_topic(topic)
    # Consumindo os dados do tópico
    for partition in partitions:
        # Obtém o último offset lido para a partição
        last_offset = get_last_offset()
        # Define o offset inicial para ler desde o começo
        consumer.seek_to_beginning()
        # Realiza o consumo das mensagens
        for message in consumer:
            if time.time() - last_message_time > 3:  # Verifica se o tempo desde a última mensagem é maior que 3 segundos
                break;
            offset = message.offset
            data = message.value
            # Verifica se a mensagem já foi vista anteriormente
            if offset <= last_offset:
                continue
                                    
            try:
                json_data = json.loads(data)
                # Processa a mensagem JSON conforme necessário
                print(json_data)
                # Atualiza o tempo da última mensagem
                last_message_time = time.time()
            except (json.JSONDecodeError, TypeError):
                print("O dado trafegado não está em formato JSON ou está mal-formatado. Exibindo como texto:")
                print(data)
            # Atualiza o tempo da última mensagem
            last_message_time = time.time()

            # Atualiza o último offset lido
            update_last_offset(offset)
            
    if time.time() - last_message_time > 5:  # Verifica se o tempo desde a última mensagem é maior que 5 segundos
        print("Não há novas mensagens disponíveis.")
        break

# Encerra o consumidor
consumer.close()