# API de Escola

O Sistema de Gestão de Doações para Organizações de Caridade é uma aplicação web projetada para ajudar organizações de caridade a gerenciar doações de forma eficiente e organizada. Este sistema permite que as organizações importem listas de doações a partir de arquivos CSV, exportem relatórios detalhados e visualizem estatísticas sobre as doações recebidas.

## Tecnologias

### **Django Rest Framework**
- **Descrição**: Um poderoso framework para construção de APIs web com Django. 
- **Site Oficial**: [Django Rest Framework](https://www.django-rest-framework.org/)

### **Celery**
- **Descrição**: Uma biblioteca para o gerenciamento de tarefas assíncronas e distribuídas. É utilizada para processar tarefas de forma assíncrona, como importação e exportação de dados.
- **Site Oficial**: [Celery](https://docs.celeryproject.org/)

### **RabbitMQ / Redis**
- **Descrição**: Brokers de mensagens utilizados pelo Celery para gerenciar a fila de tarefas. RabbitMQ é um broker de mensagens robusto, enquanto Redis é uma estrutura de dados em memória que também pode atuar como um broker de mensagens.
- **RabbitMQ**:
  - **Site Oficial**: [RabbitMQ](https://www.rabbitmq.com/)
- **Redis**:
  - **Site Oficial**: [Redis](https://redis.io/)

### **Banco de Dados**
- **PostgreSQL**:
  - **Descrição**: Um sistema de gerenciamento de banco de dados relacional poderoso e de código aberto. Ideal para sistemas que exigem alta performance e integridade dos dados.
  - **Site Oficial**: [PostgreSQL](https://www.postgresql.org/)


### **Ferramentas de Exportação**
- **Openpyxl**:
  - **Descrição**: Uma biblioteca para ler e escrever arquivos Excel (XLSX) em Python.
  - **Site Oficial**: [Openpyxl](https://openpyxl.readthedocs.io/)
- **ReportLab**:
  - **Descrição**: Uma biblioteca para gerar documentos PDF em Python.
  - **Site Oficial**: [ReportLab](https://www.reportlab.com/)

## Pré-requisitos

Antes de começar, certifique-se de ter as seguintes ferramentas instaladas:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Make](https://www.gnu.org/software/make/)

## Configuração Inicial

Para configurar o ambiente e iniciar a aplicação, siga os passos abaixo:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/JoseGuiFerreira17/api_school.git
   cd donation_hub_back

2. **Crie os arquivos de configuração necessários:**
   ```bash
   make prebuild

3. **Crie a rede Docker necessária:**

   ```bash
   make create_network

4. **Construa e inicie os containers Docker:**

   ```bash
   make build

5. **Aplique as migrações do banco de dados:**

   ```bash
   make migrate

## Comandos Makefile

Aqui estão os comandos definidos no `Makefile` e suas funções:

- **`prebuild`**: Cria os arquivos de configuração `.env` e `.db.env` a partir dos arquivos de exemplo fornecidos.

  ```bash
  cp example.env .env
  cp example.db.env .db.env

- **`create_network`**: Cria uma rede Docker personalizada para a aplicação.

  ```bash
   docker network create --gateway 10.7.0.1 --subnet 10.7.0.0/16 donation_network

- **`build`**: Constrói e inicia os containers Docker definidos no `docker-compose.yml`.
  ```bash
   docker compose up --build

- **`migrate`**: Aplica as migrações do banco de dados usando o Django.
  ```bash
   docker compose exec donation_django python manage.py migrate

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

#### Termos Principais:

- **Permissões:** Você pode usar, copiar, modificar, mesclar, publicar, distribuir, sublicenciar e vender cópias do Software.
- **Isenção de Garantia:** O software é fornecido "como está", sem garantias de qualquer tipo. O autor não será responsável por qualquer dano que possa resultar do uso do software.

Para mais detalhes, consulte o arquivo [LICENSE](LICENSE) no repositório.