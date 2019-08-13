import abc


class Duck(metaclass=abc.ABCMeta):
    """
    Duck interface
    """

    @abc.abstractmethod
    def quack(self) -> None:
        pass

    @abc.abstractmethod
    def fly(self) -> None:
        pass


class MallardDuck(Duck):
    """
    Mallard duck
    """

    def quack(self) -> None:
        print('Quack')

    def fly(self) -> None:
        print('I\'m flying')


class Turkey(metaclass=abc.ABCMeta):
    """
    Turkey interface
    """

    @abc.abstractmethod
    def gobble(self) -> None:
        pass

    @abc.abstractmethod
    def fly(self) -> None:
        pass


class WildTurkey(Turkey):
    """
    Wild turkey
    """

    def gobble(self) -> None:
        print('Gobble gobble')

    def fly(self) -> None:
        print('I\'m flying a short distance')
