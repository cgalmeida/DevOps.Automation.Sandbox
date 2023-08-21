variable tags {
    default = {
        Aluno = "Preencha com o seu nome completo"
        Disciplina = "Preencha com o nome da sua disciplina"
        Matrícula = "Preencha com o seu código de matrícula" #Mesmo código existente no endereço de e-mail@sga.pucminas.br
        Email = "codigopessoa@sga.pucminas.br"
        Professor = "Victor Sales Silva"
    }
}
variable localizacao {
    description = "Localização geográfica dos recursos Azure"
    default = "eastus" # Altere para o valor retornado na consulta sobre regiões disponíveis
}
variable gruporecursos_aula {
    description = "Grupo de recursos utilizados durante as aulas"
    default = "resourcegroup_aulas"
}
variable contaarmazenamento {
    description = "Conta de armazenamento dos dados usados durante as aulas"
    default = "storageaccountXXXXXX" # Substituir o XXXXXX pelo código de pessoa
}
variable containerdatalake {
    description = "Contêiner: Armanazenamento de blobs"
    default = "datalake-aulas"
}
variable "rede" {
    description = "Nome da rede virtual que será criada para as atividades"
    default = "vnetXXXXXX" # Substituir o XXXXXX pelo código de matrícula
}
variable "gruposeguranca" {
    description = "Grupo de segurança da plataforma Azure"
    default = "vnetsecuritygroupXXXXXX" # Substituir o XXXXXX pelo código de matrícula
}
variable "ip_pessoal" {
    description = "Endereço IP do usuário que vai se conectar à rede Azure"
    default = "XXX.XXX.XXX.XXX" # Utilize o site https://whatismyip.com.br/ para descobrir seu endereço IP
}

variable "virtualmachine_linux_kafka" {
    description = "Nome da máquina virtual LINUX"
    default = "vmlinuxKafkaXXXXXX" # Substituir o XXXXXX pelo código de matrícula
}

variable "virtualmachine_linux_dremio" {
    description = "Nome da máquina virtual LINUX"
    default = "vmlinuxDremioXXXXXX" # Substituir o XXXXXX pelo código de matrícula
}

variable "virtualmachine_linux_airflow" {
    description = "Nome da máquina virtual LINUX"
    default = "vmlinuxAirFlowXXXXXX" # Substituir o XXXXXX pelo código de matrícula
}

variable "nomeusuariovm" {
    description = "Nome do usuário administrador que vai se conectar a maquina virtual"
    default = "azureuser" # Substituir por um nome de seu conhecimento
}

variable "senhausuariovm" {
    description = "Senha do usuário administrador que vai se conectar a maquina virtual"
    default = "Xa1234@54?2" # Digite uma senha forte (mínimo de 12 dígitos), letras maiúsculas e minúsculas, caracteres especiais e números"
}
