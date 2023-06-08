#!/bin/sh

envsubst < auth.conf >/etc/nginx/sites-enabled/default
envsubst < auth.htpasswd > /etc/nginx/.htpasswd
service nginx restart

mlflow server \
--backend-store-uri postgresql://$DB_USER:$DB_PW@$DB_ENDPOINT:$DB_PORT/$DB_NAME  \
--default-artifact-root s3://$AWS_BUCKET_NAME