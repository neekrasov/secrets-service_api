CREATE DATABASE secrets;

CREATE TABLE secrets (
    id uuid PRIMARY KEY NOT NULL,
    secret VARCHAR NOT NULL,
    secret_key VARCHAR NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
);