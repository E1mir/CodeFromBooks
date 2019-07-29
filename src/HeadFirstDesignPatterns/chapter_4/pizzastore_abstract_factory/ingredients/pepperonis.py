import abc


class Pepperoni(metaclass=abc.ABCMeta):
    """Interface for pepperonis"""

    @abc.abstractmethod
    def __str__(self):
        pass


class SlicedPepperoni(Pepperoni):
    """Sliced pepperoni"""

    def __str__(self):
        return 'Sliced pepperoni'
