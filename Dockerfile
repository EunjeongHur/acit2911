FROM continuumio/anaconda3:2021.11

ADD . /code
WORKDIR /code

ENTRYPOINT ["gunicorn", "app.py"]
