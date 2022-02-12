FROM python:3.8.5

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./bcserver /bcserver
WORKDIR /bcserver

EXPOSE 8000
ENTRYPOINT python3 manage.py runserver 0.0.0.0:8000
