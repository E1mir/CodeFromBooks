import abc


class CaffeineBeverageWithHook(metaclass=abc.ABCMeta):
    """
    Abstract class for creating beverage with hook
    """

    def prepare_recipe(self) -> None:
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
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

    def customer_wants_condiments(self) -> bool:
        return True


class TeaWithHook(CaffeineBeverageWithHook):
    def brew(self) -> None:
        print('Steeping the tea')

    def add_condiments(self) -> None:
        print('Adding Lemon')

    def customer_wants_condiments(self) -> bool:
        answer = input('Would you like lemon with your tea (y/n)? ')
        return answer.strip().lower().startswith('y')


class CoffeeWithHook(CaffeineBeverageWithHook):
    def brew(self) -> None:
        print('Dripping Coffee through filter')

    def add_condiments(self) -> None:
        print('Adding Sugar and Milk')

    def customer_wants_condiments(self) -> bool:
        answer = input('Would you like milk and sugar with your coffee (y/n)? ')
        return answer.strip().lower().startswith('y')
