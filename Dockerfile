FROM python:3
ENV PYTHONUNBUFFERED 1
# RUN mkdir /crypto_games
WORKDIR /server
ADD requirements.txt /server
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install django-extensions
# ADD . /crypto_games/
