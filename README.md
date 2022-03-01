# Projeto Integrador 3 módulo "Python para Web"(PY.2021-2.M3.PWEB) UTFPR(Universidade Tecnológica Federal do Paraná).

## Etapas ##

[Aula 1](https://github.com/claudimf/PY.2021-2.M3.PWEB/blob/main/documentos/webconf1.pdf)  

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

#### Criar aplicação

```sh
sudo docker-compose run --rm web python manage.py startapp seriados
```

#### Criar superuser

```sh
sudo docker-compose run --rm web python manage.py createsuperuser
```

#### Rodar o banco de dados

```sh
sudo docker-compose run -d postgres
```

### Permissões de arquivos ###
Quando se cria arquivos dentro de um contâiner Docker eles irão pertencer ao contâiner, para mudar a permissão rode o seguinte comando:

```sh
sudo chown -R $USER:$USER .
```

## Referências ##
[1° Django + Docker](https://github.com/claudimf/django-docker)  
[2° Dockerizing Django with Postgres, Gunicorn, and Nginx](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)  
