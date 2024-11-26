import pytest
from praktikum.database import Database
from unittest.mock import MagicMock
from praktikum.burger import Burger
@pytest.fixture
def database():
    return Database()

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def bun():
    bun_mock = MagicMock()
    bun_mock.get_name.return_value = "Small Bun"
    bun_mock.get_price.return_value = 100.0
    return bun_mock

@pytest.fixture
def ingredient():
    ingredient_mock = MagicMock()
    ingredient_mock.get_name.return_value = "Cheese"
    ingredient_mock.get_type.return_value = "FILLING"
    ingredient_mock.get_price.return_value = 50.0
    return ingredient_mock