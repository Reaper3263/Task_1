import pytest

from ingredient import Ingredient
from tests.conftest import read_json


@pytest.mark.parametrize(
    "test_data",
    read_json("ingredients_test_data.json"),
    indirect=True
)
def test_get_type(test_data):
    obj = Ingredient(test_data["type"], test_data["name"], test_data["price"])
    assert obj.get_type() == test_data["type"]


@pytest.mark.parametrize(
    "test_data",
    read_json("ingredients_test_data.json"),
    indirect=True
)
def test_get_name(test_data):
    obj = Ingredient(test_data["type"], test_data["name"], test_data["price"])
    assert obj.get_name() == test_data["name"]


@pytest.mark.parametrize(
    "test_data",
    read_json("ingredients_test_data.json"),
    indirect=True
)
def test_get_price(test_data):
    obj = Ingredient(test_data["type"], test_data["name"], test_data["price"])
    assert obj.get_price() == test_data["price"]