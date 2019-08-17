import abc


class CaffeineBeverage(metaclass=abc.ABCMeta):
    """
    Abstract class for creating beverage
    """

    def prepare_recipe(self) -> None:
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    @abc.abstractmethod
    def brew(self) -> None:
        pass

    @abc.abstractmethod
    def add_condiments(self) -> None:
        pass

    def boil_water(self) -> None:
        print('Boiling water')

    def pour_in_cup(self) -> None:
        print('Pouring in cup')


class Coffee(CaffeineBeverage):
    def brew(self) -> None:
        print('Dripping Coffee through filter')

    def add_condiments(self) -> None:
        print('Adding Sugar and Milk')


class Tea(CaffeineBeverage):
    def brew(self) -> None:
        print('Steeping the tea')

    def add_condiments(self) -> None:
        print('Adding Lemon')
