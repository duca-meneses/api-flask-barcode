# APi flask - Barcode

API criada em **Python** usando o micro-framework  **Flask** . A principal funcionalidade da API é gerar códigos de barras para tags específicas em resposta a requisições HTTP feitas com o método  **POST** .

## Como usar

*Primeiro faça o clone do repositorio*

Para  usar utilizando o [Poetry](https://python-poetry.org/)(Gerenciador de pacotes):

* Nesse [link](https://python-poetry.org/docs/#installing-with-pipx) voce pode conferir a como instalar o poetry, depois de concluir a instalação faça o comando abaixo para verificar a versão do poetry

```shell
poetry --version
```

Para instalar os pacotes utilizados

```shell
poetry install
```

e para iniciar a aplicação

```python
python -m src.run
```

ou usando o taskipy uma lib do python

```python
task run
```

---

Para usar utilizando o pip(Gerenciado de pacotes padrão do python) primeiro crie seu ambiente virtual

```python
python -m venv .venv
```

* para ativar a sua venv usando windows:

```python
.venv/Scripts/Activate
```

* para ativar a sua venv usando linux/mac

```python
source .venv/bin/activate
```

para instalar as dependencia da aplicação

```python
pip install -r requirements.txt
```

e para rodar a aplicação

```python
python -m src.run
```

## Stack utilizada

* Python = 3.12
* Poetry
* Flask
* Python-barcode
* Pillow
* Cerberus
* Dependencias de desenvolvimento :
  * pytest
  * blue
  * isort
  * ruff
  * httpx
  * taskipy
