FROM python:3.8.18-alpine3.17

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN  apk update \
	&& apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
	&& pip install --upgrade pip

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./
COPY wait-for-postgres.sh /wait-for-postgres.sh
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN apk add --no-cache dos2unix \
    && dos2unix /wait-for-postgres.sh /docker-entrypoint.sh
RUN chmod +x /wait-for-postgres.sh /docker-entrypoint.sh

CMD ["sh", "/wait-for-postgres.sh", "sh", "/docker-entrypoint.sh"]