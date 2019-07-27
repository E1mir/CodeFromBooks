import abc

from HeadFirstDesignPatterns.chapter_3.beverages import Beverage


class CondimentDecorator(Beverage, metaclass=abc.ABCMeta):
    def __init__(self):
        super().__init__()
        self._beverage = None

    @property
    def beverage(self) -> Beverage:
        return self._beverage

    @abc.abstractmethod
    def description(self) -> str:
        pass


class Mocha(CondimentDecorator):

    def __init__(self, beverage: Beverage):
        super().__init__()
        self._beverage = beverage

    @property
    def description(self) -> str:
        return f"{self.beverage.description}, Mocha"

    def cost(self) -> float:
        return .20 + self.beverage.cost()


class Milk(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        super().__init__()
        self._beverage = beverage

    @property
    def description(self) -> str:
        return f"{self.beverage.description}, Milk"

    def cost(self) -> float:
        return .10 + self.beverage.cost()


class Whip(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        super().__init__()
        self._beverage = beverage

    @property
    def description(self) -> str:
        return f"{self.beverage.description}, Whip"

    def cost(self) -> float:
        return .10 + self.beverage.cost()


class Soy(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        super().__init__()
        self._beverage = beverage

    @property
    def description(self) -> str:
        return f"{self.beverage.description}, Soy"

    def cost(self) -> float:
        return .15 + self.beverage.cost()
