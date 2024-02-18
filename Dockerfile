FROM python:3.10-alpine3.18

WORKDIR /app

COPY . .

RUN pip3 install -e .

CMD ["python3", "rpsls/main_cli.py"]
