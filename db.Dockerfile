FROM postgres:14

COPY scripts/init_db.sql /docker-entrypoint-initdb.d/