FROM python:3.8-slim
WORKDIR /app
RUN apt-get update && apt-get install -y
COPY requirements.txt /app
RUN pip3 install --upgrade pip
RUN pip3 install  -r requirements.txt