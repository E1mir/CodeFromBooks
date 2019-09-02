from HeadFirstDesignPatterns.chapter_12.compound_patterns.interfaces import Quackable
from HeadFirstDesignPatterns.chapter_12.compound_patterns.observables import Observable


class MallardDuck(Quackable):
    """
    Mallard Duck model
    """

    def __init__(self):
        self._observable = Observable(self)

    def register_observer(self, observer) -> None:
        self._observable.register_observer(observer)

    def notify_observers(self) -> None:
        self._observable.notify_observers()

    def quack(self) -> None:
        print('Quack')
        self.notify_observers()

    def __str__(self) -> str:
        return 'Mallard Duck'


class RedheadDuck(Quackable):
    """
    Redhead Duck model
    """

    def __init__(self):
        self._observable = Observable(self)

    def register_observer(self, observer) -> None:
        self._observable.register_observer(observer)

    def notify_observers(self) -> None:
        self._observable.notify_observers()

    def quack(self) -> None:
        print('Quack')
        self.notify_observers()

    def __str__(self) -> str:
        return 'Redhead Duck'


class DuckCall(Quackable):
    """
    Duck call model
    """

    def __init__(self):
        self._observable = Observable(self)

    def register_observer(self, observer) -> None:
        self._observable.register_observer(observer)

    def notify_observers(self) -> None:
        self._observable.notify_observers()

    def quack(self) -> None:
        print('Kwak')
        self.notify_observers()

    def __str__(self) -> str:
        return 'Duck call'


class RubberDuck(Quackable):
    """
    Rubber Duck model
    """

    def __init__(self):
        self._observable = Observable(self)

    def register_observer(self, observer) -> None:
        self._observable.register_observer(observer)

    def notify_observers(self) -> None:
        self._observable.notify_observers()

    def quack(self) -> None:
        print('Squeak')
        self.notify_observers()

    def __str__(self) -> str:
        return 'Rubber Duck'


# ---------------------------------------
class Goose(object):
    """
    Goose model
    """

    def honk(self) -> None:
        print('Honk')

    def __str__(self) -> str:
        return 'Goose'
