FROM efreidevopschina.azurecr.io/cache/library/python:3.10-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .
COPY test_app.py .

ENV APP_NAME=Python程序
ENV GREETING=欢迎

CMD ["python", "app.py"]