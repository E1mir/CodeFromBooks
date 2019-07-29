import abc

from HeadFirstDesignPatterns.chapter_4.pizzastore_abstract_factory.ingredient_factories import NYPizzaIngredientFactory
from HeadFirstDesignPatterns.chapter_4.pizzastore_abstract_factory.pizzas import Pizza, CheesePizza, VeggiePizza, \
    ClamPizza, PepperoniPizza


class PizzaStore(metaclass=abc.ABCMeta):
    """Pizza store abstract class"""

    @abc.abstractmethod
    def create_pizza(self, item: str) -> Pizza:
        pass

    def order_pizza(self, pizza_type: str) -> Pizza:
        pizza = self.create_pizza(pizza_type)
        print(f'--- Making a {pizza.name} ---')
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


class NYPizzaStore(PizzaStore):
    """New York pizza store"""

    def create_pizza(self, item: str) -> Pizza:
        pizza = None
        ingredient_factory = NYPizzaIngredientFactory()

        if item == 'cheese':
            pizza = CheesePizza(ingredient_factory)
            pizza.name = 'New York Style Cheese Pizza'
        elif item == 'veggie':
            pizza = VeggiePizza(ingredient_factory)
            pizza.name = 'New York Style Veggie Pizza'
        elif item == 'clam':
            pizza = ClamPizza(ingredient_factory)
            pizza.name = 'New York Style Clam Pizza'
        elif item == 'pepperoni':
            pizza = PepperoniPizza(ingredient_factory)
            pizza.name = 'New York Style Pepperoni Pizza'

        return pizza


class ChicagoPizzaStore(PizzaStore):
    """Chicago pizza store"""

    def create_pizza(self, item: str) -> Pizza:
        pizza = None
        ingredient_factory = NYPizzaIngredientFactory()

        if item == 'cheese':
            pizza = CheesePizza(ingredient_factory)
            pizza.name = 'Chicago Style Cheese Pizza'
        elif item == 'veggie':
            pizza = VeggiePizza(ingredient_factory)
            pizza.name = 'Chicago Style Veggie Pizza'
        elif item == 'clam':
            pizza = ClamPizza(ingredient_factory)
            pizza.name = 'Chicago Style Clam Pizza'
        elif item == 'pepperoni':
            pizza = PepperoniPizza(ingredient_factory)
            pizza.name = 'Chicago Style Pepperoni Pizza'

        return pizza
