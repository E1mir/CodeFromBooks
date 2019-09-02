from typing import List

from HeadFirstDesignPatterns.chapter_12.compound_patterns.interfaces import Quackable


class Flock(Quackable):
    """
    Flock for ducks
    """

    def __init__(self):
        self.ducks: List[Quackable] = []

    def add(self, duck: Quackable) -> None:
        self.ducks.append(duck)

    def quack(self) -> None:
        for quacker in self.ducks:
            quacker.quack()

    def register_observer(self, observer) -> None:
        for duck in self.ducks:
            duck.register_observer(observer)

    def notify_observers(self) -> None:
        pass

    def __str__(self) -> str:
        return 'Flock of Ducks'
