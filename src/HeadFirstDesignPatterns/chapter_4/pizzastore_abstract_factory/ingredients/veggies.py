import abc


class Veggie(metaclass=abc.ABCMeta):
    """Interface for veggies"""

    @abc.abstractmethod
    def __str__(self):
        pass


class BlackOlives(Veggie):
    """Black olives"""

    def __str__(self):
        return 'Black olives'


class Eggplant(Veggie):
    """Eggplant"""

    def __str__(self):
        return 'Eggplant'


class Garlic(Veggie):
    """Garlic"""

    def __str__(self):
        return 'Garlic'


class Mushroom(Veggie):
    """Mushroom"""

    def __str__(self):
        return 'Mushrooms'


class Onion(Veggie):
    """Onion"""

    def __str__(self):
        return 'Onion'


class RedPepper(Veggie):
    """Red pepper"""

    def __str__(self):
        return 'Red pepper'


class Spinach(Veggie):
    """Spinach"""

    def __str__(self):
        return 'Spinach'
