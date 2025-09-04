#!/bin/sh

echo "Esperando a PostgreSQL..."

timeout=30
count=0

while ! nc -z postgres 5432; do
  sleep 1
  count=$((count + 1))
  if [ $count -ge $timeout ]; then
    echo "Timeout esperando a PostgreSQL"
    exit 1
  fi
done

echo "PostgreSQL está listo. Ejecutando Django..."
exec "$@"
