class MenuItem(object):
    def __init__(self, name: str, description: str, vegetarian: bool, price: float):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    @property
    def is_vegetarian(self) -> bool:
        return self.vegetarian

    def __str__(self) -> str:
        vegetarian = 'vegetarian' if self.is_vegetarian else 'not vegetarian'
        return f'{self.name}, {vegetarian} food; price - {self.price}$ '
