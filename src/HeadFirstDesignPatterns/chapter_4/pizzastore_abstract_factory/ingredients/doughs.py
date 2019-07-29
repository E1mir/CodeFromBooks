import abc


class Dough(metaclass=abc.ABCMeta):
    """Interface for dough"""

    @abc.abstractmethod
    def __str__(self):
        pass


class ThickCrustDough(Dough):
    """Thick crust dough"""

    def __str__(self):
        return 'Thick crust dough'


class ThinCrustDough(Dough):
    """Thin crust dough"""

    def __str__(self):
        return 'Thin crust dough'
