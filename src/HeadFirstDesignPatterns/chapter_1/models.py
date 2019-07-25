import abc

from HeadFirstDesignPatterns.chapter_1.behaviors import QuackBehavior, FlyBehavior, FlyWithWings, Quack, FlyNoWay


class Duck(metaclass=abc.ABCMeta):
    """
    Abstract class of Duck model
    """

    def __init__(self):
        self._fly_behavior = None
        self._quack_behavior = None

    @property
    def fly_behavior(self) -> FlyBehavior:
        return self._fly_behavior

    @fly_behavior.setter
    def fly_behavior(self, behavior: FlyBehavior):
        self._fly_behavior = behavior

    @property
    def quack_behavior(self) -> QuackBehavior:
        return self._quack_behavior

    @quack_behavior.setter
    def quack_behavior(self, behavior: QuackBehavior):
        self._quack_behavior = behavior

    def perform_quack(self):
        self.quack_behavior.quack()

    def perform_fly(self):
        self.fly_behavior.fly()

    @staticmethod
    def swim():
        print("All ducks float, even decoys!")

    @abc.abstractmethod
    def display(self):
        pass


class MallardDuck(Duck):
    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm Mallard duck!")


class ModelDuck(Duck):
    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a model duck")
