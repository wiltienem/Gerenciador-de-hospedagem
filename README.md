# Gerenciador de Hospedagem

## Descrição

O Gerenciador de Hospedagem é uma aplicação web desenvolvida em Python utilizando Streamlit para auxiliar no gerenciamento de hospedagens, hóspedes, reservas, pagamentos e avaliações.

O sistema foi criado com foco na organização das informações de uma plataforma de hospedagem, permitindo visualizar dados, realizar cadastros, consultas, edições e exclusões, além de apresentar indicadores e gráficos para facilitar a análise das informações.

Todos os dados utilizados pelo sistema são armazenados em arquivos CSV, simulando um banco de dados simples para fins acadêmicos.

---

## Integrante

- Wiltiene Marrara da Silva Andrade

---

## Funcionalidades

- Cadastro de hóspedes.
- Cadastro de hospedagens.
- Cadastro de reservas.
- Cadastro de pagamentos.
- Cadastro de avaliações.
- Pesquisa de hóspedes.
- Pesquisa de hospedagens.
- Edição de registros.
- Exclusão de registros.
- Dashboard com indicadores.
- Visualização de gráficos estatísticos.
- Leitura e manipulação de arquivos CSV.

---

## Conceitos de Programação Orientada a Objetos utilizados

O projeto foi desenvolvido aplicando diversos conceitos de Programação Orientada a Objetos (POO), entre eles:

- Classes e Objetos
- Encapsulamento
- Herança
- Polimorfismo
- Associação
- Agregação
- Composição
- Abstração

---

## Estrutura do Projeto

```
Sistema-Hospedagem/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── classes/
├── componentes/
├── paginas/
├── graficos/
├── utils/
├── dados/
├── docs/
└── images/
```

---

## Diagrama de Classes

O diagrama UML desenvolvido para o projeto encontra-se na pasta:

```
images/
```

Arquivo:

```
diagrama_uml.png
```

---

## Tecnologias Utilizadas

- Python 3
- Streamlit
- Pandas
- Plotly

---

## Como Executar

### 1. Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
```

### 2. Acessar a pasta do projeto

```bash
cd Sistema-Hospedagem
```

### 3. Criar um ambiente virtual

```bash
python3 -m venv .venv
```

### 4. Ativar o ambiente virtual

Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

### 5. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 6. Executar a aplicação

```bash
python3 -m streamlit run app.py
```

Após executar o comando, o sistema será aberto automaticamente no navegador.

---

## Organização dos Dados

Os dados utilizados pela aplicação são armazenados na pasta:

```
dados/
```

Arquivos disponíveis:

- hospedes.csv
- listings.csv
- reservas.csv
- pagamentos.csv
- avaliacoes.csv

---

## Funcionalidades da Interface

O sistema possui as seguintes páginas:

- Início
- Hospedagens
- Hóspedes
- Reservas
- Pagamentos
- Avaliações
- Dashboard
- Relatórios

Também conta com componentes reutilizáveis, como:

- Menu lateral
- Cards de hospedagem
- Indicadores
- Gráficos interativos

---

## Controle de Versão

Durante o desenvolvimento do projeto foi utilizado o Git para controle de versões e o GitHub para armazenamento e compartilhamento do código-fonte, mantendo um histórico de commits com mensagens descritivas.

---

## Licença

Projeto desenvolvido exclusivamente para fins acadêmicos na disciplina de Programação Orientada a Objetos.