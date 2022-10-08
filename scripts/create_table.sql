-- Active: 1665240056944@@127.0.0.1@5432@secrets@public
CREATE TABLE secrets (
    id uuid PRIMARY KEY,
    secret VARCHAR NOT NULL,
    hash_secret_phrase VARCHAR NOT NULL,
    is_activa BOOLEAN DEFAULT TRUE
);