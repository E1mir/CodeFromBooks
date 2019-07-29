import abc
from typing import List

from HeadFirstDesignPatterns.chapter_4.pizzastore_abstract_factory.ingredient_factories import PizzaIngredientFactory
from HeadFirstDesignPatterns.chapter_4.pizzastore_abstract_factory.ingredients.cheeses import Cheese
from HeadFirstDesignPatterns.chapter_4.pizzastore_abstract_factory.ingredients.clams import Clams
from HeadFirstDesignPatterns.chapter_4.pizzastore_abstract_factory.ingredients.doughs import Dough
from HeadFirstDesignPatterns.chapter_4.pizzastore_abstract_factory.ingredients.pepperonis import Pepperoni
from HeadFirstDesignPatterns.chapter_4.pizzastore_abstract_factory.ingredients.sauces import Sauce
from HeadFirstDesignPatterns.chapter_4.pizzastore_abstract_factory.ingredients.veggies import Veggie


class Pizza(metaclass=abc.ABCMeta):
    """Abstract class for Pizza"""

    def __init__(self):
        self._name = None
        self._dough = None
        self._sauce = None
        self._veggies = []
        self._cheese = None
        self._pepperoni = None
        self._clams = None

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def dough(self) -> Dough:
        return self._dough

    @property
    def sauce(self) -> Sauce:
        return self._sauce

    @property
    def veggies(self) -> List[Veggie]:
        return self._veggies

    @property
    def cheese(self) -> Cheese:
        return self._cheese

    @property
    def pepperoni(self) -> Pepperoni:
        return self._pepperoni

    @property
    def clams(self) -> Clams:
        return self._clams

    @abc.abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print('Bake for 25 minutes at 350')

    def cut(self):
        print('Cutting the pizza into diagonal slices')

    def box(self):
        print('Place pizza in official PizzaStore box')

    def __str__(self):
        result = f'\n---- {self.name} ----\n'
        if self.dough is not None:
            result += str(self.dough)
            result += '\n'
        if self.sauce is not None:
            result += str(self.sauce)
            result += '\n'
        if self.cheese is not None:
            result += str(self.cheese)
            result += '\n'
        if self.veggies is not None:
            veggies = self.veggies
            for i, veggie in enumerate(veggies):
                result += str(veggie)
                if i < len(veggies) - 1:
                    result += ', '
            result += '\n'
        if self.clams is not None:
            result += str(self.clams)
            result += '\n'
        if self.pepperoni is not None:
            result += str(self.pepperoni)
            result += '\n'

        return ''.join(result)


class CheesePizza(Pizza):
    """Cheese pizza"""

    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        super().__init__()
        self._ingredient_factory = ingredient_factory

    def prepare(self):
        print(f'Preparing {self.name}')
        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()
        self._cheese = self._ingredient_factory.create_cheese()


class ClamPizza(Pizza):
    """Clam pizza"""

    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        super().__init__()
        self._ingredient_factory = ingredient_factory

    def prepare(self):
        print(f'Preparing {self.name}')
        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()
        self._cheese = self._ingredient_factory.create_cheese()
        self._clams = self._ingredient_factory.create_clams()


class PepperoniPizza(Pizza):
    """Pepperoni pizza"""

    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        super().__init__()
        self._ingredient_factory = ingredient_factory

    def prepare(self):
        print(f'Preparing {self.name}')
        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()
        self._cheese = self._ingredient_factory.create_cheese()
        self._veggies = self._ingredient_factory.create_veggies()
        self._pepperoni = self._ingredient_factory.create_pepperoni()


class VeggiePizza(Pizza):
    """Veggie pizza"""

    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        super().__init__()
        self._ingredient_factory = ingredient_factory

    def prepare(self):
        print(f'Preparing {self.name}')
        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()
        self._cheese = self._ingredient_factory.create_cheese()
        self._veggies = self._ingredient_factory.create_veggies()
