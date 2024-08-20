from mrs_api.services.engine import get_postgres_uri

def test_get_postgres_uri():
    assert get_postgres_uri(
        host="abcd",
        port=5432,
        user="admin",
        password="admin",
        db="P@#"
    ) == "postgresql+asyncpg://admin:admin@abcd:5432/P%40%23"