FROM ubuntu/nginx:1.18-20.04_beta

RUN apt-get update \
    && apt-get install --no-install-recommends pip -y \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir mlflow==2.3.2 boto3 psycopg2-binary

COPY auth.conf auth.htpasswd launch.sh ./
RUN chmod +x launch.sh

CMD ["./launch.sh"]