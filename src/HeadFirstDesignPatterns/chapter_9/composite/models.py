import abc
from typing import Iterator, List, Optional

from HeadFirstDesignPatterns.chapter_9.composite.custom_exception import UnsupportedOperationException
from HeadFirstDesignPatterns.chapter_9.composite.iterators import NoneIterator, CompositeIterator


class MenuComponent(metaclass=abc.ABCMeta):
    """
    Menu Component abstract class
    """

    def add(self, menu_component) -> None:
        raise UnsupportedOperationException()

    def remove(self, menu_component) -> None:
        raise UnsupportedOperationException()

    def get_child(self, index: int):
        raise UnsupportedOperationException()

    @property
    def name(self) -> str:
        raise UnsupportedOperationException()

    @property
    def description(self) -> str:
        raise UnsupportedOperationException()

    @property
    def price(self) -> float:
        raise UnsupportedOperationException()

    @property
    def is_vegetarian(self) -> bool:
        raise UnsupportedOperationException()

    def print(self) -> None:
        raise UnsupportedOperationException()

    @abc.abstractmethod
    def create_iterator(self) -> Iterator:
        pass


class Menu(MenuComponent):
    """
    Menu
    """

    def __init__(self, name: str, description: str):
        self._menu_components: List[MenuComponent] = []
        self._name = name
        self._description = description
        self._iterator: Optional[Iterator[MenuComponent]] = None

    def add(self, menu_component: MenuComponent) -> None:
        self._menu_components.append(menu_component)

    def remove(self, menu_component: MenuComponent) -> None:
        self._menu_components.remove(menu_component)

    def get_child(self, index: int):
        return self._menu_components[index]

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    def print(self) -> None:
        print(f'\n{self.name}', end='')
        print(f', {self.description}')
        print('-' * 21)
        iterator: Iterator[MenuComponent] = iter(self._menu_components)
        for component in iterator:
            component.print()

    def create_iterator(self) -> Iterator[MenuComponent]:
        if self._iterator is None:
            self._iterator = CompositeIterator(iter(self._menu_components))
        return self._iterator

    def __str__(self) -> str:
        return f'{self.name} -- {self.description}'

    def __repr__(self):
        return f'Menu(\'{self.name}\')'


class MenuItem(MenuComponent):
    """
    Menu item
    """

    def __init__(self, name: str, description: str, vegetarian: bool, price: float):
        self._name = name
        self._description = description
        self._vegetarian = vegetarian
        self._price = price

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @property
    def price(self) -> float:
        return self._price

    @property
    def is_vegetarian(self) -> bool:
        return self._vegetarian

    def print(self) -> None:
        print(f'\t{self.name} ', end='')
        if self.is_vegetarian:
            print('(v)', end='')
        print(f', {self.price}')
        print(f'\t -- {self.description}')

    def create_iterator(self) -> Iterator[MenuComponent]:
        return NoneIterator()

    def __str__(self) -> str:
        vegetarian = ', (v)' if self.is_vegetarian else ''
        return f'{self._name}{vegetarian}; price - {self._price}$ '

    def __repr__(self):
        return f'MenuItem(\'{self.name}\')'
