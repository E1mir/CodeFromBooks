import abc


class Cheese(metaclass=abc.ABCMeta):
    """Interface for cheese"""

    @abc.abstractmethod
    def __str__(self):
        pass


class MozzarellaCheese(Cheese):
    """Mozzarella cheese"""

    def __str__(self):
        return 'Shredded Mozzarella'


class ParmesanCheese(Cheese):
    """Parmesan cheese"""

    def __str__(self):
        return 'Shredded Parmesan'


class ReggianoCheese(Cheese):
    """Reggiano cheese"""

    def __str__(self):
        return 'Reggiano Cheese'
