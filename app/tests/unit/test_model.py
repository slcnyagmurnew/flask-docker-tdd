from app.models import Item


def test_new_item():
    item = Item.Item("Rose", "Red")  # given model
    assert item.name == "Rose"  # when tested
    assert item.color == "Red"  # then expected response
