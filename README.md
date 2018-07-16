# Scrapy Basics

Projeto em Scrapy criado para demonstração. Contém funcionalidades básicas que
são populares no framework _Scrapy_ e configurações que facilitam o deploy
para o _Scrapinghub_.

### Pré-requisitos

Para rodar este projeto é necessário ter instalado:
- [Python](https://www.python.org/) >= 3.6
- [Scrapy](https://scrapy.org/) >= 1.5

Se você possui o [pip](https://pypi.org/project/pip/) instalado, é possível
instalar o Scrapy através do gerenciador de pacotes:

```
pip install scrapy==1.5.0
```

### Instalação

Clone o projeto e acesse o diretório recém-criado:


```
git clone git@github.com:lidimayra/scrapy-basics.git && cd scrapy-basics
```

### Execução

Para realizar o crawl de uma spider execute o comando `scrapy crawl` passando o
nome da spider como parâmetro.

ex.:
```
# Execução da spider most_popular_movies
scrapy crawl most_popular_movies
```
