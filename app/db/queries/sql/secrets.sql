-- name: create_secret!
INSERT INTO secrets (id, secret, secret_key) VALUES (
    :id,
    :secret,
    :secret_key
)

-- name: get_secret^
SELECT secret FROM secrets WHERE
    secret_key = :secret_key AND
    is_active = true
    

-- name: set_secret_status<!
UPDATE secrets SET is_active = :is_active 
    WHERE secret_key = :secret_key
