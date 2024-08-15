#!/bin/sh

# Ожидание доступности базы данных
until nc -z -v -w30 $DATABASE_HOST $DATABASE_PORT
do
  echo "Waiting for database connection..."
  sleep 5
done

exec "$@"