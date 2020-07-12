FROM python:3.8.3-buster

ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt
COPY . /app/
RUN make setup