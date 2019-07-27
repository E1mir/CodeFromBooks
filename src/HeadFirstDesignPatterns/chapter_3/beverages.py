import abc


class Beverage(metaclass=abc.ABCMeta):

    def __init__(self):
        self._description = "Unknown Beverage"

    @property
    def description(self):
        return self._description

    @abc.abstractmethod
    def cost(self) -> float:
        pass

    def display(self):
        print(f"{self.description} ${self.cost()}")


class Espresso(Beverage):
    def __init__(self):
        super().__init__()
        self._description = "Espresso"

    def cost(self) -> float:
        return 1.99


class HouseBlend(Beverage):

    def __init__(self):
        super().__init__()
        self._description = "House Blend Coffee"

    def cost(self) -> float:
        return .89


class DarkRoast(Beverage):
    def __init__(self):
        super().__init__()
        self._description = "Dark Roast Coffee"

    def cost(self) -> float:
        return .99


class Decaf(Beverage):
    def __init__(self):
        super().__init__()
        self._description = 'Decaf Coffee'

    def cost(self) -> float:
        return 1.05
