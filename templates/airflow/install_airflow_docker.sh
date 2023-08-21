sudo rm -rf airflow;
sudo mkdir airflow;
sudo chmod 777 airflow;
cd airflow;
sudo curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.5.3/docker-compose.yaml';
sudo chmod 777 docker-compose.yaml;
sudo mkdir -p ./dags ./logs ./plugins ./scripts ./datasets;
sudo echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env;
sudo chmod 777 dags;
sudo chmod 777 logs;
sudo chmod 777 plugins;
sudo chmod 777 scripts;
sudo chmod 777 datasets;