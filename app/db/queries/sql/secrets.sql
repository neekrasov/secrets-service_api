-- name: create_secret!
INSERT INTO secrets (id, secret, hash_secret_phrase) VALUES (
    :id,
    :new_secret,
    :new_hash_secret_phrase
)