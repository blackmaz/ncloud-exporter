FROM python:3.12.7-slim

RUN ln -snf /usr/share/zoneinfo/Asia/Seoul /etc/localtime && echo "Asia/Seoul" > /etc/timezone

COPY requirements.txt .
RUN pip install distlib setuptools wheel && \
    pip install -r requirements.txt

COPY ncloud /ncloud
COPY exporter /exporter
COPY config /config
COPY main.py .
COPY common.py .
COPY config.yaml .

ENV ENV=PRD
ENV ACCOUNT_NAME=huniverse
ENV PRODUCT_NAMES="Server Redis"
ENV ACCESS_KEY=
ENV SECRET_KEY=

CMD ["python", "./main.py"]
