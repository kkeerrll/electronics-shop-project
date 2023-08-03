import csv
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        """Возвращает полное имя сотрудника. К атрибуту можно обращаться без ()."""
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name[0:10]

    @staticmethod
    def string_to_number(str1: str) -> int:
        return int(float(str1))


    @staticmethod
    def instantiate_from_csv():
        with open("/Users/anzelikagudkova/Desktop/electronics-shop-project/src/items.csv", 'r', newline='',
                  encoding='CP1251') as file:
            data = csv.DictReader(file)
            for item in list(data):
                obj = Item(item['name'], Item.string_to_number(item['price']), Item.string_to_number(item['quantity']))
                Item.all.append(obj)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __add__(self, other):
        return self.quantity + other.quantity

    # @staticmethod
    # def instantiate_from_csv():
    #     """Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv"""
    #     try:
    #         with open("/Users/anzelikagudkova/Desktop/electronics1/src/items.csv", 'r', newline='',
    #                   encoding='CP1251') as file:
    #             data = csv.DictReader(file)
    #             for item in data:
    #                 item['name'], float(item['price']), Item.string_to_number(item['quantity'])
    #
    #     except Exception:
    #         print('\033[91m' + 'InstantiateCSVError: Файл item.csv поврежден' + '\033[0m')
    #         # raise Exception('InstantiateCSVError: Файл item.csv поврежден')
    #     except FileNotFoundError:
    #         print('\033[91m' + 'FileNotFoundError: Отсутствует файл item.csv' + '\033[0m')
    #         # raise ZeroDivisionError('Cannot divide by zero')


    # @staticmethod
    # def instantiate_from_csv():
    #     """Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv"""
    #     with open("/Users/anzelikagudkova/Desktop/electronics1/src/items.csv", 'r', newline='',
    #               encoding='CP1251') as file:
    #         data = csv.DictReader(file)
    #         for item in data:
    #             item['name'], float(item['price']), Item.string_to_number(item['quantity'])
    #
    #
    #     raise Exception('InstantiateCSVError: Файл item.csv поврежден')
    #     raise FileNotFoundError('FileNotFoundError: Отсутствует файл item.csv')
    @staticmethod
    def instantiate_from_csv():
        try:
            with open("/Users/anzelikagudkova/Desktop/electronics1/src/items.csv", 'r', newline='',
                      encoding='CP1251') as file:
                data = csv.DictReader(file)
                items = []
                for item in data:
                    name = item['name']
                    price = float(item['price'])
                    quantity = Item.string_to_number(item['quantity'])
                    item_instance = Item(name, price, quantity)
                    items.append(item_instance)
                return items
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')
        except (IOError, ValueError):
            raise Exception('Файл item.csv поврежден')