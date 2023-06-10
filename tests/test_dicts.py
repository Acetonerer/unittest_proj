import pytest
from utils.dicts import get_val


@pytest.fixture
def my_dict():
    return {"name": "Alex", "age": 22, "city": "Shush"}


def test_get_val_ex(my_dict):
    assert get_val(my_dict, "name") == "Alex"
    assert get_val(my_dict, "age") == 22
    assert get_val(my_dict, "city") == "Shush"


def test_get_val_nex(my_dict):
    assert get_val(my_dict, "play") == "git"


def test_get_val_nex_df(my_dict):
    assert get_val(my_dict, "play", default="read") == "read"




