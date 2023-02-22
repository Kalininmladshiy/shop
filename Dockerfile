FROM python:latest
EXPOSE 8000
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app

