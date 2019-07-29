import abc
from typing import List

from HeadFirstDesignPatterns.chapter_4.pizzastore_abstract_factory.ingredients.cheeses import Cheese, ReggianoCheese, \
    MozzarellaCheese
from HeadFirstDesignPatterns.chapter_4.pizzastore_abstract_factory.ingredients.clams import Clams, FreshClams, \
    FrozenClams
from HeadFirstDesignPatterns.chapter_4.pizzastore_abstract_factory.ingredients.doughs import Dough, ThinCrustDough, \
    ThickCrustDough
from HeadFirstDesignPatterns.chapter_4.pizzastore_abstract_factory.ingredients.pepperonis import Pepperoni, \
    SlicedPepperoni
from HeadFirstDesignPatterns.chapter_4.pizzastore_abstract_factory.ingredients.sauces import Sauce, MarinaraSauce, \
    PlumTomatoSauce
from HeadFirstDesignPatterns.chapter_4.pizzastore_abstract_factory.ingredients.veggies import Veggie, Garlic, Onion, \
    Mushroom, RedPepper, BlackOlives, Spinach, Eggplant


class PizzaIngredientFactory(metaclass=abc.ABCMeta):
    """Interface for pizza ingredient factory"""

    @abc.abstractmethod
    def create_dough(self) -> Dough:
        pass

    @abc.abstractmethod
    def create_sauce(self) -> Sauce:
        pass

    @abc.abstractmethod
    def create_cheese(self) -> Cheese:
        pass

    @abc.abstractmethod
    def create_veggies(self) -> List[Veggie]:
        pass

    @abc.abstractmethod
    def create_pepperoni(self) -> Pepperoni:
        pass

    @abc.abstractmethod
    def create_clams(self) -> Clams:
        pass


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    """New York pizza ingredient factory"""

    def create_dough(self) -> Dough:
        return ThinCrustDough()

    def create_sauce(self) -> Sauce:
        return MarinaraSauce()

    def create_cheese(self) -> Cheese:
        return ReggianoCheese()

    def create_veggies(self) -> List[Veggie]:
        veggies: List[Veggie] = [Garlic(), Onion(), Mushroom(), RedPepper()]
        return veggies

    def create_pepperoni(self) -> Pepperoni:
        return SlicedPepperoni()

    def create_clams(self) -> Clams:
        return FreshClams()


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    """Chicago pizza ingredient factory"""

    def create_dough(self) -> Dough:
        return ThickCrustDough()

    def create_sauce(self) -> Sauce:
        return PlumTomatoSauce()

    def create_cheese(self) -> Cheese:
        return MozzarellaCheese()

    def create_veggies(self) -> List[Veggie]:
        veggies: List[Veggie] = [BlackOlives(), Spinach(), Eggplant()]
        return veggies

    def create_pepperoni(self) -> Pepperoni:
        return SlicedPepperoni()

    def create_clams(self) -> Clams:
        return FrozenClams()
