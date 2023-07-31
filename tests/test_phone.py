from src.phone import Phone
from src.item import Item
def test_str():
    phone = Phone('iPhone 14', 120000, 5, 2)
    assert str(phone) == 'iPhone 14'

def test_repr():
    phone = Phone('iPhone 14', 120000, 5, 2)
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"

def test_add():
    item = Item('Телевизор', 10000, 5)
    phone = Phone('iPhone 14', 120000, 5, 2)
    assert item + phone == 10