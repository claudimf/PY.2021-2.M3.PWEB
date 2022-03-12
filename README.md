# Projeto Integrador 3 módulo "Python para Web"(PY.2021-2.M3.PWEB) UTFPR(Universidade Tecnológica Federal do Paraná).

## Etapas ##

[Aula 1](https://github.com/claudimf/PY.2021-2.M3.PWEB/blob/main/documentos/webconf1.pdf)  
[Aula 2](https://github.com/claudimf/PY.2021-2.M3.PWEB/blob/main/documentos/01-Models.pdf)  
[Aula 3](https://github.com/claudimf/PY.2021-2.M3.PWEB/blob/main/documentos/02-urls-views-templates.pdf)  
[Aula 4](https://github.com/claudimf/PY.2021-2.M3.PWEB/blob/main/documentos/04-Forms-ModelForms-Views%20Gen%C3%A9ricas%20de%20Edi%C3%A7%C3%A3o.pdf)  
[Aula 5](https://github.com/claudimf/PY.2021-2.M3.PWEB/blob/main/documentos/webconf2.pdf)  
[Aula 6](https://github.com/claudimf/PY.2021-2.M3.PWEB/blob/main/documentos/06-consultas-Q_Auth.pdf)  
[Aula 7](https://github.com/claudimf/PY.2021-2.M3.PWEB/blob/main/documentos/07-Auth.pdf)  

## Como utilizar? ##

**:warning: Warning:** É necessário ter o Docker instalado:
- 🐳 [Docker Engine Installation](https://docs.docker.com/engine/install/ubuntu/)  
- 🐳 [Docker Compose Installation](https://docs.docker.com/compose/install/)  
- **💡 Tip:** [For any doubts please use Docker documentation](https://docs.docker.com/)  

### Utilizando a aplicação

Após instalar o Docker e o Docker-compose, abar um terminal e execute:

```sh
sudo docker-compose up
```
Para acessar a aplicação, abra uma nova aba no seu terminal e execute:

```sh
sudo docker-compose run --rm postgres bash
```

Para resetar a aplicação, execute:

```sh
docker-compose down && docker-compose up
```

#### Rodar migrações

```sh
sudo docker-compose run --rm web python manage.py makemigrations
sudo docker-compose run --rm web python manage.py migrate
```

#### Acessar o Shell

```sh
sudo docker-compose run --rm web python manage.py shell
```

#### Criar dados

```sh
from seriados.models import Serie, Temporada, Episodio

Serie.objects.all()
nova = Serie(nome='Doctor Who')
nova.save()
print(nova.id)
print(nova.nome)
Serie.objects.all()
```

####  Display de um choice

```sh
from seriados import models

s = models.Serie(nome="Fawlty Towers")
s.save()

t = models.Temporada(numero=1, serie=s)
t.save()

import datetime
e = models.Episodio(data=datetime.date(1975,9,19),
titulo="A Touch of Class", temporada=t
)
e.save()

from django.contrib.auth import models as auth_models
u = auth_models.User.objects.get(pk=1)

r = models.Revisor(user=u)
r.save()

re = models.ReviewEpisodio(episodio=e, revisor=r, nota = ’A’)
re.save()

re.get_nota_display() # Imprime ’Excelente’
re.nota # Imprime ’A’
```

#### Acessando o valor de display de um choice
```sh
from seriados import models
e = models.Episodio.objects.get(pk=1)
e.get_absolute_url() # Retorna ’/seriados/episodio/1/’
```

#### Criar aplicação

```sh
sudo docker-compose run --rm web python manage.py startapp seriados
```

#### Carregar dados iniciais da aplicação
```sh
sudo docker-compose run --rm web python manage.py loaddata seriados/fixtures/01_initial_values.json
```

#### Criar superuser

```sh
sudo docker-compose run --rm web python manage.py createsuperuser
```

#### Rodar o banco de dados

```sh
sudo docker-compose run -d postgres
```

#### Criar fixtures
```sh
sudo docker-compose run --rm web ./create_fixtures
```

#### Recriar e Popular banco
```sh
sudo docker-compose run --rm web ./populate_db
```

### Permissões de arquivos ###
Quando se cria arquivos dentro de um contâiner Docker eles irão pertencer ao contâiner, para mudar a permissão rode o seguinte comando:

```sh
sudo chown -R $USER:$USER .
```

## Referências ##
[1° Django + Docker](https://github.com/claudimf/django-docker)  
[2° Dockerizing Django with Postgres, Gunicorn, and Nginx](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)  
[3° How to provide initial data for models](https://docs.djangoproject.com/en/4.0/howto/initial-data/)  
[4° Django: setup básico com Bootstrap](https://dev.to/thalesbruno/django-projeto-generico-com-bootstrap-3d86)  