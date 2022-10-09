from aiohttp import ClientSession

async def test_generate_secret_without_body_parameter(client: ClientSession) -> None:
    resp = await client.post("/api/v1/generate", json={
        "secret": "test",
    })
    assert resp.status == 400
    
async def test_generate_secret_without_body(client: ClientSession) -> None:
    resp = await client.post("/api/v1/generate")
    assert resp.status == 400

async def test_get_secret_double(client: ClientSession) -> None:
    test_secret_key = "test"
    
    await client.post("/api/v1/generate", json={
        "secret": "test",
        "secret_key": test_secret_key
    })
    
    await client.get(f"/api/v1/secrets/{test_secret_key}")
    resp = await client.get(f"/api/v1/secrets/{test_secret_key}")
    
    assert resp.status == 400
    

async def test_get_secret_invalid_key(client: ClientSession) -> None:
    resp = await client.get(f"/api/v1/secrets/test")
    
    assert resp.status == 400