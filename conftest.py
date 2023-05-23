import pytest


@pytest.fixture(scope='module')
def request_get_fixture():
    print('\nCreation of AuthCode: {AuthCode}')
    data = None
    yield data
    print('\ndel of data')