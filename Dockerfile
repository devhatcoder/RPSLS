FROM python:3.10-alpine3.18

WORKDIR /app

COPY ./requirements.txt /app/

RUN pip3 install -r requirements.txt

COPY ./rpsls /app/

CMD ["python3", "main_cli.py"]
