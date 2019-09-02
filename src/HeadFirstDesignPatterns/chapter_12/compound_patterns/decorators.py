from HeadFirstDesignPatterns.chapter_12.compound_patterns.interfaces import Quackable


class QuackCounter(Quackable):
    """
    Quack counter decorator
    """
    number_of_quacks: int = 0

    def __init__(self, duck: Quackable):
        self.duck = duck

    def quack(self) -> None:
        self.duck.quack()
        QuackCounter.number_of_quacks += 1

    def register_observer(self, observer) -> None:
        self.duck.register_observer(observer)

    def notify_observers(self) -> None:
        self.duck.notify_observers()

    def __str__(self) -> str:
        return str(self.duck)
