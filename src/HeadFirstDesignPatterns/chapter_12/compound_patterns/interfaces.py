import abc

from HeadFirstDesignPatterns.chapter_12.compound_patterns.observables import QuackObservable


class Quackable(QuackObservable):
    """
    Quackable interface
    """

    @abc.abstractmethod
    def quack(self) -> None:
        pass
