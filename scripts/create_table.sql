-- Active: 1665240056944@@127.0.0.1@5432@secrets@public
CREATE TABLE secrets (
    id uuid PRIMARY KEY NOT NULL,
    secret VARCHAR NOT NULL,
    secret_key VARCHAR NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
);

DROP TABLE secrets;