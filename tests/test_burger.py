import pytest

from bun import Bun
from burger import Burger
from ingredient import Ingredient
from tests.conftest import read_json


@pytest.mark.parametrize(
    "test_data",
    read_json("bun_test_data.json"),
    indirect=True,
)
def test_set_buns(test_data):
    test_bun = Bun(test_data['name'], test_data['price'])
    burger = Burger()

    burger.set_buns(test_bun)

    assert burger.bun.get_name() == test_data['name']
    assert burger.bun.get_price() == test_data['price']


@pytest.mark.parametrize(
    "test_data",
    read_json("ingredients_test_data.json"),
    indirect=True,
)
def test_add_ingredient(test_data):
    burger = Burger()
    test_ingredient = Ingredient(test_data['type'], test_data['name'], test_data['price'])

    burger.add_ingredient(test_ingredient)

    assert len(burger.ingredients) == 1
    assert burger.ingredients[0] == test_ingredient


@pytest.mark.parametrize(
    "test_data",
    read_json("ingredients_test_data.json"),
    indirect=True,
)
def test_remove_ingredient(test_data):
    burger = Burger()
    test_ingredient = Ingredient(test_data['type'], test_data['name'], test_data['price'])
    burger.ingredients = [test_ingredient]
    burger.remove_ingredient(0)

    assert burger.ingredients == []


@pytest.mark.parametrize(
    "test_data",
    read_json("ingredients_test_data.json"),
    indirect=True,
)
def test_move_ingredient(test_data):
    burger = Burger()
    ing_first = Ingredient(test_data['type'], test_data['name'], test_data['price'])
    ing_second = Ingredient("sauce", "Тестовый соус заглушка", 0.0)

    burger.ingredients = [ing_first, ing_second]

    burger.move_ingredient(0, 1)

    assert burger.ingredients == [ing_second, ing_first]


@pytest.mark.parametrize(
    "test_data",
    read_json("burger_test_data.json"),
    indirect=True,
)
def test_get_price(test_data):
    burger = Burger()

    test_bun = Bun(test_data['bun']['name'], test_data['bun']['price'])
    burger.set_buns(test_bun)

    for ing in test_data['ingredients']:
        test_ingredient = Ingredient(ing['type'], ing['name'], ing['price'])
        burger.add_ingredient(test_ingredient)

    actual_price = burger.get_price()

    assert actual_price == test_data['expected_price']


@pytest.mark.parametrize(
    "test_data",
    read_json("burger_test_data.json"),
    indirect=True,
)
def test_get_receipt(test_data):
    burger = Burger()

    test_bun = Bun(test_data['bun']['name'], test_data['bun']['price'])
    burger.set_buns(test_bun)

    for ing in test_data['ingredients']:
        test_ingredient = Ingredient(ing['type'], ing['name'], ing['price'])
        burger.add_ingredient(test_ingredient)

    actual_receipt = burger.get_receipt()

    assert actual_receipt == test_data['expected_receipt']
