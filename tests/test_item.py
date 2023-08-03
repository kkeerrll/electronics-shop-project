import pytest

from src.item import Item
from src.phone import Phone



test_item1 = Item("Утюг", 2000, 15)
test_item2 = Item("TV", 40000, 5)


def test_calculate_total_price():
    assert test_item1.calculate_total_price() == 30000
    assert test_item2.calculate_total_price() == 200000

def test_apply_discount():
    Item.pay_rate = 0.5
    test_item1.apply_discount()
    assert test_item1.price == 1000
    test_item2.apply_discount()
    assert test_item2.price == 20000

def test_name_setter():
    item = Item('Телевизор', 10000, 5)
    assert item.name == "Телевизор"

def test_string_to_number():
    assert Item.string_to_number('5') == 5

def test_instantiate_from_csv():
    Item.all = []
    Item.instantiate_from_csv()
    assert len(Item.all) == 5

def test_str():
    item = Item('Телевизор', 10000, 5)
    assert str(item) == 'Телевизор'

def test_repr():
    item = Item('Телевизор', 10000, 5)
    assert repr(item) == "Item('Телевизор', 10000, 5)"
def test_add():
    item = Item('Телевизор', 10000, 5)
    phone = Phone('iPhone 14', 120000, 5, 2)
    assert item + phone == 10

def test_instantiate_from_csv_file_not_found():
    # Предполагаем, что файл items.csv не существует
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()


def test_instantiate_from_csv_file_corrupted():
    # Предполагаем, что файл items.csv существует, но поврежден
    with pytest.raises(Exception):
        Item.instantiate_from_csv()

