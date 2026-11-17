import pytest

from bun import Bun
from tests.conftest import read_json


@pytest.mark.parametrize(
    "test_data",
    read_json("bun_test_data.json"),
    indirect=True
)
def test_get_name(test_data):
    obj = Bun(test_data['name'], test_data['price'])
    assert obj.get_name() == test_data['name']


@pytest.mark.parametrize(
    "test_data",
    read_json("bun_test_data.json"),
    indirect=True
)
def test_get_price(test_data):
    obj = Bun(test_data['name'], test_data['price'])
    assert obj.get_price() == test_data['price']
