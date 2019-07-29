import abc


class Clams(metaclass=abc.ABCMeta):
    """Interface for clams"""

    @abc.abstractmethod
    def __str__(self):
        pass


class FreshClams(Clams):
    """Fresh clams"""

    def __str__(self):
        return 'Fresh Clams from Long Island Sound'


class FrozenClams(Clams):
    """Frozen clams"""

    def __str__(self):
        return 'Frozen Clams from Chesapeake Bay'
