import os
import pytest
from mrs_api.env.settings import get_settings, Settings


@pytest.fixture
def settings():
    return get_settings()


@pytest.fixture
def custom_settings():
    os.environ.setdefault(key="POSTGRES_HOST", value="TESTING")
    return get_settings(), Settings()


def test_settings(settings, custom_settings):
    assert settings.postgres_host == custom_settings[0].postgres_host
    assert settings.postgres_host != custom_settings[1].postgres_host
