import abc

from HeadFirstDesignPatterns.chapter_12.compound_patterns.decorators import QuackCounter
from HeadFirstDesignPatterns.chapter_12.compound_patterns.interfaces import Quackable
from HeadFirstDesignPatterns.chapter_12.compound_patterns.models import MallardDuck, DuckCall, RedheadDuck, RubberDuck


class AbstractDuckFactory(metaclass=abc.ABCMeta):
    """
    Abstract factory for Duck
    """

    @abc.abstractmethod
    def create_mallard_duck(self) -> Quackable:
        pass

    @abc.abstractmethod
    def create_redhead_duck(self) -> Quackable:
        pass

    @abc.abstractmethod
    def create_duck_call(self) -> Quackable:
        pass

    @abc.abstractmethod
    def create_rubber_duck(self) -> Quackable:
        pass


class DuckFactory(AbstractDuckFactory):
    """
    Simple duck factory
    """

    def create_mallard_duck(self) -> Quackable:
        return MallardDuck()

    def create_redhead_duck(self) -> Quackable:
        return RedheadDuck()

    def create_duck_call(self) -> Quackable:
        return DuckCall()

    def create_rubber_duck(self) -> Quackable:
        return RubberDuck()


class CountingDuckFactory(AbstractDuckFactory):
    """
    Counting duck factory
    """

    def create_mallard_duck(self) -> Quackable:
        return QuackCounter(MallardDuck())

    def create_redhead_duck(self) -> Quackable:
        return QuackCounter(RedheadDuck())

    def create_duck_call(self) -> Quackable:
        return QuackCounter(DuckCall())

    def create_rubber_duck(self) -> Quackable:
        return QuackCounter(RubberDuck())
