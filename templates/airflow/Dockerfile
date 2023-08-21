FROM apache/airflow:2.5.3

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        freetds-dev \
        libkrb5-dev \
        libsasl2-dev \
        libssl-dev \
        libffi-dev \
        libpq-dev \
        build-essential \
        python3.9 \
        python3-pip \
	&& apt-get install -y openjdk-11-jdk \
	&& apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Configurar a variável de ambiente JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64

# Definindo a versão do Python a ser usada
ENV PYTHON_VERSION=3.9

USER airflow
WORKDIR /home/airflow

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN python -m pip install --upgrade pip