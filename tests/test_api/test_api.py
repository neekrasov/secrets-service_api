from aiohttp import ClientSession

async def test_generate_secret(client: ClientSession) -> None:
    resp = await client.post("/api/v1/generate", json={
        "secret": "test",
        "secret_key": "test"
    })
    assert resp.status == 200

async def test_get_secret(client: ClientSession) -> None:
    test_secret_key = "test"
    
    await client.post("/api/v1/generate", json={
        "secret": "test",
        "secret_key": test_secret_key
    })
    
    resp = await client.get(f"/api/v1/secrets/{test_secret_key}")
    
    
    assert resp.status == 200