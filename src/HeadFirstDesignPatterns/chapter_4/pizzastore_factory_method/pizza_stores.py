import abc
from typing import Optional

from HeadFirstDesignPatterns.chapter_4.pizzastore_factory_method.pizzas import (
    Pizza,
    NYStyleCheesePizza,
    NYStyleVeggiePizza,
    NYStyleClamPizza,
    NYStylePepperoniPizza,
    ChicagoStyleCheesePizza,
    ChicagoStyleVeggiePizza,
    ChicagoStyleClamPizza,
    ChicagoStylePepperoniPizza
)


class PizzaStore(metaclass=abc.ABCMeta):
    """Abstract class for pizza store"""

    @abc.abstractmethod
    def create_pizza(self, item: str) -> Optional[Pizza]:
        pass

    def order_pizza(self, pizza_type: str) -> Optional[Pizza]:
        pizza: Pizza = self.create_pizza(pizza_type)
        print(f'--- Making a {pizza.name} ---')
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


class NYPizzaStore(PizzaStore):
    """New York pizza store"""

    def create_pizza(self, item: str) -> Optional[Pizza]:
        if item == 'cheese':
            return NYStyleCheesePizza()
        elif item == 'veggie':
            return NYStyleVeggiePizza()
        elif item == 'clam':
            return NYStyleClamPizza()
        elif item == 'pepperoni':
            return NYStylePepperoniPizza()
        else:
            return None


class ChicagoPizzaStore(PizzaStore):
    """Chicago pizza store"""

    def create_pizza(self, item: str) -> Optional[Pizza]:
        if item == 'cheese':
            return ChicagoStyleCheesePizza()
        elif item == 'veggie':
            return ChicagoStyleVeggiePizza()
        elif item == 'clam':
            return ChicagoStyleClamPizza()
        elif item == 'pepperoni':
            return ChicagoStylePepperoniPizza()
        else:
            return None
