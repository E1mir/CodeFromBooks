import abc
from typing import Iterator, List, Dict

from HeadFirstDesignPatterns.chapter_9.iterator.iterators import DinerMenuIterator
from HeadFirstDesignPatterns.chapter_9.iterator.models import MenuItem


class Menu(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_iterator(self) -> Iterator[MenuItem]:
        pass


class DinerMenu(Menu):
    __MAX_ITEMS = 6

    def __init__(self):
        self._menu_items = []

        self.add_item('Vegetarian BLT', '(Fakin\') Bacon with lettuce & tomato on whole wheat', True, 2.99)
        self.add_item('BLT', 'Bacon with lettuce & tomato on whole wheat', False, 2.99)
        self.add_item('Soup of the day', 'Soup of the day, with a side of potato salad', False, 3.29)
        self.add_item('Hotdog', 'A hot dog, with saurkraut, relish, onions, topped with cheese', False, 3.05)
        self.add_item('Steamed Veggies and Brown Rice', 'A medly of steamed vegetables over brown rice', True, 3.99)
        self.add_item('Pasta', 'Spaghetti with Marinara Sauce, and a slice of sourdough bread', True, 3.89)

    def add_item(self, name: str, description: str, vegetarian: bool, price: float) -> None:
        menu_item = MenuItem(name, description, vegetarian, price)
        current_length = len(self._menu_items)
        if current_length >= self.__MAX_ITEMS:
            print('Sorry, menu is full! Can\'t add item to menu')
        else:
            self._menu_items.append(menu_item)

    @property
    def menu_items(self) -> List[MenuItem]:
        return self._menu_items

    def create_iterator(self) -> Iterator[MenuItem]:
        return DinerMenuIterator(self.menu_items)


class CafeMenu(Menu):
    def __init__(self):
        self._menu_items: Dict[str, MenuItem] = {}
        self.add_item(
            'Veggie Burger and Air Fries',
            'Veggie burger on a whole wheat bun, lettuce, tomato, and fries',
            True,
            3.99
        )
        self.add_item('Soup of the day', 'A cup of the soup of the day, with a side salad', False, 3.69)
        self.add_item('Burrito', 'A large burrito, with whole pinto beans, salsa, guacamole', True, 4.29)

    def add_item(self, name: str, description: str, vegetarian: bool, price: float) -> None:
        menu_item = MenuItem(name, description, vegetarian, price)
        self._menu_items[menu_item.name] = menu_item

    @property
    def menu_items(self) -> Dict[str, MenuItem]:
        return self._menu_items

    def create_iterator(self) -> Iterator[MenuItem]:
        return iter(self.menu_items.values())


class PancakeHouseMenu(Menu):
    def __init__(self):
        self._menu_items: List[MenuItem] = []
        self.add_item('K&B\'s Pancake Breakfast', 'Pancakes with scrambled eggs, and toast', True, 2.99)
        self.add_item('Regular Pancake Breakfast', 'Pancakes with fried eggs, sausage', False, 2.99)
        self.add_item('Blueberry Pancakes', 'Pancakes made with fresh blueberries, and blueberry syrup', True, 3.49)
        self.add_item('Waffles', 'Waffles, with your choice of blueberries or strawberries', True, 3.59)

    def add_item(self, name: str, description: str, vegetarian: bool, price: float) -> None:
        menu_item = MenuItem(name, description, vegetarian, price)
        self._menu_items.append(menu_item)

    @property
    def menu_items(self) -> List[MenuItem]:
        return self._menu_items

    def create_iterator(self) -> Iterator[MenuItem]:
        return iter(self.menu_items)
