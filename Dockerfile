FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .

RUN pip install -r requirements.txt && rm requirements.txt

COPY server.py .

CMD ["sh", "-c", "python server.py"]
