FROM python:3.6.8

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip install .

ENTRYPOINT ["storyscript"]