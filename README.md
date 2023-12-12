# Trabalho Final - TF_CSD

Este é um guia passo a passo para executar o projeto TF_CSD hospedado no GitHub. Siga as instruções abaixo para configurar e executar o projeto localmente em seu ambiente.

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes requisitos instalados em seu sistema:

- Git
- Python (preferencialmente Python 3.x)
- Pip (um gerenciador de pacotes para Python)

##  Passo 1: Clonar o Repositório

Abra um terminal e execute o seguinte comando para clonar o repositório TF_CSD do GitHub:

```bash
git clone https://github.com/ppinheirosiqueira/TF_CSD
``` 
## Passo 2: Navegar até a Pasta do Projeto

Depois de clonar o repositório, navegue até a pasta `TF_CSD` usando o comando:

```bash
cd TF_CSD
```

## Passo 3: Instalar o Poetry

O próximo passo é instalar o Poetry, que é uma ferramenta para gerenciamento de dependências em Python. Você pode instalar o Poetry usando pip:

```bash
pip install poetry
```
## Passo 4: Ativar o Ambiente Virtual

Com o Poetry instalado, você pode criar um novo ambiente virtual e ativá-lo usando o comando:

```bash
poetry shell
```
## Passo 5: Instalar as Dependências

Agora você pode instalar todas as dependências necessárias para o projeto com o comando:

```bash
poetry install
```
## Passo 6: Executar o Projeto

Finalmente, execute o script com o comando:

```bash
cd TFCSD
python manage.py runserver
```
Agora você deve ser capaz de acessar o projeto em seu navegador local no endereço http://localhost:8000.



