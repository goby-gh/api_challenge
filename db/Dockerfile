FROM postgres:15

ENV POSTGRES_DB habitat
ENV POSTGRES_PASSWORD energy

COPY ./init.db.sh /docker-entrypoint-initdb.d/

COPY ./ /tmp/
