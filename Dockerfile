FROM python:3.9.12
#FROM python:3.7.7-slim

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD ["python3", "app.py"]