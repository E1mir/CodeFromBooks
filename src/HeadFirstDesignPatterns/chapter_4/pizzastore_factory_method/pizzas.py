import abc


class Pizza(metaclass=abc.ABCMeta):

    def __init__(self):
        self.name = None
        self.dough = None
        self.sauce = None
        self.toppings = []

    def prepare(self):
        print(f'Prepare {self.name}')
        print('Tossing dough...')
        print('Adding sauce...')
        print('Adding toppings: ')
        for topping in self.toppings:
            print(f'\t{topping}')

    def bake(self):
        print('Bake for 25 minutes at 350')

    def cut(self):
        print('Cut the pizza into diagonal slices')

    def box(self):
        print('Place pizza in official PizzaStore box')

    def __str__(self):
        display = f'---- {self.name} ----\n'
        display += f'{self.dough}\n'
        display += f'{self.sauce}\n'
        for topping in self.toppings:
            display += f'{topping}\n'
        return display


# CHICAGO PIZZAS

class ChicagoStyleClamPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = 'Chicago Style Clam Pizza'
        self.dough = 'Extra Thick Crust Dough'
        self.sauce = 'Plum Tomato Sauce'
        self.toppings.append('Shredded Mozzarella Cheese')
        self.toppings.append('Frozen Clams from Chesapeake Bay')

    def cut(self):
        print('Cutting the pizza into square slices')


class ChicagoStylePepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = 'Chicago Style Pepperoni Pizza'
        self.dough = 'Extra Thick Crust Dough'
        self.sauce = 'Plum Tomato Sauce'
        self.toppings.append('Shredded Mozzarella Cheese')
        self.toppings.append('Black Olives')
        self.toppings.append('Spinach')
        self.toppings.append('Eggplant')
        self.toppings.append('Sliced Pepperoni')

    def cut(self):
        print('Cutting the pizza into square slices')


class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = 'Chicago Style Deep Dish Cheese Pizza'
        self.dough = 'Extra Thick Crust Dough'
        self.sauce = 'Plum Tomato Sauce'
        self.toppings.append('Shredded Mozzarella Cheese')

    def cut(self):
        print('Cutting the pizza into square slices')


class ChicagoStyleVeggiePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = 'Chicago Deep Dish Veggie Pizza'
        self.dough = 'Extra Thick Crust Dough'
        self.sauce = 'Plum Tomato Sauce'

        self.toppings.append('Shredded Mozzarella Cheese')
        self.toppings.append('Black Olives')
        self.toppings.append('Spinach')
        self.toppings.append('Eggplant')

    def cut(self):
        print('Cutting the pizza into square slices')


# NEW YORK PIZZAS

class NYStyleClamPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = 'NY Style Clam Pizza'
        self.dough = 'Thin Crust Dough'
        self.sauce = 'Marinara Sauce'

        self.toppings.append('Grated Reggiano Cheese')
        self.toppings.append('Fresh Clams from Long Island Sound')


class NYStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = 'NY Style Sauce and Cheese Pizza'
        self.dough = 'Thin Crust Dough'
        self.sauce = 'Marinara Sauce'

        self.toppings.append('Grated Reggiano Cheese')


class NYStylePepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = 'NY Style Pepperoni Pizza'
        self.dough = 'Thin Crust Dough'
        self.sauce = 'Marinara Sauce'

        self.toppings.append('Grated Reggiano Cheese')
        self.toppings.append('Sliced Pepperoni')
        self.toppings.append('Garlic')
        self.toppings.append('Onion')
        self.toppings.append('Mushrooms')
        self.toppings.append('Red Pepper')


class NYStyleVeggiePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = 'NY Style Veggie Pizza'
        self.dough = 'Thin Crust Dough'
        self.sauce = 'Marinara Sauce'

        self.toppings.append('Grated Reggiano Cheese')
        self.toppings.append('Garlic')
        self.toppings.append('Onion')
        self.toppings.append('Mushrooms')
        self.toppings.append('Red Pepper')
