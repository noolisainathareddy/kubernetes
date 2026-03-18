FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt

COPY . .

CMD ["uvicron","app.main:app", "--host","127.0.0.1", "--port", "80" ]