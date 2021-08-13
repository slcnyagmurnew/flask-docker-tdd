import pytest

from app.models import Item


@pytest.fixture(scope="module")
def new_item():
    item = Item.Item("Daisy", "White")
    return item
