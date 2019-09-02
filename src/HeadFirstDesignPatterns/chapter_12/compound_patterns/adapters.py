from HeadFirstDesignPatterns.chapter_12.compound_patterns.interfaces import Quackable
from HeadFirstDesignPatterns.chapter_12.compound_patterns.models import Goose
from HeadFirstDesignPatterns.chapter_12.compound_patterns.observables import Observable


class GooseAdapter(Quackable):
    """
    Goose adapter
    """

    def __init__(self, goose: Goose):
        self._goose = goose
        self._observable = Observable(self)

    def quack(self) -> None:
        self._goose.honk()
        self.notify_observers()

    def register_observer(self, observer) -> None:
        self._observable.register_observer(observer)

    def notify_observers(self) -> None:
        self._observable.notify_observers()

    def __str__(self) -> str:
        return 'Goose pretending to be a Duck'
