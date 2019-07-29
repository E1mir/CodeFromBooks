import abc


class Sauce(metaclass=abc.ABCMeta):
    """Interface for sauces"""

    @abc.abstractmethod
    def __str__(self):
        pass


class MarinaraSauce(Sauce):
    """Marinara sauce"""

    def __str__(self):
        return 'Marinara sauce'


class PlumTomatoSauce(Sauce):
    """Plum tomato sauce"""

    def __str__(self):
        return 'Tomato sauce with plum tomatoes'

