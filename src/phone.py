

class Phone:
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса phone.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        """Возвращает полное имя сотрудника. К атрибуту можно обращаться без ()."""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        try:
            if not isinstance(number_of_sim, int) or number_of_sim <= 0:
                raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
            self.__number_of_sim = number_of_sim
        except ValueError as error:
            print('\033[91m' + f'ValueError: { error }' + '\033[0m')

    def __str__(self):
        return self.__name
    def __repr__(self):
        return f"Phone('{ self.__name }', { self.price }, { self.quantity }, { self.number_of_sim })"
    def __add__(self, other):
        return self.quantity + other.quantity
