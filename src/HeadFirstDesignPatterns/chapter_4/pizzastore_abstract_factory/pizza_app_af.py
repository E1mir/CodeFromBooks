from HeadFirstDesignPatterns.chapter_4.pizzastore_abstract_factory.pizza_stores import PizzaStore, NYPizzaStore, \
    ChicagoPizzaStore
from HeadFirstDesignPatterns.chapter_4.pizzastore_abstract_factory.pizzas import Pizza

if __name__ == '__main__':
    ny_store: PizzaStore = NYPizzaStore()
    ch_store: PizzaStore = ChicagoPizzaStore()

    pizza: Pizza = ny_store.order_pizza('cheese')
    print(f'Ethan ordered a {pizza}\n')

    pizza: Pizza = ch_store.order_pizza('cheese')
    print(f'Joel ordered a {pizza}\n')

    pizza: Pizza = ny_store.order_pizza('clam')
    print(f'Ethan ordered a {pizza}\n')

    pizza: Pizza = ch_store.order_pizza('clam')
    print(f'Joel ordered a {pizza}\n')

    pizza: Pizza = ny_store.order_pizza('pepperoni')
    print(f'Ethan ordered a {pizza}\n')

    pizza: Pizza = ch_store.order_pizza('pepperoni')
    print(f'Joel ordered a {pizza}\n')

    pizza: Pizza = ny_store.order_pizza('veggie')
    print(f'Ethan ordered a {pizza}\n')

    pizza: Pizza = ch_store.order_pizza('veggie')
    print(f'Joel ordered a {pizza}\n')
