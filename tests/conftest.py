import json
from pathlib import Path

import pytest


def read_json(file_name: str) -> list:
    data_path = Path(__file__).parent / "test_data" / file_name
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture
def test_data(request):
    return request.param
