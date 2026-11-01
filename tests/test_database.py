import pytest

from database import Database
from tests.conftest import read_json

db_data = read_json("database_test_data.json")


@pytest.mark.parametrize(
    "index, expected",
    enumerate(db_data["expected_buns"]),
    ids=lambda param: f"bun_index_{param}" if isinstance(param, int) else param["name"]
)
def test_available_buns(index, expected):
    db = Database()

    buns_list = db.available_buns()

    assert len(buns_list) == len(db_data["expected_buns"])

    actual_bun = buns_list[index]
    assert actual_bun.get_name() == expected["name"]
    assert actual_bun.get_price() == expected["price"]


@pytest.mark.parametrize(
    "index, expected",
    enumerate(db_data["expected_ingredients"]),
    ids=lambda param: f"ing_index_{param}" if isinstance(param, int) else f"{param['type']}-{param['name']}"
)
def test_available_ingredients(index, expected):
    db = Database()

    ingredients_list = db.available_ingredients()

    assert len(ingredients_list) == len(db_data["expected_ingredients"])

    actual_ingredient = ingredients_list[index]
    assert actual_ingredient.get_type() == expected["type"]
    assert actual_ingredient.get_name() == expected["name"]
    assert actual_ingredient.get_price() == expected["price"]

