import pytest
import time
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


@pytest.fixture(autouse=True)
def sleep():
    time.sleep(1)
    yield
