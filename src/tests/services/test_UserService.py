import pytest

from src.services.UsersServices import UsersService

@pytest.fixture(scope='session')
def users():
    return UsersService.get_user()

def test_get_user_not_none(users):
    assert users != None
