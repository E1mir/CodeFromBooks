import abc
from typing import List


class QuackObservable(metaclass=abc.ABCMeta):
    """
    Observable for duck
    """

    @abc.abstractmethod
    def register_observer(self, observer) -> None:
        pass

    @abc.abstractmethod
    def notify_observers(self) -> None:
        pass


class Observer(metaclass=abc.ABCMeta):
    """
    Observer
    """

    @abc.abstractmethod
    def update(self, duck: QuackObservable):
        pass


class Observable(QuackObservable):
    """
    Observable
    """

    def __init__(self, duck: QuackObservable):
        self._observers: List[Observer] = []
        self.duck = duck

    def register_observer(self, observer: Observer) -> None:
        self._observers.append(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self.duck)


class Quackologist(Observer):
    """
    Quackologist observer
    """

    def update(self, duck: QuackObservable):
        print(f'Quacklogist: {duck} just quacked.')
