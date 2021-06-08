### roxparteste

Este repositório contem o trabalho efetuado como teste para contratação da Rox. 
O detalhamento encontra-se no documento [.\roxpartner\Engenheiro de Dados - CSV\TesteEngenheiroDados.docx], e contem as
seguintes tarefas a serem executadas :

1.	Fazer a modelagem conceitual dos dados;
2.	Criação da infraestrutura necessária;
3.	Criação de todos os artefatos necessários para carregar os arquivos para o banco criado;
4.	Desenvolvimento de SCRIPT para análise de dados;
5.	(opcional) Criar um relatório em qualquer ferramenta de visualização de dados.

### 🎲 Justificativa

Para a realização do projeto, utilizamos a Cloud da Microsoft (Azure), pela facilidade de acesso e manipulação da base de dados utilizando o SQL Server - além de já possuir uma conta ativa !!!.
Para a carga dos dados, realizamos um script Python (3.8.10) versão em [08/06/2021] [.\Rox-test\Scripts], que efetua uma carga full das tabelas, devendo ser executado durante a madrugada logo após a consolidação das tabelas transacionais. O script utiliza os seguintes pacotes (PIP) instalados [.\Rox-test\Scripts\Requeriments.txt] :

- numpy==1.20.3
- pandas==1.2.4
- pyodbc==4.0.30
- python-dateutil==2.8.1
- pytz==2021.1
- six==1.16.0

### 🎲 Configuração da Cloud Azure

Documentação para a configuração do serviço de banco de dados em Cloud sem servidor encontra-se na pasta [.\Rox-test\Azure]

### 🎲 Modelo Entidade e Relacionamento - MER

Documentação da modelagem do banco de dados encontra-se no documento [.\Rox-test\Azure\Modelo Entidade Relacionamento.pdf]

### 🎲 Script de criação das tabelas

O script para geração das tabelas utilizadas neste teste localiza-se em  [.\Rox-test\Scripts\criação tabelas.sql]